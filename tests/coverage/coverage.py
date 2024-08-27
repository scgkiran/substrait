# SPDX-License-Identifier: Apache-2.0

from antlr4 import FileStream, InputStream, CommonTokenStream
from antlr_generated.TestFileLexer import TestFileLexer
from antlr4.error.ErrorListener import ErrorListener
from antlr_generated.TestFileParser import TestFileParser
from tests.coverage.visitor import TestCaseVisitor


def parse_one_file(file_path):
    parse_stream(FileStream(file_path))


def parse_string(input_string):
    return parse_stream(InputStream(input_string))


def parse_stream(input_stream):
    # Create a lexer and parser
    lexer = TestFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TestFileParser(token_stream)

    tree = parser.doc()  # This is the entry point of testfile parser
    if parser.getNumberOfSyntaxErrors() > 0:
        print(tree.toStringTree(recog=parser))
        print(f"{parser.getNumberOfSyntaxErrors()} Syntax errors found, exiting")
        return

    # Optionally, print the parse tree in LISP format
    print(tree.toStringTree(recog=parser))

    # TODO use custom visitor to build test cases and compute coverage
    # visitor = TestCaseVisitor()
    # visitor.visit(tree)
    # tree.visit()


def parse_basic_example():
    parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: '/extensions/functions_arithmetic.yaml'

# basic: 'Basic examples without any special cases'
add(120::i8, 5::i8) = 125::i8
add(100::i16, 100::i16) = 200::i16

# overflow: Examples demonstrating overflow behavior
add(120::i8, 10::i8) [overflow:ERROR] = <!ERROR>
"""
    )


def parse_date_time_example():
    parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
    ### SUBSTRAIT_INCLUDE: '/extensions/functions_datetime.yaml'

# timestamps: examples using the timestamp type
lt('2016-12-31T13:30:15'::ts, '2017-12-31T13:30:15'::ts) = true::bool
"""
    )


def parse_decimal_example():
    parse_string(
        """### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: 'extensions/functions_arithmetic_decimal.yaml'

# basic: Basic examples without any special cases
power(8::dec, 2::dec<38, 0>) = 64::fp64
power(1.0::dec, -1.0::dec<38, 0>) = 1.0::fp64
"""
    )


if __name__ == "__main__":
    # TODO move these tests to test folder
    # parse_basic_example()
    parse_date_time_example()
    # parse_decimal_example()
    # parse_one_file("../cases/arithmetic/add.test")
    # parse_one_file("../cases/datetime/lt_datetime.test")
    # parse_one_file("../cases/arithmetic_decimal/power.test")
