from antlr4 import FileStream, InputStream, CommonTokenStream
from antlr_generated.TestFileLexer import TestFileLexer
from antlr4.error.ErrorListener import ErrorListener
from antlr_generated.TestFileParser import TestFileParser
from tests.coverage.visitor import TestCaseVisitor

def load_file(file_path):
    with open(file_path, 'r') as file:
        parse_string(file.read())


def parse_string(input_string, rule_name='doc'):

    # Read input (e.g., from a file or string)
    input_stream = InputStream(input_string)

    # Create a lexer and parser
    lexer = TestFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TestFileParser(token_stream)

    # tree = parser.doc()  # This is the entry point of testfile parser
    tree = get_parse_tree(parser, rule_name)
    if parser.getNumberOfSyntaxErrors() > 0:
        print(tree.toStringTree(recog=parser))
        print(f"{parser.getNumberOfSyntaxErrors()} Syntax errors found, exiting")
        return

    # Optionally, print the parse tree in LISP format
    print(tree.toStringTree(recog=parser))

    visitor = TestCaseVisitor()
    # visitor.visit(tree)

    # tree.visit()


def get_parse_tree(parser, rule_name):
    if rule_name == 'doc':
        return parser.doc()
    elif rule_name == 'integerOnly':
        return parser.integerOnly()
    elif rule_name == 'argumentOnly':
        return parser.argumentOnly()
    elif rule_name == 'typeOnly':
        return parser.typeOnly()
    else:
        return parser.groupOnly()

def parse_header():
    parse_string('''### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: '/extensions/functions_arithmetic.yaml'
''')


def parse_argument():
    parse_string('120::I8', "argumentOnly")


def parse_interger():
    parse_string('120', "integerOnly")

def parse_type(typeStr):
    parse_string(typeStr, "typeOnly")

def parse_testcase():
    parse_string('add(120::i8, 5::i8) = 125::i8')


def parse_group():
    parse_string("# basic: 'Basic examples without any special cases'", "groupOnly")

def parse_basic_example():
    parse_string('''### SUBSTRAIT_SCALAR_TEST: v1.0
### SUBSTRAIT_INCLUDE: '/extensions/functions_arithmetic.yaml'

# basic: 'Basic examples without any special cases'
add(120::i8, 5::i8) = 125::i8
add(100::i16, 100::i16) = 200::i16

# overflow: Examples demonstrating overflow behavior
add(120::i8, 10::i8) [overflow:ERROR] = <!ERROR>
''')


def parse_one_file():
    load_file("../cases/arithmetic/add.test")


if __name__ == '__main__':
    parse_one_file()
    # TODO get rid of debug code
    # parse_basic_example()
    # parse_group()
    # parse_argument()
    # parse_type("date")
    # parse_type("i8")
