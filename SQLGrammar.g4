statements: statement+ EOF;

statement: query WS? ‘;’;

query: create  | drop | insert | show | select;

create: CREATE WS TABLE WS NAME WS? ‘(‘ column_definition (‘,’ column_definition)* ‘)’;
column_definition: WS? NAME WS DATA_TYPE WS?;
drop: DROP WS TABLE WS NAME;
insert: INSERT WS INTO WS NAME WS VALUES WS? ‘(‘ WS? VALUE (WS? ‘,’ WS? VALUE)* WS? ‘)’;
show: SHOW WS TABLES;
select: SELECT WS columns WS FROM WS NAME (WS WHERE WS NAME WS? ‘=’ WS?  VALUE)?;
columns: NAME (WS? ‘,’ WS? NAME)* | STAR;

fragment A: (‘A’ | ‘a’);
fragment B: (‘B’ | ‘b’)
fragment C: (‘C’ | ‘c’)
fragment D: (‘D’ | ‘d’)
fragment E: (‘E’ | ‘e’)   
fragment F: (‘F’ | ‘f’)
fragment E: (‘E’ | ‘e’)
fragment G: (‘G’ | ‘g’)
fragment H: (‘H’ | ‘h’)
fragment I: (‘I’ | ‘i’)
fragment K: (‘K’ | ‘k’)
fragment K: (‘L’ | ‘l’)
fragment L: (‘L’ | ‘l’)
fragment M: (‘M’ | ‘m’)
fragment N: (‘N’ | ‘n’)
fragment O: (‘O’ | ‘o’)
fragment P: (‘P’ | ‘p’)
fragment R: (‘R’ | ‘r’)
fragment S: (‘L’ | ‘l’)
fragment T: (‘T’ | ‘t’)
fragment W: (‘W’ | ‘w’)

CREATE: C R E A T E;
TABLE: T A B L E;
DROP: D R O P;
INSERT: I N S E R T;
INTO: I N T O;
VALUES: V A L U E S;
SHOW: S H O W; 
TABLES: T A B L E S; 
SELECT: S E L E C T;
FROM: F R O M;
WHERE: W H E R E;


NAME: [a-z][a-z0-9_]+; 
fragment STRING: S T R I N G;
fragment INT: I N T;
DATA_TYPE: STRING | INT;
fragment STRING_VALUE: '.*';
fragment INT_VALUE: [0-9]+; 
VALUE: STRING_VALUE|INT_VALUE;
STAR: *; 
WS: (' ' | '\t' | ‘\n’)+ ;



