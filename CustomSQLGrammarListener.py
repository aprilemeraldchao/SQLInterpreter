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
            self.colDefs = cols  # array filled with tuples, which are of size=2 (colName, colType)
            self.rows = []  # contains arrays of same size, each with same number of elements

        def insert(self, values):
            self.rows.append(values)
            # values = an array of tuples, which are of size=1, representing each column value

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
            colType = "string" if colDef.data_type().STRING() else "int"
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
        print("\n>Showing tables")
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
        # print("\nEntered SELECT\n")

        # working fine
        table_column_names = [] # this'd stores the column names for case 3 as well
        # this array will always have 2 items: 1. table_name, 2. filter_column
        for name in ctx.NAME():
            table_column_names.append(name)

        table_name = table_column_names[0]  # working fine

        '''
        3 cases: 
        1. SELECT col1, col2, ...
        2. SELECT * ... ==> if len(query_column_names) == 1 and 
        3. SELECT col1, col2 FROM table_name WHERE col1=value
        '''

        print(">Select query for", table_name) # working

        # got the table name
        # Now, want the column names from the select query
        query_column_names = []
        if ctx.columns().NAME():
            for name in ctx.columns().NAME():
                col_name = name.getText()
                query_column_names.append(col_name)
        else:
            query_column_names.append(ctx.columns().STAR().getText())
            # query_column_names.append("*")

        '''
        for name in ctx.columns().NAME():
            col_name = name.getText()
            query_column_names.append(col_name)
        '''

        # print the column names in the query
        x = "\t".join([column for column in query_column_names])
        print(x) # column names being printed

        # need to get the data for these query_column_names
        table_object = self.tables[table_name.getText()]

        # find the tuple indices of the column names given in the colDefs array
        # so, we can use that indices tho print specific tuple in the arrays of self.rows

        '''
        Case #1  SELECT col1, col2, ...
        This means that the query_column_names is not size=1 (i.e., it's not just a star), 
        AND the table_column_names is size=1 (i.e., there is not a WHERE clause at the end)
        '''

        col_indices = []
        where_index = None

        query_col_index = 0
        for table_col_index, (c_name, c_type) in enumerate(table_object.colDefs):
            if query_column_names[0] == '*' or (query_col_index < len(query_column_names) and c_name == query_column_names[query_col_index]):
                col_indices.append(table_col_index)
                query_col_index += 1

            if len(table_column_names) > 1 and c_name == table_column_names[1].getText():
                where_index = table_col_index


        # use the indices in col_indices to access specific tuple in arrays of self.rows
        for row in table_object.rows:
            # check if there's a where clause, then check if where clause is true
            if len(table_column_names) > 1:
                if ctx.value().STRING_VALUE():
                    value = ctx.value().STRING_VALUE().getText()
                else:
                    value = ctx.value().INT_VALUE().getText()

                if row[where_index] != value:
                    continue

            x = ""
            for index in col_indices:
                x += row[index] + '\t'
            print(x)   # specific row data print working





        print()





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

    # Enter a parse tree produced by SQLGrammarParser#data_type.
    def enterData_type(self, ctx: SQLGrammarParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#data_type.
    def exitData_type(self, ctx: SQLGrammarParser.Data_typeContext):
        pass

    # Enter a parse tree produced by SQLGrammarParser#value.
    def enterValue(self, ctx: SQLGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#value.
    def exitValue(self, ctx: SQLGrammarParser.ValueContext):
        pass


del SQLGrammarParser