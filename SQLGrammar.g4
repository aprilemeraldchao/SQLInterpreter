grammar SQLGrammar;

statements: statement+ EOF;
statement: query WS? ';' WS;
query: create | drop | insert | show | select;

create:
	CREATE WS TABLE WS NAME WS? '(' column_definition (
		',' column_definition
	)* ')';
drop: DROP WS TABLE WS NAME;
insert:
	INSERT WS INTO WS NAME WS VALUES WS? '(' WS? value (
		WS? ',' WS? value
	)* WS? ')';
show: SHOW WS TABLES;
select:
	SELECT WS columns WS FROM WS NAME (
		WS WHERE WS NAME WS? '=' WS? value
	)?;

column_definition: WS? NAME WS type WS?;
columns: NAME (WS? ',' WS? NAME)* | STAR;
type: STRING | INT;
value: STRING_VALUE | INT_VALUE;

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
STRING: S T R I N G;
INT: I N T;

NAME: [a-z][a-z0-9_]+;
STAR: ('*');

STRING_VALUE:
	'\'' (~('\'' | '\\' | '\r' | '\n') | '\\' ('\'' | '\\'))* '\'';
INT_VALUE: [0-9]+;

WS: (' ' | '\t' | '\n')+;

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];