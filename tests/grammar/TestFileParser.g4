parser grammar TestFileParser;

options {
    tokenVocab=TestFileLexer;  // This imports the tokens from TestFileLexer.g4
}

doc
    : header (testGroup? testCase+)+ EOF
    ;

header
    : version include
    ;

version
    : SUBSTRAIT_SCALAR_TEST FORMAT_VERSION
    ;

include
    : SUBSTRAIT_INCLUDE STRING (COMMA STRING)?
    ;

testGroup
    : DESCRIPTION_LINE
    ;

testCase
    : functionName=IDENTIFIER OPAREN arguments CPAREN ( OBRACKET func_options CBRACKET )? EQ result
    ;

arguments
    : argument (COMMA argument)*
    ;

result
    : argument
    | substraitError
    ;

// TODO remove the debug rules
argumentOnly : argument EOF ;
integerOnly : INTEGER_LITERAL EOF ;
typeOnly : datatype EOF ;
groupOnly : testGroup EOF ;

argument
    : nullArg
    | i8Arg | i16Arg | i32Arg | i64Arg
    | fp32Arg | fp64Arg
    | booleanArg
    | stringArg
    | decimalArg
    | dateArg
    | timeArg
    | timestampArg
    | timestampTzArg
    | intervalYearArg
    | intervalDayArg
    ;

nullArg: NULL_LITERAL DOUBLE_COLON datatype;

i8Arg: INTEGER_LITERAL DOUBLE_COLON I8;

i16Arg: INTEGER_LITERAL DOUBLE_COLON I16;

i32Arg: INTEGER_LITERAL DOUBLE_COLON I32;

i64Arg: INTEGER_LITERAL DOUBLE_COLON I64;

fp32Arg
    : FLOAT_LITERAL DOUBLE_COLON FP32
    ;

fp64Arg
    : FLOAT_LITERAL DOUBLE_COLON FP64
    ;

booleanArg
    : BOOLEAN_LITERAL DOUBLE_COLON Bool
    ;

stringArg
    : STRING_LITERAL DOUBLE_COLON String
    ;

decimalArg
    : DECIMAL_LITERAL DOUBLE_COLON (FP32 | FP64 | Decimal)
    ;

dateArg
    : DATE_LITERAL DOUBLE_COLON Date
    ;

timeArg
    : TIME_LITERAL DOUBLE_COLON Time
    ;

timestampArg
    : TIMESTAMP_LITERAL DOUBLE_COLON Timestamp
    ;

timestampTzArg
    : TIMESTAMP_TZ_LITERAL DOUBLE_COLON TimestampTZ
    ;

intervalYearArg
    : INTERVAL_YEAR_LITERAL DOUBLE_COLON IntervalYear
    ;

intervalDayArg
    : INTERVAL_DAY_LITERAL DOUBLE_COLON IntervalDay
    ;

intervalYearLiteral
    : PERIOD_PREFIX (years=INTEGER_LITERAL YEAR_SUFFIX) (months=INTEGER_LITERAL M_SUFFIX)?
    | PERIOD_PREFIX (months=INTEGER_LITERAL M_SUFFIX)
    ;

intervalDayLiteral
    : PERIOD_PREFIX (days=INTEGER_LITERAL DAY_SUFFIX) (TIME_PREFIX timeInterval)?
    | PERIOD_PREFIX TIME_PREFIX timeInterval
    ;

timeInterval
    : hours=INTEGER_LITERAL HOUR_SUFFIX (minutes=INTEGER_LITERAL M_SUFFIX)? (seconds=INTEGER_LITERAL SECOND_SUFFIX)?
        (fractionalSeconds=INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | minutes=INTEGER_LITERAL M_SUFFIX (seconds=INTEGER_LITERAL SECOND_SUFFIX)? (fractionalSeconds=INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | seconds=INTEGER_LITERAL SECOND_SUFFIX (fractionalSeconds=INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | fractionalSeconds=INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX
    ;

datatype
    : scalarType
    | parameterizedType
    ;

scalarType
  : Bool #Boolean
  | I8 #i8
  | I16 #i16
  | I32 #i32
  | I64 #i64
  | FP32 #fp32
  | FP64 #fp64
  | String #string
  | Binary #binary
  | Timestamp #timestamp
  | TimestampTZ #timestampTz
  | Date #date
  | Time #time
  | IntervalDay #intervalDay
  | IntervalYear #intervalYear
  | UUID #uuid
  | UserDefined IDENTIFIER #userDefined
  ;

parameterizedType
  : FixedChar isnull=QMARK? O_ANGLE_BRACKET len=numericParameter C_ANGLE_BRACKET #fixedChar
  | VarChar isnull=QMARK? O_ANGLE_BRACKET len=numericParameter C_ANGLE_BRACKET #varChar
  | FixedBinary isnull=QMARK? O_ANGLE_BRACKET len=numericParameter C_ANGLE_BRACKET #fixedBinary
  | Decimal isnull=QMARK? O_ANGLE_BRACKET precision=numericParameter COMMA scale=numericParameter C_ANGLE_BRACKET #decimal
  | PrecisionTimestamp isnull=QMARK? O_ANGLE_BRACKET precision=numericParameter C_ANGLE_BRACKET #precisionTimestamp
  | PrecisionTimestampTZ isnull=QMARK? O_ANGLE_BRACKET precision=numericParameter C_ANGLE_BRACKET #precisionTimestampTZ
//  | Struct isnull='?'? Lt expr (Comma expr)* Gt #struct
//  | NStruct isnull='?'? Lt Identifier expr (Comma Identifier expr)* Gt #nStruct
//  | List isnull='?'? Lt expr Gt #list
//  | Map isnull='?'? Lt key=expr Comma value=expr Gt #map
  ;

numericParameter
  : INTEGER_LITERAL #numericLiteral
  ;

substraitError
    : ERROR_RESULT | UNDEFINED_RESULT
    ;

func_option
    : option_name COLON option_value
    ;

option_name
    : OVERFLOW | ROUNDING
    | IDENTIFIER
    ;

option_value
    : ERROR | SATURATE | SILENT | TIE_TO_EVEN
    ;

func_options
    : func_option (COMMA func_option)*
    ;
