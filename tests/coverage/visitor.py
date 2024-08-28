# SPDX-License-Identifier: Apache-2.0
from tests.coverage.antlr_generated.TestFileParser import TestFileParser
from tests.coverage.antlr_generated.TestFileParserVisitor import TestFileParserVisitor
from tests.coverage.nodes import CaseGroup, TestFile, TestCase, CaseLiteral


class TestCaseVisitor(TestFileParserVisitor):
    def visitDoc(self, ctx: TestFileParser.DocContext):
        # TODO Implement this method
        version, include = self.visitHeader(ctx.header())
        testcases = []
        for group in ctx.testGroup():
            _, group_tests = self.visitTestGroup(group)
            for test_case in group_tests:
                test_case.base_uri = include
            testcases.extend(group_tests)

        return TestFile(version, include, testcases)

    def visitHeader(self, ctx: TestFileParser.HeaderContext):
        version = self.visitVersion(ctx.version())
        include = self.visitInclude(ctx.include())
        return version, include

    def visitVersion(self, ctx: TestFileParser.VersionContext):
        return ctx.FORMAT_VERSION().getText()

    def visitInclude(self, ctx: TestFileParser.IncludeContext):
        # TODO handle multiple includes
        return ctx.STRING_LITERAL(0).getText().strip("'")

    def visitTestGroupDescription(self, ctx: TestFileParser.TestGroupDescriptionContext):
        group = ctx.DESCRIPTION_LINE().getText().strip("#").strip()
        parts = group.split(":")
        if len(parts) == 2:
            return CaseGroup(parts[0].strip(), parts[1].strip())

        return CaseGroup(group, "")

    def visitTestGroup(self, ctx: TestFileParser.TestGroupContext):
        group = self.visitTestGroupDescription(ctx.testGroupDescription())
        test_cases = []
        for test_case in ctx.testCase():
            testcase = self.visitTestCase(test_case)
            testcase.group = group
            test_cases.append(testcase)
        return group, test_cases

    def visitTestCase(self, ctx: TestFileParser.TestCaseContext):
        # TODO Implement this method
        args = self.visitArguments(ctx.arguments())
        result = self.visitResult(ctx.result())
        options = dict()
        if ctx.func_options() is not None:
            options = self.visitFunc_options(ctx.func_options())
        return TestCase(function=ctx.IDENTIFIER().getText(),
                        base_uri="",
                        group=None,
                        options=options,
                        args=args,
                        result=result,
                        comment="")

    def visitFunc_options(self, ctx: TestFileParser.Func_optionsContext):
        options = {}
        for option in ctx.func_option():
            key, value = self.visitFunc_option(option)
            options[key] = value
        return options

    def visitFunc_option(self, ctx: TestFileParser.Func_optionContext):
        key = ctx.option_name().getText()
        value = ctx.option_value().getText()
        return key, value

    def visitArguments(self, ctx: TestFileParser.ArgumentsContext):
        arguments = []
        for arg in ctx.argument():
            arguments.append(self.visitArgument(arg))
        return arguments

    def visitArgument(self, ctx: TestFileParser.ArgumentContext):
        if ctx.i8Arg() is not None:
            return self.visitI8Arg(ctx.i8Arg())
        if ctx.i16Arg() is not None:
            return self.visitI16Arg(ctx.i16Arg())
        if ctx.i32Arg() is not None:
            return self.visitI32Arg(ctx.i32Arg())
        if ctx.i64Arg() is not None:
            return self.visitI64Arg(ctx.i64Arg())
        if ctx.fp32Arg() is not None:
            return self.visitFp32Arg(ctx.fp32Arg())
        if ctx.fp64Arg() is not None:
            return self.visitFp64Arg(ctx.fp64Arg())
        if ctx.booleanArg() is not None:
            return self.visitBooleanArg(ctx.booleanArg())
        if ctx.stringArg() is not None:
            return self.visitStringArg(ctx.stringArg())
        if ctx.decimalArg() is not None:
            return self.visitDecimalArg(ctx.decimalArg())
        if ctx.dateArg() is not None:
            return self.visitDateArg(ctx.dateArg())
        if ctx.timeArg() is not None:
            return self.visitTimeArg(ctx.timeArg())
        if ctx.timestampArg() is not None:
            return self.visitTimestampArg(ctx.timestampArg())
        if ctx.timestampTzArg() is not None:
            return self.visitTimestampTzArg(ctx.timestampTzArg())
        if ctx.intervalDayArg() is not None:
            return self.visitIntervalDayArg(ctx.intervalDayArg())
        if ctx.intervalYearArg() is not None:
            return self.visitIntervalYearArg(ctx.intervalYearArg())
        if ctx.nullArg() is not None:
            return self.visitNullArg(ctx.nullArg())

        return CaseLiteral(value="unknown_value", type="unknown_type")

    def visitNumericLiteral(self, ctx:TestFileParser.NumericLiteralContext):
        if ctx.INTEGER_LITERAL() is not None:
            return ctx.INTEGER_LITERAL().getText()
        if ctx.DECIMAL_LITERAL() is not None:
            return ctx.DECIMAL_LITERAL().getText()
        return ctx.FLOAT_LITERAL

    def visitNullArg(self, ctx: TestFileParser.NullArgContext):
        datatype = ctx.datatype().getText()
        return CaseLiteral(value=None, type=datatype)

    def visitI8Arg(self, ctx: TestFileParser.I8ArgContext):
        return CaseLiteral(value=ctx.INTEGER_LITERAL().getText(), type="i8")

    def visitI16Arg(self, ctx: TestFileParser.I16ArgContext):
        return CaseLiteral(value=ctx.INTEGER_LITERAL().getText(), type="i16")

    def visitI32Arg(self, ctx: TestFileParser.I32ArgContext):
        return CaseLiteral(value=ctx.INTEGER_LITERAL().getText(), type="i32")

    def visitI64Arg(self, ctx: TestFileParser.I64ArgContext):
        return CaseLiteral(value=ctx.INTEGER_LITERAL().getText(), type="i64")

    def visitFp32Arg(self, ctx: TestFileParser.Fp32ArgContext):
        # TODO add checks on number of decimal places
        return CaseLiteral(value=self.visitNumericLiteral(ctx.numericLiteral()), type=ctx.FP32().getText().lower())

    def visitFp64Arg(self, ctx: TestFileParser.Fp64ArgContext):
        return CaseLiteral(value=self.visitNumericLiteral(ctx.numericLiteral()), type=ctx.FP64().getText().lower())

    def visitBooleanArg(self, ctx: TestFileParser.BooleanArgContext):
        return CaseLiteral(value=ctx.BOOLEAN_LITERAL().getText(), type="bool")

    def visitStringArg(self, ctx: TestFileParser.StringArgContext):
        return CaseLiteral(value=ctx.STRING_LITERAL().getText(), type="str")

    def visitDecimalArg(self, ctx: TestFileParser.DecimalArgContext):
        return CaseLiteral(value=self.visitNumericLiteral(ctx.numericLiteral()), type=ctx.decimalType().getText().lower())

    def visitDateArg(self, ctx: TestFileParser.DateArgContext):
        return CaseLiteral(value=ctx.DATE_LITERAL().getText().strip("'"), type="date")

    def visitTimeArg(self, ctx: TestFileParser.TimeArgContext):
        return CaseLiteral(value=ctx.TIME_LITERAL().getText().strip("'"), type="time")

    def visitTimestampArg(self, ctx: TestFileParser.TimestampArgContext):
        return CaseLiteral(value=ctx.TIMESTAMP_LITERAL().getText().strip("'"), type="ts")

    def visitTimestampTzArg(self, ctx: TestFileParser.TimestampTzArgContext):
        return CaseLiteral(value=ctx.TIMESTAMP_TZ_LITERAL().getText().strip("'"), type="tstz")

    def visitIntervalDayArg(self, ctx: TestFileParser.IntervalDayArgContext):
        return CaseLiteral(value=ctx.INTERVAL_DAY_LITERAL().getText().strip("'"), type="iday")

    def visitIntervalYearArg(self, ctx: TestFileParser.IntervalYearArgContext):
        return CaseLiteral(value=ctx.INTERVAL_YEAR_LITERAL().getText().strip("'"), type="iyear")

    def visitResult(self, ctx: TestFileParser.ResultContext):
        if ctx.argument() is not None:
            return self.visitArgument(ctx.argument())
        return self.visitSubstraitError(ctx.substraitError())

    def visitSubstraitError(self, ctx: TestFileParser.SubstraitErrorContext):
        if ctx.ERROR_RESULT() is not None:
            return "error"
        if ctx.UNDEFINED_RESULT() is not None:
            return "undefined"
        return "unknown_error"
