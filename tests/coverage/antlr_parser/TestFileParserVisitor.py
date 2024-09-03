# Generated from TestFileParser.g4 by ANTLR 4.13.2
from antlr4 import ParseTreeVisitor

if "." in __name__:
    from .TestFileParser import TestFileParser
else:
    from TestFileParser import TestFileParser

# This class defines a complete generic visitor for a parse tree produced by TestFileParser.


class TestFileParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestFileParser#doc.
    def visitDoc(self, ctx: TestFileParser.DocContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#header.
    def visitHeader(self, ctx: TestFileParser.HeaderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#version.
    def visitVersion(self, ctx: TestFileParser.VersionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#include.
    def visitInclude(self, ctx: TestFileParser.IncludeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#testGroupDescription.
    def visitTestGroupDescription(
        self, ctx: TestFileParser.TestGroupDescriptionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#testCase.
    def visitTestCase(self, ctx: TestFileParser.TestCaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#testGroup.
    def visitTestGroup(self, ctx: TestFileParser.TestGroupContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#arguments.
    def visitArguments(self, ctx: TestFileParser.ArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#result.
    def visitResult(self, ctx: TestFileParser.ResultContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#argument.
    def visitArgument(self, ctx: TestFileParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#numericLiteral.
    def visitNumericLiteral(self, ctx: TestFileParser.NumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#nullArg.
    def visitNullArg(self, ctx: TestFileParser.NullArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i8Arg.
    def visitI8Arg(self, ctx: TestFileParser.I8ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i16Arg.
    def visitI16Arg(self, ctx: TestFileParser.I16ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i32Arg.
    def visitI32Arg(self, ctx: TestFileParser.I32ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i64Arg.
    def visitI64Arg(self, ctx: TestFileParser.I64ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fp32Arg.
    def visitFp32Arg(self, ctx: TestFileParser.Fp32ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fp64Arg.
    def visitFp64Arg(self, ctx: TestFileParser.Fp64ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#decimalArg.
    def visitDecimalArg(self, ctx: TestFileParser.DecimalArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#booleanArg.
    def visitBooleanArg(self, ctx: TestFileParser.BooleanArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#stringArg.
    def visitStringArg(self, ctx: TestFileParser.StringArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#dateArg.
    def visitDateArg(self, ctx: TestFileParser.DateArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timeArg.
    def visitTimeArg(self, ctx: TestFileParser.TimeArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timestampArg.
    def visitTimestampArg(self, ctx: TestFileParser.TimestampArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timestampTzArg.
    def visitTimestampTzArg(self, ctx: TestFileParser.TimestampTzArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalYearArg.
    def visitIntervalYearArg(self, ctx: TestFileParser.IntervalYearArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalDayArg.
    def visitIntervalDayArg(self, ctx: TestFileParser.IntervalDayArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalYearLiteral.
    def visitIntervalYearLiteral(self, ctx: TestFileParser.IntervalYearLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalDayLiteral.
    def visitIntervalDayLiteral(self, ctx: TestFileParser.IntervalDayLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timeInterval.
    def visitTimeInterval(self, ctx: TestFileParser.TimeIntervalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#datatype.
    def visitDatatype(self, ctx: TestFileParser.DatatypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#Boolean.
    def visitBoolean(self, ctx: TestFileParser.BooleanContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i8.
    def visitI8(self, ctx: TestFileParser.I8Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i16.
    def visitI16(self, ctx: TestFileParser.I16Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i32.
    def visitI32(self, ctx: TestFileParser.I32Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#i64.
    def visitI64(self, ctx: TestFileParser.I64Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fp32.
    def visitFp32(self, ctx: TestFileParser.Fp32Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fp64.
    def visitFp64(self, ctx: TestFileParser.Fp64Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#string.
    def visitString(self, ctx: TestFileParser.StringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#binary.
    def visitBinary(self, ctx: TestFileParser.BinaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timestamp.
    def visitTimestamp(self, ctx: TestFileParser.TimestampContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#timestampTz.
    def visitTimestampTz(self, ctx: TestFileParser.TimestampTzContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#date.
    def visitDate(self, ctx: TestFileParser.DateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#time.
    def visitTime(self, ctx: TestFileParser.TimeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalDay.
    def visitIntervalDay(self, ctx: TestFileParser.IntervalDayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#intervalYear.
    def visitIntervalYear(self, ctx: TestFileParser.IntervalYearContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#uuid.
    def visitUuid(self, ctx: TestFileParser.UuidContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#userDefined.
    def visitUserDefined(self, ctx: TestFileParser.UserDefinedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fixedChar.
    def visitFixedChar(self, ctx: TestFileParser.FixedCharContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#varChar.
    def visitVarChar(self, ctx: TestFileParser.VarCharContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#fixedBinary.
    def visitFixedBinary(self, ctx: TestFileParser.FixedBinaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#decimal.
    def visitDecimal(self, ctx: TestFileParser.DecimalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#precisionTimestamp.
    def visitPrecisionTimestamp(self, ctx: TestFileParser.PrecisionTimestampContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#precisionTimestampTZ.
    def visitPrecisionTimestampTZ(
        self, ctx: TestFileParser.PrecisionTimestampTZContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#parameterizedType.
    def visitParameterizedType(self, ctx: TestFileParser.ParameterizedTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#integerLiteral.
    def visitIntegerLiteral(self, ctx: TestFileParser.IntegerLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#substraitError.
    def visitSubstraitError(self, ctx: TestFileParser.SubstraitErrorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#func_option.
    def visitFunc_option(self, ctx: TestFileParser.Func_optionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#option_name.
    def visitOption_name(self, ctx: TestFileParser.Option_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#option_value.
    def visitOption_value(self, ctx: TestFileParser.Option_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TestFileParser#func_options.
    def visitFunc_options(self, ctx: TestFileParser.Func_optionsContext):
        return self.visitChildren(ctx)


del TestFileParser
