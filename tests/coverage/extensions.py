import os
import yaml
from ruamel.yaml import YAML

enable_debug = False


def error(msg):
    print(f"ERROR: {msg}")


def debug(msg):
    if enable_debug:
        print(f"DEBUG: {msg}")


type_to_short_type = {
    'required enumeration': 'req',
    'i8': 'i8',
    'i16': 'i16',
    'i32': 'i32',
    'i64': 'i64',
    'fp32': 'fp32',
    'fp64': 'fp64',
    'string': 'str',
    'binary': 'vbin',
    'boolean': 'bool',
    'timestamp': 'ts',
    'timestamp_tz': 'tstz',
    'date': 'date',
    'time': 'time',
    'interval_year': 'iyear',
    'interval_day': 'iday',
    'uuid': 'uuid',
    'fixedchar<N>': 'fchar',
    'varchar<N>': 'vchar',
    'fixedbinary<N>': 'fbin',
    'decimal<P,S>': 'dec',
    'precision_timestamp<P>': 'pts',
    'precision_timestamp_tz<P>': 'ptstz',
    'struct<T1,T2,...,TN>': 'struct',
    'list<T>': 'list',
    'map<K,V>': 'map',
    'map': 'map',
    'any': 'any',
    'any1': 'any1',
    'any2': 'any2',
    'any3': 'any3',
    'user defined type': 'u!name',

    # added to handle parametrized types
    'fixedchar': 'fchar',
    'varchar': 'vchar',
    'fixedbinary': 'fbin',
    'decimal': 'dec',
    'precision_timestamp': 'pts',
    'precision_timestamp_tz': 'ptstz',
    'struct': 'struct',
    'list': 'list',

    # added to handle geometry type
    'geometry': 'geometry',
}

short_type_to_type = {st: lt for lt, st in type_to_short_type.items()}


class Extension:
    @staticmethod
    def get_base_uri():
        return 'https://github.com/substrait-io/substrait/blob/main/extensions/'

    @staticmethod
    def get_short_type(long_type):
        long_type = long_type.lower().rstrip('?')
        short_type = type_to_short_type.get(long_type, None)

        if short_type is None:
            # remove the type parameters and try again
            if '<' in long_type:
                long_type = long_type[:long_type.find('<')].rstrip('?')
                short_type = type_to_short_type.get(long_type, None)
            if short_type is None:
                if '\n' in long_type:
                    long_type = long_type.split('\n')[-1]
                    short_type = type_to_short_type.get(long_type, None)
            if short_type is None:
                if '!' not in long_type:
                    error(f"Type not found in the mapping: {long_type}")
                return long_type
        return short_type

    @staticmethod
    def get_long_type(short_type):
        if short_type.endswith('?'):
            short_type = short_type[:-1]
        long_type = short_type_to_type.get(short_type, None)
        if long_type is None:
            error(f"Type not found in the mapping: {short_type}")
            return short_type
        return long_type

    @staticmethod
    def get_supported_kernels_from_impls(func):
        overloads = []
        for impl in func['impls']:
            args = []
            if 'args' in impl:
                for arg in impl['args']:
                    if 'value' in arg:
                        arg_type = arg['value']
                        if arg_type.endswith('?'):
                            arg_type = arg_type[:-1]
                        args.append(Extension.get_short_type(arg_type))
                    else:
                        debug(f"arg is not a value type for function: {func['name']} arg must be enum options {arg['options']}")
                        args.append('str')
            overloads.append(FunctionOverload(args, Extension.get_short_type(impl['return']), 'variadic' in impl))
        return overloads

    @staticmethod
    def add_functions_to_map(func_list, function_map, suffix, extension):
        dup_idx = 0
        for func in func_list:
            name = func['name']
            uri = extension[5:]  # strip the ../..
            if name in function_map:
                debug(f"Duplicate function name: {name} renaming to {name}_{suffix} extension: {extension}")
                dup_idx += 1
                name = f"{name}_dup{dup_idx}_{suffix}"
                assert name not in function_map, f"Duplicate function name: {name} renaming to {name}_{suffix} extension: {extension}"
            func['overloads'] = Extension.get_supported_kernels_from_impls(func)
            func['uri'] = uri
            func.pop('description', None)
            func.pop('impls', None)
            function_map[name] = func

    @staticmethod
    def read_substrait_extensions(dir_path: str):
        # read files from extensions directory
        extensions = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.yaml') and file.startswith('functions_'):
                    extensions.append(os.path.join(root, file))

        extensions.sort()

        scalar_functions = {}
        aggregate_functions = {}
        window_functions = {}
        dependencies = {}
        # convert yaml file to a python dictionary
        for extension in extensions:
            suffix = extension[:-5]  # strip .yaml at the end of the extension
            suffix = suffix[suffix.rfind('/') + 1:]  # strip the path and get the name of the extension
            suffix = suffix[suffix.find('_') + 1:]  # get the suffix after the last _

            dependencies[suffix] = Extension.get_base_uri() + extension
            with open(extension, 'r') as fh:
                data = yaml.load(fh, Loader=yaml.FullLoader)
                if 'scalar_functions' in data:
                    Extension.add_functions_to_map(data['scalar_functions'], scalar_functions, suffix, extension)
                if 'aggregate_functions' in data:
                    Extension.add_functions_to_map(data['aggregate_functions'], aggregate_functions, suffix, extension)
                if 'window_functions' in data:
                    Extension.add_functions_to_map(data['window_functions'], scalar_functions, suffix, extension)

        return FunctionRegistry(scalar_functions, aggregate_functions, window_functions, dependencies)


