from antlr4 import InputStream
from tests.coverage.case_file_parser import parse_stream, parse_one_file
from tests.coverage.nodes import CaseLiteral


def parse_string(input_string):
    return parse_stream(InputStream(input_string))


def test_parse_basic_example():
    test_file = parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: '/extensions/functions_arithmetic.yaml'

# basic: 'Basic examples without any special cases'
add(120::i8, 5::i8) = 125::i8
add(100::i16, 100::i16) = 200::i16

# overflow: Examples demonstrating overflow behavior
add(120::i8, 10::i8) [overflow:ERROR] = <!ERROR>
"""
    )
    assert len(test_file.testcases) == 3


def test_parse_date_time_example():
    test_file = parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
    ### SUBSTRAIT_INCLUDE: '/extensions/functions_datetime.yaml'

# timestamps: examples using the timestamp type
lt('2016-12-31T13:30:15'::ts, '2017-12-31T13:30:15'::ts) = true::bool
"""
    )
    assert len(test_file.testcases) == 1
    assert test_file.testcases[0].func_name == "lt"
    assert test_file.testcases[0].base_uri == "/extensions/functions_datetime.yaml"
    assert test_file.testcases[0].group.name == "timestamps"
    assert (
        test_file.testcases[0].group.description == "examples using the timestamp type"
    )
    assert test_file.testcases[0].result == CaseLiteral("true", "bool")
    assert test_file.testcases[0].args[0] == CaseLiteral("2016-12-31T13:30:15", "ts")
    assert test_file.testcases[0].args[1] == CaseLiteral("2017-12-31T13:30:15", "ts")


def test_parse_decimal_example():
    test_file = parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: 'extensions/functions_arithmetic_decimal.yaml'

# basic: Basic examples without any special cases
power(8::dec<38,0>, 2::dec<38, 0>) = 64::fp64
power(1.0::dec<38, 0>, -1.0::dec<38, 0>) = 1.0::fp64
"""
    )
    assert len(test_file.testcases) == 2
    assert test_file.testcases[0].func_name == "power"
    assert (
        test_file.testcases[0].base_uri
        == "extensions/functions_arithmetic_decimal.yaml"
    )
    assert test_file.testcases[0].group.name == "basic"
    assert (
        test_file.testcases[0].group.description
        == "Basic examples without any special cases"
    )
    assert test_file.testcases[0].result == CaseLiteral("64", "fp64")
    assert test_file.testcases[0].args[0] == CaseLiteral("8", "dec<38,0>")
    assert test_file.testcases[0].args[1] == CaseLiteral("2", "dec<38,0>")


def test_parse_file():
    test_file = parse_one_file("../cases/arithmetic/add.test")
    assert len(test_file.testcases) == 15
    assert test_file.testcases[0].func_name == "add"
    assert test_file.testcases[0].base_uri == "/extensions/functions_arithmetic.yaml"
    assert test_file.include == "/extensions/functions_arithmetic.yaml"

    test_file = parse_one_file("../cases/datetime/lt_datetime.test")
    assert len(test_file.testcases) == 13
    assert test_file.testcases[0].func_name == "lt"
    assert test_file.testcases[0].base_uri == "/extensions/functions_datetime.yaml"

    test_file = parse_one_file("../cases/arithmetic_decimal/power.test")
    assert len(test_file.testcases) == 9
    assert test_file.testcases[0].func_name == "power"
    assert (
        test_file.testcases[0].base_uri
        == "extensions/functions_arithmetic_decimal.yaml"
    )
