# Generated from TestFileParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TestFileParser import TestFileParser
else:
    from TestFileParser import TestFileParser

# This class defines a complete listener for a parse tree produced by TestFileParser.
class TestFileParserListener(ParseTreeListener):

    # Enter a parse tree produced by TestFileParser#doc.
    def enterDoc(self, ctx:TestFileParser.DocContext):
        pass

    # Exit a parse tree produced by TestFileParser#doc.
    def exitDoc(self, ctx:TestFileParser.DocContext):
        pass


    # Enter a parse tree produced by TestFileParser#header.
    def enterHeader(self, ctx:TestFileParser.HeaderContext):
        pass

    # Exit a parse tree produced by TestFileParser#header.
    def exitHeader(self, ctx:TestFileParser.HeaderContext):
        pass


    # Enter a parse tree produced by TestFileParser#version.
    def enterVersion(self, ctx:TestFileParser.VersionContext):
        pass

    # Exit a parse tree produced by TestFileParser#version.
    def exitVersion(self, ctx:TestFileParser.VersionContext):
        pass


    # Enter a parse tree produced by TestFileParser#include.
    def enterInclude(self, ctx:TestFileParser.IncludeContext):
        pass

    # Exit a parse tree produced by TestFileParser#include.
    def exitInclude(self, ctx:TestFileParser.IncludeContext):
        pass


    # Enter a parse tree produced by TestFileParser#testGroupDescription.
    def enterTestGroupDescription(self, ctx:TestFileParser.TestGroupDescriptionContext):
        pass

    # Exit a parse tree produced by TestFileParser#testGroupDescription.
    def exitTestGroupDescription(self, ctx:TestFileParser.TestGroupDescriptionContext):
        pass


    # Enter a parse tree produced by TestFileParser#testCase.
    def enterTestCase(self, ctx:TestFileParser.TestCaseContext):
        pass

    # Exit a parse tree produced by TestFileParser#testCase.
    def exitTestCase(self, ctx:TestFileParser.TestCaseContext):
        pass


    # Enter a parse tree produced by TestFileParser#testGroup.
    def enterTestGroup(self, ctx:TestFileParser.TestGroupContext):
        pass

    # Exit a parse tree produced by TestFileParser#testGroup.
    def exitTestGroup(self, ctx:TestFileParser.TestGroupContext):
        pass


    # Enter a parse tree produced by TestFileParser#arguments.
    def enterArguments(self, ctx:TestFileParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by TestFileParser#arguments.
    def exitArguments(self, ctx:TestFileParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by TestFileParser#result.
    def enterResult(self, ctx:TestFileParser.ResultContext):
        pass

    # Exit a parse tree produced by TestFileParser#result.
    def exitResult(self, ctx:TestFileParser.ResultContext):
        pass


    # Enter a parse tree produced by TestFileParser#argument.
    def enterArgument(self, ctx:TestFileParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TestFileParser#argument.
    def exitArgument(self, ctx:TestFileParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TestFileParser#numericLiteral.
    def enterNumericLiteral(self, ctx:TestFileParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by TestFileParser#numericLiteral.
    def exitNumericLiteral(self, ctx:TestFileParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by TestFileParser#nullArg.
    def enterNullArg(self, ctx:TestFileParser.NullArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#nullArg.
    def exitNullArg(self, ctx:TestFileParser.NullArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#i8Arg.
    def enterI8Arg(self, ctx:TestFileParser.I8ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#i8Arg.
    def exitI8Arg(self, ctx:TestFileParser.I8ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#i16Arg.
    def enterI16Arg(self, ctx:TestFileParser.I16ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#i16Arg.
    def exitI16Arg(self, ctx:TestFileParser.I16ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#i32Arg.
    def enterI32Arg(self, ctx:TestFileParser.I32ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#i32Arg.
    def exitI32Arg(self, ctx:TestFileParser.I32ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#i64Arg.
    def enterI64Arg(self, ctx:TestFileParser.I64ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#i64Arg.
    def exitI64Arg(self, ctx:TestFileParser.I64ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#fp32Arg.
    def enterFp32Arg(self, ctx:TestFileParser.Fp32ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#fp32Arg.
    def exitFp32Arg(self, ctx:TestFileParser.Fp32ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#fp64Arg.
    def enterFp64Arg(self, ctx:TestFileParser.Fp64ArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#fp64Arg.
    def exitFp64Arg(self, ctx:TestFileParser.Fp64ArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#decimalArg.
    def enterDecimalArg(self, ctx:TestFileParser.DecimalArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#decimalArg.
    def exitDecimalArg(self, ctx:TestFileParser.DecimalArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#booleanArg.
    def enterBooleanArg(self, ctx:TestFileParser.BooleanArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#booleanArg.
    def exitBooleanArg(self, ctx:TestFileParser.BooleanArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#stringArg.
    def enterStringArg(self, ctx:TestFileParser.StringArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#stringArg.
    def exitStringArg(self, ctx:TestFileParser.StringArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#dateArg.
    def enterDateArg(self, ctx:TestFileParser.DateArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#dateArg.
    def exitDateArg(self, ctx:TestFileParser.DateArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#timeArg.
    def enterTimeArg(self, ctx:TestFileParser.TimeArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#timeArg.
    def exitTimeArg(self, ctx:TestFileParser.TimeArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#timestampArg.
    def enterTimestampArg(self, ctx:TestFileParser.TimestampArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#timestampArg.
    def exitTimestampArg(self, ctx:TestFileParser.TimestampArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#timestampTzArg.
    def enterTimestampTzArg(self, ctx:TestFileParser.TimestampTzArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#timestampTzArg.
    def exitTimestampTzArg(self, ctx:TestFileParser.TimestampTzArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalYearArg.
    def enterIntervalYearArg(self, ctx:TestFileParser.IntervalYearArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalYearArg.
    def exitIntervalYearArg(self, ctx:TestFileParser.IntervalYearArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalDayArg.
    def enterIntervalDayArg(self, ctx:TestFileParser.IntervalDayArgContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalDayArg.
    def exitIntervalDayArg(self, ctx:TestFileParser.IntervalDayArgContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalYearLiteral.
    def enterIntervalYearLiteral(self, ctx:TestFileParser.IntervalYearLiteralContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalYearLiteral.
    def exitIntervalYearLiteral(self, ctx:TestFileParser.IntervalYearLiteralContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalDayLiteral.
    def enterIntervalDayLiteral(self, ctx:TestFileParser.IntervalDayLiteralContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalDayLiteral.
    def exitIntervalDayLiteral(self, ctx:TestFileParser.IntervalDayLiteralContext):
        pass


    # Enter a parse tree produced by TestFileParser#timeInterval.
    def enterTimeInterval(self, ctx:TestFileParser.TimeIntervalContext):
        pass

    # Exit a parse tree produced by TestFileParser#timeInterval.
    def exitTimeInterval(self, ctx:TestFileParser.TimeIntervalContext):
        pass


    # Enter a parse tree produced by TestFileParser#datatype.
    def enterDatatype(self, ctx:TestFileParser.DatatypeContext):
        pass

    # Exit a parse tree produced by TestFileParser#datatype.
    def exitDatatype(self, ctx:TestFileParser.DatatypeContext):
        pass


    # Enter a parse tree produced by TestFileParser#Boolean.
    def enterBoolean(self, ctx:TestFileParser.BooleanContext):
        pass

    # Exit a parse tree produced by TestFileParser#Boolean.
    def exitBoolean(self, ctx:TestFileParser.BooleanContext):
        pass


    # Enter a parse tree produced by TestFileParser#i8.
    def enterI8(self, ctx:TestFileParser.I8Context):
        pass

    # Exit a parse tree produced by TestFileParser#i8.
    def exitI8(self, ctx:TestFileParser.I8Context):
        pass


    # Enter a parse tree produced by TestFileParser#i16.
    def enterI16(self, ctx:TestFileParser.I16Context):
        pass

    # Exit a parse tree produced by TestFileParser#i16.
    def exitI16(self, ctx:TestFileParser.I16Context):
        pass


    # Enter a parse tree produced by TestFileParser#i32.
    def enterI32(self, ctx:TestFileParser.I32Context):
        pass

    # Exit a parse tree produced by TestFileParser#i32.
    def exitI32(self, ctx:TestFileParser.I32Context):
        pass


    # Enter a parse tree produced by TestFileParser#i64.
    def enterI64(self, ctx:TestFileParser.I64Context):
        pass

    # Exit a parse tree produced by TestFileParser#i64.
    def exitI64(self, ctx:TestFileParser.I64Context):
        pass


    # Enter a parse tree produced by TestFileParser#fp32.
    def enterFp32(self, ctx:TestFileParser.Fp32Context):
        pass

    # Exit a parse tree produced by TestFileParser#fp32.
    def exitFp32(self, ctx:TestFileParser.Fp32Context):
        pass


    # Enter a parse tree produced by TestFileParser#fp64.
    def enterFp64(self, ctx:TestFileParser.Fp64Context):
        pass

    # Exit a parse tree produced by TestFileParser#fp64.
    def exitFp64(self, ctx:TestFileParser.Fp64Context):
        pass


    # Enter a parse tree produced by TestFileParser#string.
    def enterString(self, ctx:TestFileParser.StringContext):
        pass

    # Exit a parse tree produced by TestFileParser#string.
    def exitString(self, ctx:TestFileParser.StringContext):
        pass


    # Enter a parse tree produced by TestFileParser#binary.
    def enterBinary(self, ctx:TestFileParser.BinaryContext):
        pass

    # Exit a parse tree produced by TestFileParser#binary.
    def exitBinary(self, ctx:TestFileParser.BinaryContext):
        pass


    # Enter a parse tree produced by TestFileParser#timestamp.
    def enterTimestamp(self, ctx:TestFileParser.TimestampContext):
        pass

    # Exit a parse tree produced by TestFileParser#timestamp.
    def exitTimestamp(self, ctx:TestFileParser.TimestampContext):
        pass


    # Enter a parse tree produced by TestFileParser#timestampTz.
    def enterTimestampTz(self, ctx:TestFileParser.TimestampTzContext):
        pass

    # Exit a parse tree produced by TestFileParser#timestampTz.
    def exitTimestampTz(self, ctx:TestFileParser.TimestampTzContext):
        pass


    # Enter a parse tree produced by TestFileParser#date.
    def enterDate(self, ctx:TestFileParser.DateContext):
        pass

    # Exit a parse tree produced by TestFileParser#date.
    def exitDate(self, ctx:TestFileParser.DateContext):
        pass


    # Enter a parse tree produced by TestFileParser#time.
    def enterTime(self, ctx:TestFileParser.TimeContext):
        pass

    # Exit a parse tree produced by TestFileParser#time.
    def exitTime(self, ctx:TestFileParser.TimeContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalDay.
    def enterIntervalDay(self, ctx:TestFileParser.IntervalDayContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalDay.
    def exitIntervalDay(self, ctx:TestFileParser.IntervalDayContext):
        pass


    # Enter a parse tree produced by TestFileParser#intervalYear.
    def enterIntervalYear(self, ctx:TestFileParser.IntervalYearContext):
        pass

    # Exit a parse tree produced by TestFileParser#intervalYear.
    def exitIntervalYear(self, ctx:TestFileParser.IntervalYearContext):
        pass


    # Enter a parse tree produced by TestFileParser#uuid.
    def enterUuid(self, ctx:TestFileParser.UuidContext):
        pass

    # Exit a parse tree produced by TestFileParser#uuid.
    def exitUuid(self, ctx:TestFileParser.UuidContext):
        pass


    # Enter a parse tree produced by TestFileParser#userDefined.
    def enterUserDefined(self, ctx:TestFileParser.UserDefinedContext):
        pass

    # Exit a parse tree produced by TestFileParser#userDefined.
    def exitUserDefined(self, ctx:TestFileParser.UserDefinedContext):
        pass


    # Enter a parse tree produced by TestFileParser#fixedChar.
    def enterFixedChar(self, ctx:TestFileParser.FixedCharContext):
        pass

    # Exit a parse tree produced by TestFileParser#fixedChar.
    def exitFixedChar(self, ctx:TestFileParser.FixedCharContext):
        pass


    # Enter a parse tree produced by TestFileParser#varChar.
    def enterVarChar(self, ctx:TestFileParser.VarCharContext):
        pass

    # Exit a parse tree produced by TestFileParser#varChar.
    def exitVarChar(self, ctx:TestFileParser.VarCharContext):
        pass


    # Enter a parse tree produced by TestFileParser#fixedBinary.
    def enterFixedBinary(self, ctx:TestFileParser.FixedBinaryContext):
        pass

    # Exit a parse tree produced by TestFileParser#fixedBinary.
    def exitFixedBinary(self, ctx:TestFileParser.FixedBinaryContext):
        pass


    # Enter a parse tree produced by TestFileParser#decimal.
    def enterDecimal(self, ctx:TestFileParser.DecimalContext):
        pass

    # Exit a parse tree produced by TestFileParser#decimal.
    def exitDecimal(self, ctx:TestFileParser.DecimalContext):
        pass


    # Enter a parse tree produced by TestFileParser#precisionTimestamp.
    def enterPrecisionTimestamp(self, ctx:TestFileParser.PrecisionTimestampContext):
        pass

    # Exit a parse tree produced by TestFileParser#precisionTimestamp.
    def exitPrecisionTimestamp(self, ctx:TestFileParser.PrecisionTimestampContext):
        pass


    # Enter a parse tree produced by TestFileParser#precisionTimestampTZ.
    def enterPrecisionTimestampTZ(self, ctx:TestFileParser.PrecisionTimestampTZContext):
        pass

    # Exit a parse tree produced by TestFileParser#precisionTimestampTZ.
    def exitPrecisionTimestampTZ(self, ctx:TestFileParser.PrecisionTimestampTZContext):
        pass


    # Enter a parse tree produced by TestFileParser#parameterizedType.
    def enterParameterizedType(self, ctx:TestFileParser.ParameterizedTypeContext):
        pass

    # Exit a parse tree produced by TestFileParser#parameterizedType.
    def exitParameterizedType(self, ctx:TestFileParser.ParameterizedTypeContext):
        pass


    # Enter a parse tree produced by TestFileParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:TestFileParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by TestFileParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:TestFileParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by TestFileParser#substraitError.
    def enterSubstraitError(self, ctx:TestFileParser.SubstraitErrorContext):
        pass

    # Exit a parse tree produced by TestFileParser#substraitError.
    def exitSubstraitError(self, ctx:TestFileParser.SubstraitErrorContext):
        pass


    # Enter a parse tree produced by TestFileParser#func_option.
    def enterFunc_option(self, ctx:TestFileParser.Func_optionContext):
        pass

    # Exit a parse tree produced by TestFileParser#func_option.
    def exitFunc_option(self, ctx:TestFileParser.Func_optionContext):
        pass


    # Enter a parse tree produced by TestFileParser#option_name.
    def enterOption_name(self, ctx:TestFileParser.Option_nameContext):
        pass

    # Exit a parse tree produced by TestFileParser#option_name.
    def exitOption_name(self, ctx:TestFileParser.Option_nameContext):
        pass


    # Enter a parse tree produced by TestFileParser#option_value.
    def enterOption_value(self, ctx:TestFileParser.Option_valueContext):
        pass

    # Exit a parse tree produced by TestFileParser#option_value.
    def exitOption_value(self, ctx:TestFileParser.Option_valueContext):
        pass


    # Enter a parse tree produced by TestFileParser#func_options.
    def enterFunc_options(self, ctx:TestFileParser.Func_optionsContext):
        pass

    # Exit a parse tree produced by TestFileParser#func_options.
    def exitFunc_options(self, ctx:TestFileParser.Func_optionsContext):
        pass



del TestFileParser