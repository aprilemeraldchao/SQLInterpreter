import sys
from antlr4 import *
from SQLGrammarLexer import SQLGrammarLexer
from SQLGrammarParser import SQLGrammarParser
from CustomSQLGrammarListener import CustomSQLGrammarListener


def main():
    """
    input = InputStream(
        '''
        CREATE TABLE table_1 (col_1 int, col_2 string, col_3 string);
        INSERT INTO table_1 VALUES (123,'abc', 'bb');
        INSERT INTO table_1 VALUES (223,'abc', 'bb');
        SELECT col_1, col_3 FROM table_1;
        SELECT * FROM table_1;
        SELECT col_1, col_2 FROM table_1 WHERE col_1=123;
        SELECT * FROM table_1 WHERE col_1=223;
        '''
    )
    """

    f = open("input.txt", "r")
    input_text = InputStream(f.read())
    lexer = SQLGrammarLexer(input_text)
    stream = CommonTokenStream(lexer)
    parser = SQLGrammarParser(stream)
    tree = parser.statements()

    sqlStatements = CustomSQLGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(sqlStatements, tree)


if __name__ == "__main__":
    main()