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
            self.rows = []  # contains arrays of same size, each with same number of tuples

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
        for name in ctx.NAME():
            table_column_names.append(name)

        table_name = table_column_names[0]  # working fine

        '''
        3 cases: 
        1. SELECT col1, col2, ...
        2. SELECT * ... ==> if len(column_names) == 1 and 
        3. SELECT col1, col2 FROM table_name WHERE col1=value
        '''

        print(">Select query for", table_name) # working

        # got the table name
        # Now, want the column names from the select query
        column_names = []
        if ctx.columns().NAME():
            for name in ctx.columns().NAME():
                col_name = name.getText()
                column_names.append(col_name)
        else:
            column_names.append("*")

        '''
        for name in ctx.columns().NAME():
            col_name = name.getText()
            column_names.append(col_name)
        '''

        # print the column names in the query
        x = "\t".join([column for column in column_names])
        print(x) # column names being printed

        # need to get the data for these column_names
        table_object = self.tables[table_name.getText()]

        # find the tuple indices of the column names given in the colDefs array
        # so, we can use that indices tho print specific tuple in the arrays of self.rows

        '''
        Case #1  SELECT col1, col2, ...
        This means that the column_names is not size=1 (i.e., it's not just a star), 
        AND the table_column_names is size=1 (i.e., there is not a WHERE clause at the end)
        '''
        if len(table_column_names) == 1 and len(column_names) != 1:
            col_indices = []
            index_1 = 0
            index_2 = 0
            for (c_name, c_type) in table_object.colDefs:
                if index_2 < len(column_names) and c_name == column_names[index_2]:
                    col_indices.append(index_1)
                    index_1 += 1
                    index_2 += 1
                else:
                    index_1 += 1
                    index_2 += 1

            # use the indices in col_indices to access specific tuple in arrays of self.rows
            for row in table_object.rows:
                x = ""
                for index in col_indices:
                    x += row[index] + '\t'
                print(x)   # specific row data print working

        elif len(table_column_names) == 1 and len(column_names) == 1 : # just a STAR as a column selection
            '''
            Case #2 ==> SELECT * ...
            just print the whole table for this one
            '''
            print(table_object)

        else:
            '''
            Case #3 ==> SELECT col1, col2, FROM table_name WHERE ...
            just print the whole table for this one
            '''
            print("WHERE clause in the query")
            # filter out the rows where the selected the columns have the data
            # To do:
            # 1. get the index=1's value in table_column_names ==> that's the column name for which
            # WHERE clause is getting applied
            # 2. get the index of the column from colDefs
            # 3. then use the index from step 2 in each row of self.rows to check if the values is matching

            # step 1
            filter_column_name = table_column_names[1]
            print("filter_column_name:", filter_column_name)


            target_index = 0
            for (c_name, c_type) in table_object.colDefs:
                if c_name == filter_column_name:
                    break
                else:
                    target_index += 1

            print(target_index)


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