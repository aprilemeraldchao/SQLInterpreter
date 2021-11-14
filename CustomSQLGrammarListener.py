# Generated from SQLGrammar.g4 by ANTLR 4.9
from antlr4 import *
from SQLGrammarListener import SQLGrammarListener

if __name__ is not None and "." in __name__:
    from .SQLGrammarParser import SQLGrammarParser
else:
    from SQLGrammarParser import SQLGrammarParser

# This class defines a complete listener for a parse tree produced by SQLGrammarParser.
class CustomSQLGrammarListener(SQLGrammarListener):
    class Table:
        def __init__(self, name, cols):
            self.name = name
            self.colDefs = cols
            self.rows = []

        def insert(self, values):
            self.rows.append(values)

        def __str__(self):
            toStr = "Table: " + self.name + "\n"
            toStr += "\t".join([colDef[0] for colDef in self.colDefs]) + "\n"
            toStr += (
                "\t".join(["(" + colDef[1] + ")" for colDef in self.colDefs]) + "\n"
            )
            for row in self.rows:
                for value in row:
                    toStr += value + "\t"
                toStr += "\n"
            return toStr

    def __init__(self):
        self.tables = {}

    # Enter a parse tree produced by SQLGrammarParser#statements.
    def enterStatements(self, ctx: SQLGrammarParser.StatementsContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#statements.
    def exitStatements(self, ctx: SQLGrammarParser.StatementsContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#statement.
    def enterStatement(self, ctx: SQLGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#statement.
    def exitStatement(self, ctx: SQLGrammarParser.StatementContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#query.
    def enterQuery(self, ctx: SQLGrammarParser.QueryContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#query.
    def exitQuery(self, ctx: SQLGrammarParser.QueryContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#create.
    def enterCreate(self, ctx: SQLGrammarParser.CreateContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#create.
    def exitCreate(self, ctx: SQLGrammarParser.CreateContext):
        tableName = ctx.NAME().getText()
        cols = []
        for colDef in ctx.column_definition():
            colName = colDef.NAME().getText()
            colType = "string" if colDef.type().STRING() else "int"
            cols.append((colName, colType))
        self.tables[tableName] = self.Table(tableName, cols)
        print(">Created", tableName, "Table\n")

    # Enter a parse tree produced by SQLGrammarParser#drop.
    def enterDrop(self, ctx: SQLGrammarParser.DropContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#drop.
    def exitDrop(self, ctx: SQLGrammarParser.DropContext):
        tableName = ctx.NAME().getText()
        self.tables.pop(tableName)
        print(">Dropped", tableName, "Table\n")

    # Enter a parse tree produced by SQLGrammarParser#insert.
    def enterInsert(self, ctx: SQLGrammarParser.InsertContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#insert.
    def exitInsert(self, ctx: SQLGrammarParser.InsertContext):
        tableName = ctx.NAME().getText()
        values = []
        for value in ctx.value():
            val = (
                value.STRING_VALUE().getText()
                if value.STRING_VALUE()
                else value.INT_VALUE().getText()
            )
            values.append(val)
        # TBD check if values match col defs
        self.tables[tableName].insert(values)
        print(">Inserted", "(" + ", ".join(values) + ")", "into", tableName, "Table")

    # Enter a parse tree produced by SQLGrammarParser#show.
    def enterShow(self, ctx: SQLGrammarParser.ShowContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#show.
    def exitShow(self, ctx: SQLGrammarParser.ShowContext):
        print(">Showing tables")
        if len(self.tables) == 0:
            print("No tables")
            print()
        for table in self.tables.values():
            print(table)

    # Enter a parse tree produced by SQLGrammarParser#select.
    def enterSelect(self, ctx: SQLGrammarParser.SelectContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#select.
    def exitSelect(self, ctx: SQLGrammarParser.SelectContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#column_definition.
    def enterColumn_definition(self, ctx: SQLGrammarParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#column_definition.
    def exitColumn_definition(self, ctx: SQLGrammarParser.Column_definitionContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#columns.
    def enterColumns(self, ctx: SQLGrammarParser.ColumnsContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#columns.
    def exitColumns(self, ctx: SQLGrammarParser.ColumnsContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#type.
    def enterType(self, ctx: SQLGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#type.
    def exitType(self, ctx: SQLGrammarParser.TypeContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#value.
    def enterValue(self, ctx: SQLGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#value.
    def exitValue(self, ctx: SQLGrammarParser.ValueContext):
        pass


del SQLGrammarParser