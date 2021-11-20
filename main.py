import sys
from antlr4 import *
from SQLGrammarLexer import SQLGrammarLexer
from SQLGrammarParser import SQLGrammarParser
from CustomSQLGrammarListener import CustomSQLGrammarListener


def main():
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