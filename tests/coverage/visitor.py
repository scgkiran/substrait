# SPDX-License-Identifier: Apache-2.0
import sys
from antlr4 import *
from antlr_generated.TestFileParser import TestFileParser
from antlr_generated.TestFileParserVisitor import TestFileParserVisitor


class TestCaseVisitor(TestFileParserVisitor):
    def visitDoc(self, ctx: TestFileParser.DocContext):
        # TODO Implement this method
        return int(ctx.getText())

    def visitTestGroup(self, ctx: TestFileParser.TestGroupContext):
        # TODO Implement this method
        return self.visitChildren(ctx)

    def visitTestCase(self, ctx: TestFileParser.TestCaseContext):
        # TODO Implement this method
        return self.visitChildren(ctx)
