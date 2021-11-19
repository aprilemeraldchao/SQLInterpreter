# Generated from SQLGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLGrammarParser import SQLGrammarParser
else:
    from SQLGrammarParser import SQLGrammarParser

# This class defines a complete listener for a parse tree produced by SQLGrammarParser.
class SQLGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by SQLGrammarParser#statements.
    def enterStatements(self, ctx:SQLGrammarParser.StatementsContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#statements.
    def exitStatements(self, ctx:SQLGrammarParser.StatementsContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#statement.
    def enterStatement(self, ctx:SQLGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#statement.
    def exitStatement(self, ctx:SQLGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#query.
    def enterQuery(self, ctx:SQLGrammarParser.QueryContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#query.
    def exitQuery(self, ctx:SQLGrammarParser.QueryContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#create.
    def enterCreate(self, ctx:SQLGrammarParser.CreateContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#create.
    def exitCreate(self, ctx:SQLGrammarParser.CreateContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#drop.
    def enterDrop(self, ctx:SQLGrammarParser.DropContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#drop.
    def exitDrop(self, ctx:SQLGrammarParser.DropContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#insert.
    def enterInsert(self, ctx:SQLGrammarParser.InsertContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#insert.
    def exitInsert(self, ctx:SQLGrammarParser.InsertContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#show.
    def enterShow(self, ctx:SQLGrammarParser.ShowContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#show.
    def exitShow(self, ctx:SQLGrammarParser.ShowContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#select.
    def enterSelect(self, ctx:SQLGrammarParser.SelectContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#select.
    def exitSelect(self, ctx:SQLGrammarParser.SelectContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#column_definition.
    def enterColumn_definition(self, ctx:SQLGrammarParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#column_definition.
    def exitColumn_definition(self, ctx:SQLGrammarParser.Column_definitionContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#columns.
    def enterColumns(self, ctx:SQLGrammarParser.ColumnsContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#columns.
    def exitColumns(self, ctx:SQLGrammarParser.ColumnsContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#data_type.
    def enterData_type(self, ctx:SQLGrammarParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#data_type.
    def exitData_type(self, ctx:SQLGrammarParser.Data_typeContext):
        pass


    # Enter a parse tree produced by SQLGrammarParser#value.
    def enterValue(self, ctx:SQLGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#value.
    def exitValue(self, ctx:SQLGrammarParser.ValueContext):
        pass



del SQLGrammarParser