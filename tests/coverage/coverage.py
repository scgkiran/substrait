# SPDX-License-Identifier: Apache-2.0
from collections import defaultdict

from tests.coverage.case_file_parser import load_all_testcases
from tests.coverage.extensions import Extension, error, FunctionRegistry


class FunctionTestCoverage:
    function_name: str
    test_count: int
    function_variant_coverage: defaultdict[str, int]

    def __init__(self, function_name):
        self.function_name = function_name
        self.test_count = 0
        self.function_variant_coverage = defaultdict(int)

    def update_coverage(self, function_variant, count):
        self.function_variant_coverage[function_variant] += count
        self.test_count += count


class FileTestCoverage:
    file_name: str
    test_count: int
    function_coverage: dict[str, FunctionTestCoverage]

    def __init__(self, file_name):
        self.file_name = file_name
        self.test_count = 0
        self.function_coverage = dict()

    def update_coverage(self, func_name, args, count):
        key = f"{func_name}({', '.join(args)})"
        if func_name not in self.function_coverage:
            self.function_coverage[func_name] = FunctionTestCoverage(func_name)
        self.function_coverage[func_name].update_coverage(key, count)
        self.test_count += count


class TestCoverage:
    file_coverage: dict[str, FileTestCoverage]
    test_count: int

    def __init__(self, ext_uris):
        self.file_coverage = dict()
        self.test_count = 0
        for ext_uri in ext_uris:
            self.file_coverage[ext_uri] = FileTestCoverage(ext_uri)

    def update_coverage(self, ext_uri, function, args, count):
        if ext_uri not in self.file_coverage:
            self.file_coverage[ext_uri] = FileTestCoverage(ext_uri)
        self.file_coverage[ext_uri].update_coverage(function, args, count)
        self.test_count += count

    def dump_coverage(self):
        covered_variants = 0
        total_variants = 0
        for file_coverage in self.file_coverage.values():
            for function_coverage in file_coverage.function_coverage.values():
                for (
                    sig,
                    test_count,
                ) in function_coverage.function_variant_coverage.items():
                    total_variants += 1
                    if test_count > 0:
                        covered_variants += 1
                    print(f"{file_coverage.file_name} \t\t{sig}: {test_count}")
        print(
            f"Total test count: {self.test_count}, {covered_variants}/{total_variants} function variants are covered"
        )


def update_test_count(test_case_files: list, function_registry: FunctionRegistry):
    for test_file in test_case_files:
        for test_case in test_file.testcases:
            function_variant = function_registry.get_function(
                test_case.func_name, test_case.get_arg_types()
            )
            if function_variant:
                if (
                    function_variant.return_type != test_case.get_return_type()
                    and not test_case.is_return_type_error()
                ):
                    error(
                        f"Return type mismatch in function {test_case.func_name}: {function_variant.return_type} != {test_case.get_return_type()}"
                    )
                    continue
                function_variant.increment_test_count()
            else:
                error(f"Function not found: {test_case.func_name}({test_case.args})")


if __name__ == "__main__":
    test_files = load_all_testcases("../cases")
    function_registry = Extension.read_substrait_extensions("../../extensions")
    coverage = TestCoverage(function_registry.get_extension_list())
    update_test_count(test_files, function_registry)
    function_registry.fill_coverage(coverage)
    coverage.dump_coverage()
