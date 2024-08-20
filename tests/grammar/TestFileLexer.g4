lexer grammar TestFileLexer;

// Whitespace and comment handling
LineComment   : '//' ~[\r\n]* -> channel(HIDDEN) ;
BlockComment  : ( '/*' ( ~'*' | '*'+ ~[*/] ) '*'* '*/' ) -> channel(HIDDEN) ;
Whitespace    : [ \t\r\n]+ -> channel(HIDDEN) ;

// Substrait is case-insensitive, ANTLR is not. So, in order to define our
// keywords in a somewhat readable way, we have to define these shortcuts.

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

fragment DIGIT: [0-9];

fragment INTEGER
  : '0'
  | [1-9] [0-9]*
  ;

SUBSTRAIT_SCALAR_TEST
    : '### SUBSTRAIT_SCALAR_TEST:'
    ;

FORMAT_VERSION
    : 'v' DIGIT+ ('.' DIGIT+)?
    ;

SUBSTRAIT_INCLUDE
    : '### SUBSTRAIT_INCLUDE:'
    ;

DESCRIPTION_LINE
    : '# ' ~[\r\n]* '\r'? '\n'
    ;

ERROR_RESULT
    : '<!ERROR>'
    ;

UNDEFINED_RESULT
    : '<!UNDEFINED>'
    ;

OVERFLOW: 'overlfow';
ROUNDING: 'rounding';
ERROR: 'ERROR';
SATURATE: 'SATURATE';
SILENT: 'SILENT';
TIE_TO_EVEN: 'TIE_TO_EVEN';
NAN: 'NAN';

STRING_LITERAL
    : '"' (~["\r\n])* '"'
    ;

INTEGER_LITERAL
    : [+-]? INTEGER
    ;

DECIMAL_LITERAL
    : [+-]? [0-9]+ ('.' [0-9]+)?
    ;

FLOAT_LITERAL
    : [+-]? [0-9]+ ('.' [0-9]*)? ( [eE] [+-]? [0-9]+ )?
    | [+-]? 'inf'
    | 'nan' | 'NaN'
    | 'snan'
    ;

BOOLEAN_LITERAL
    : 'true' | 'false'
    ;


fragment FourDigits: [0-9][0-9][0-9][0-9];
fragment TwoDigits: [0-9][0-9];

DATE_LITERAL
    : '\'' FourDigits '-' TwoDigits '-' TwoDigits '\''
    ;

TIME_LITERAL
    : '\'' TwoDigits ':' TwoDigits ':' TwoDigits ( '.' [0-9]+ )? '\''
    ;

TIMESTAMP_LITERAL
    : '\'' FourDigits '-' TwoDigits '-' TwoDigits 'T' TwoDigits ':' TwoDigits ':' TwoDigits ( '.' [0-9]+ )? '\''
    ;

TIMESTAMP_TZ_LITERAL
    : '\'' FourDigits '-' TwoDigits '-' TwoDigits 'T' TwoDigits ':' TwoDigits ':' TwoDigits ( '.' [0-9]+ )?
        [+-] TwoDigits ':' TwoDigits '\''
    ;

PERIOD_PREFIX: 'P';
TIME_PREFIX: 'T';
YEAR_SUFFIX: 'Y';
M_SUFFIX: 'M';  // used for both months and minutes
DAY_SUFFIX: 'D';
HOUR_SUFFIX: 'H';
SECOND_SUFFIX: 'S';
FRACTIONAL_SECOND_SUFFIX: 'F';

INTERVAL_YEAR_LITERAL
    : '\'' PERIOD_PREFIX INTEGER_LITERAL YEAR_SUFFIX (INTEGER_LITERAL M_SUFFIX)? '\''
    | '\'' PERIOD_PREFIX INTEGER_LITERAL M_SUFFIX '\''
    ;

INTERVAL_DAY_LITERAL
    : '\'' PERIOD_PREFIX INTEGER_LITERAL DAY_SUFFIX (TIME_PREFIX TIME_INTERVAL)? '\''
    | '\'' PERIOD_PREFIX TIME_PREFIX TIME_INTERVAL '\''
    ;

fragment TIME_INTERVAL
    : INTEGER_LITERAL HOUR_SUFFIX (INTEGER_LITERAL M_SUFFIX)? (INTEGER_LITERAL SECOND_SUFFIX)?
        (INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | INTEGER_LITERAL M_SUFFIX (INTEGER_LITERAL SECOND_SUFFIX)? (INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | INTEGER_LITERAL SECOND_SUFFIX (INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX)?
    | INTEGER_LITERAL FRACTIONAL_SECOND_SUFFIX
    ;

NULL_LITERAL: 'null';

// short names for types
Bool: B O O L;
I8       : I '8';
I16      : I '16';
I32      : I '32';
I64      : I '64';
FP32     : F P '32';
FP64     : F P '64';
String   : S T R;
Binary   : V B I N;
Timestamp: T S;
TimestampTZ: T S T Z;
Date     : D A T E;
Time     : T I M E;
IntervalYear: I Y E A R;
IntervalDay: I D A Y;
UUID     : U U I D;
Decimal  : D E C;
PrecisionTimestamp: P T S;
PrecisionTimestampTZ: P T S T Z;
FixedChar: F C H A R;
VarChar  : V C H A R;
FixedBinary: F B I N;
Struct   : S T R U C T;
NStruct  : N S T R U C T;
List     : L I S T;
Map      : M A P;
ANY      : A N Y;
UserDefined: U '!';

DOUBLE_COLON: '::';

IDENTIFIER
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

// ORGANIZE
O_ANGLE_BRACKET: '<';
C_ANGLE_BRACKET: '>';
OPAREN: '(';
CPAREN: ')';
OBRACKET: '[';
CBRACKET: ']';
COMMA: ',';
EQ: '=';
COLON: ':';
QMARK: '?';
HASH: '#';
DOT: '.';

STRING
    : '\'' ('\\' . | '\'\'' | ~['\\])* '\''
    ;

