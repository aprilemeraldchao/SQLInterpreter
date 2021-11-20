# Generated from SQLGrammar.g4 by ANTLR 4.9
from antlr4 import *
from tabulate import tabulate
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

            # array filled with tuples, which are of size=2 (col_name, col_type)
            self.col_defs = cols

            # contains arrays of same size (the number of columns in this array)
            self.rows = []

        def insert(self, row):
            # row = an array of column values
            self.rows.append(row)

        def display(self, col_indices, filter_index, filter_val):
            # contains all rows that should be displayed
            display_rows = []
            for row in self.rows:
                # skip rows that don't match the where condition
                if filter_index >= 0 and row[filter_index] != filter_val:
                    continue

                # add only the queried columns
                display_rows.append([row[index] for index in col_indices])

            # get column headers
            display_headers = [self.col_defs[index][0] for index in col_indices]

            # print queried columns and rows with tabulate module
            print(
                tabulate(
                    display_rows,
                    headers=display_headers,
                    tablefmt="fancy_grid",
                    numalign="left",
                )
            )

        def __str__(self):
            toStr = "Table: " + self.name + "\n"
            toStr += tabulate(
                [[col_def[1] for col_def in self.col_defs]],
                headers=[col_def[0] for col_def in self.col_defs],
                tablefmt="fancy_grid",
                numalign="left",
            )
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
        print(">", ctx.getText()[:-1])

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
        # get table name from query
        table_name = ctx.NAME().getText()

        # get column definitions from query
        cols = []
        for col_def in ctx.column_definition():
            col_name = col_def.NAME().getText()
            col_type = "string" if col_def.data_type().STRING() else "int"
            cols.append((col_name, col_type))

        # create and add table to tables dictionary
        self.tables[table_name] = self.Table(table_name, cols)

    # Enter a parse tree produced by SQLGrammarParser#drop.
    def enterDrop(self, ctx: SQLGrammarParser.DropContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#drop.
    def exitDrop(self, ctx: SQLGrammarParser.DropContext):
        # get table name from query
        table_name = ctx.NAME().getText()

        # remove table from tables dictionary
        self.tables.pop(table_name)

    # Enter a parse tree produced by SQLGrammarParser#insert.
    def enterInsert(self, ctx: SQLGrammarParser.InsertContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#insert.
    def exitInsert(self, ctx: SQLGrammarParser.InsertContext):
        # get table name from query
        table_name = ctx.NAME().getText()

        # get row values
        row = []
        for value in ctx.value():
            row.append(
                value.STRING_VALUE().getText()
                if value.STRING_VALUE()
                else value.INT_VALUE().getText()
            )

        # insert the row into the table
        self.tables[table_name].insert(row)

    # Enter a parse tree produced by SQLGrammarParser#show.
    def enterShow(self, ctx: SQLGrammarParser.ShowContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#show.
    def exitShow(self, ctx: SQLGrammarParser.ShowContext):
        if len(self.tables) == 0:
            # if no tables exist yet
            print("No tables\n")

        # else print every table that does exist
        for table in self.tables.values():
            print(table)
            print()

    # Enter a parse tree produced by SQLGrammarParser#select.
    def enterSelect(self, ctx: SQLGrammarParser.SelectContext):
        pass

    # Exit a parse tree produced by SQLGrammarParser#select.
    def exitSelect(self, ctx: SQLGrammarParser.SelectContext):
        # this array will always have at most 2 items: 1. table_name, 2. filter_column
        table_column_names = ctx.NAME()

        # get table name from query
        table_name = table_column_names[0]

        # get query column names from query
        query_column_names = []
        if ctx.columns().NAME():
            # if column names were supplied, add those
            for col_name in ctx.columns().NAME():
                query_column_names.append(col_name.getText())
        else:
            # else a '*' was supplied so add that
            query_column_names.append(ctx.columns().STAR().getText())

        # get the table object for this query
        table_object = self.tables[table_name.getText()]

        # initialize variables for displaying the query
        col_indices = []  # indices of the columns to display
        filter_index = -1  # index of the column from the WHERE clause
        filter_val = None  # expected value from the WHERE clause

        # populate the column indices and set the filter index
        query_col_index = 0  # index of the current query column we are looking for in the table's columns

        # loop over all column definitions in the table
        for table_col_index, (c_name, _) in enumerate(table_object.col_defs):
            # if the query is for all columns or we found the query column
            if query_column_names[0] == "*" or (
                query_col_index < len(query_column_names)
                and c_name == query_column_names[query_col_index]
            ):
                # add the index of the column to display
                col_indices.append(table_col_index)

                # increment to the next query column to look for
                query_col_index += 1

            # if we found the column from the WHERE clause, set the filter index
            if (
                len(table_column_names) > 1
                and c_name == table_column_names[1].getText()
            ):
                filter_index = table_col_index

        # if the filter index was set
        if filter_index >= 0:
            # get the expected value
            filter_val = (
                ctx.value().STRING_VALUE().getText()
                if ctx.value().STRING_VALUE()
                else ctx.value().INT_VALUE().getText()
            )

        # display the filtered table
        table_object.display(col_indices, filter_index, filter_val)
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