class FunctionType:
    SCALAR = 1
    AGGREGATE = 2
    WINDOW = 3


class FunctionVariant:
    def __init__(self, name, uri, description, args, return_type, variadic, func_type):
        self.name = name
        self.uri = uri
        self.description = description
        self.args = args
        self.return_type = return_type
        self.variadic = variadic
        self.func_type = func_type
        self.test_count = 0

    def __str__(self):
        return f"Function(name={self.name}, uri={self.uri}, description={self.description}, overloads={self.overload}, args={self.args}, result={self.result})"

    def increment_test_count(self, count=1):
        self.test_count += count


class FunctionOverload:
    def __init__(self, args, return_type, variadic):
        self.args = args
        self.return_type = return_type
        self.variadic = variadic

    def __str__(self):
        return f"FunctionOverload(args={self.args}, result={self.return_type}, variadic={self.variadic})"

# define function type enum


class FunctionRegistry:
    registry = dict()
    dependencies = dict()
    scalar_functions = dict()
    aggregate_functions = dict()
    window_functions = dict()
    extensions = set()

    def __init__(self, scalar_functions, aggregate_functions, window_functions, dependencies):
        self.dependencies = dependencies
        self.scalar_functions = scalar_functions
        self.aggregate_functions = aggregate_functions
        self.window_functions = window_functions
        self.add_functions(scalar_functions, FunctionType.SCALAR)
        self.add_functions(aggregate_functions, FunctionType.AGGREGATE)
        self.add_functions(window_functions, FunctionType.WINDOW)

    def add_functions(self, functions, func_type):
        for func in functions.values():
            self.extensions.add(func['uri'])
            f_name = func["name"]
            fun_arr = self.registry.get(f_name, [])
            for overload in func["overloads"]:
                function = FunctionVariant(func["name"], func["uri"], "", overload.args, overload.return_type, overload.variadic, func_type)
                fun_arr.append(function)
            self.registry[f_name] = fun_arr

    def get_function(self, name, args) -> [FunctionVariant]:
        functions = self.registry.get(name, None)
        if functions is None:
            return None
        for function in functions:
            if function.args == args:
                return function

    def get_extension_list(self):
        return list(self.extensions)

    def fill_coverage(self, coverage):
        for func_name, functions in self.registry.items():
            for function in functions:
                coverage.update_coverage(function.uri, func_name, function.args, function.test_count)

