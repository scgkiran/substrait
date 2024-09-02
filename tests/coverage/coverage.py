# SPDX-License-Identifier: Apache-2.0

from tests.coverage.case_file_parser import load_all_testcases
from tests.coverage.extensions import Extension, error


class FunctionTestCoverage:
    function_name: str
    test_count: int
    function_variant_coverage: {str: int}

    def __init__(self, function_name):
        self.function_name = function_name
        self.test_count = 0
        self.function_variant_coverage = dict()

    def update_coverage(self, function_variant):
        if function_variant not in self.function_variant_coverage:
            self.function_variant_coverage[function_variant] = 0
        self.function_variant_coverage[function_variant] += 1
        self.test_count += 1


class FileTestCoverage:
    file_name: str
    test_count: int
    function_coverage: {str: FunctionTestCoverage}

    def __init__(self, file_name):
        self.file_name = file_name
        self.test_count = 0
        self.function_coverage = dict()

    def update_coverage(self, func_name, args):
        key = f"{func_name}({", ".join(args)})"
        if func_name not in self.function_coverage:
            self.function_coverage[func_name] = FunctionTestCoverage(func_name)
        self.function_coverage[func_name].update_coverage(key)
        self.test_count += 1


class TestCoverage:
    file_coverage: {str: FileTestCoverage}
    test_count: int

    def __init__(self):
        self.file_coverage = dict()
        self.test_count = 0

    def update_coverage(self, ext_uri, function, args):
        if ext_uri not in self.file_coverage:
            self.file_coverage[ext_uri] = FileTestCoverage(ext_uri)
        self.file_coverage[ext_uri].update_coverage(function, args)
        self.test_count += 1

    def dump_coverage(self):
        for file_coverage in self.file_coverage.values():
            print(f"File: {file_coverage.file_name}")
            for function_coverage in file_coverage.function_coverage.values():
                print(f"\tFunction: {function_coverage.function_name}: {function_coverage.test_count}")
                for sig, test_count in function_coverage.function_variant_coverage.items():
                    print(f"\t\t{sig}: {test_count}")


def update_test_count(test_case_files, function_registry, coverage):
    for test_file in test_case_files:
        for test_case in test_file.testcases:
            function_variant = function_registry.get_function(test_case.func_name, test_case.get_arg_types())
            if function_variant is not None:
                if function_variant.return_type != test_case.get_return_type() and not test_case.is_return_type_error():
                    error(f"Return type mismatch in function {test_case.func_name}: {function_variant.return_type} != {test_case.get_return_type()}")
                coverage.update_coverage(function_variant.uri, test_case.func_name, test_case.get_arg_types())
            else:
                print(f"Function not found: {test_case.func_name}({test_case.args})")


if __name__ == "__main__":
    test_files = load_all_testcases('../cases')
    extensions = Extension.read_substrait_extensions("../../extensions")
    coverage = TestCoverage()
    update_test_count(test_files, extensions, coverage)
    coverage.dump_coverage()

