# SPDX-License-Identifier: Apache-2.0
import os

from antlr4 import FileStream, InputStream, CommonTokenStream
from tests.coverage.antlr_generated.TestFileLexer import TestFileLexer
from tests.coverage.antlr_generated.TestFileParser import TestFileParser
from tests.coverage.visitor import TestCaseVisitor


def parse_one_file(file_path):
    return parse_stream(FileStream(file_path))


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
    visitor = TestCaseVisitor()
    test_file = visitor.visit(tree)
    return test_file


def parse_directory_recursively(dirPath):
    # for each file in directory call parse_one_file
    test_files = []
    for file in os.listdir(dirPath):
        if os.path.isfile(file) and file.endswith(".test"):
            test_file = parse_one_file(file)
            test_files.append(test_file)
        elif os.path.isdir(file):
            parse_directory_recursively(file)


if __name__ == "__main__":
    # TODO move these tests to test folder
    parse_directory_recursively("../cases")
