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
            print(f"selected {len(display_rows)} row(s)")

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

    def printError(self, msg):
        print(f"\033[91mRuntime Error: {msg}\033[0m\n")

    # Enter a parse tree produced by SQLGrammarParser#statement.
    def enterStatement(self, ctx: SQLGrammarParser.StatementContext):
        print(f"\033[96m>{ctx.getText()[:-1].strip()}\033[0m")

    # Exit a parse tree produced by SQLGrammarParser#create.
    def exitCreate(self, ctx: SQLGrammarParser.CreateContext):
        # get table name from query
        table_name = ctx.NAME().getText()

        # check if table name already exists
        if table_name in self.tables:
            self.printError(
                f"CREATE failed because table name '{table_name}' already exists"
            )
            return

        # get column definitions from query
        cols = []
        col_names = set()

        for col_def in ctx.column_definition():
            col_name = col_def.NAME().getText()

            # check if column name already exists
            if col_name in col_names:
                self.printError(
                    f"CREATE failed because column name '{col_name}' already used"
                )
                return

            col_type = "string" if col_def.data_type().STRING() else "int"
            cols.append((col_name, col_type))
            col_names.add(col_name)

        # create and add table to tables dictionary
        self.tables[table_name] = self.Table(table_name, cols)

    # Exit a parse tree produced by SQLGrammarParser#drop.
    def exitDrop(self, ctx: SQLGrammarParser.DropContext):
        # get table name from query
        table_name = ctx.NAME().getText()

        # check if table exists
        if table_name not in self.tables:
            self.printError(f"DROP failed because table '{table_name}' doesn't exist")
            return

        # remove table from tables dictionary
        self.tables.pop(table_name)

    # Exit a parse tree produced by SQLGrammarParser#insert.
    def exitInsert(self, ctx: SQLGrammarParser.InsertContext):
        # get table name from query
        table_name = ctx.NAME().getText()

        # check if table exists
        if table_name not in self.tables:
            self.printError(f"INSERT failed because table '{table_name}' doesn't exist")
            return

        # check if number of columns match
        if len(self.tables[table_name].col_defs) != len(ctx.value()):
            self.printError(
                f"INSERT failed because number of columns don't match (table '{table_name}' is expecting {len(self.tables[table_name].col_defs)} columns)"
            )
            return

        # get row values
        row = []
        for i, value in enumerate(ctx.value()):
            # check if column type is correct
            cur_col_def = self.tables[table_name].col_defs[i]
            if (value.STRING_VALUE() and cur_col_def[1] == "string") or (
                value.INT_VALUE() and cur_col_def[1] == "int"
            ):
                # if value type matches column type, add the value to the row
                row.append(
                    value.STRING_VALUE().getText()
                    if value.STRING_VALUE()
                    else value.INT_VALUE().getText()
                )
            else:
                self.printError(
                    f"INSERT failed because table {table_name}'s column '{cur_col_def[0]}' must be of type {cur_col_def[1]}"
                )
                return

        # insert the row into the table
        self.tables[table_name].insert(row)

    # Exit a parse tree produced by SQLGrammarParser#show.
    def exitShow(self, ctx: SQLGrammarParser.ShowContext):
        if len(self.tables) == 0:
            # if no tables exist yet
            print("No tables\n")

        # else print every table that does exist
        for table in self.tables.values():
            print(table)
            print()

    # Exit a parse tree produced by SQLGrammarParser#select.
    def exitSelect(self, ctx: SQLGrammarParser.SelectContext):
        # this array will always have at most 2 items: 1. table_name, 2. filter_column
        table_column_names = ctx.NAME()

        # get table name from query
        table_name = table_column_names[0].getText()

        # check if table exists
        if table_name not in self.tables:
            self.printError(f"SELECT failed because table '{table_name}' doesn't exist")
            return

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
        table_object = self.tables[table_name]

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

        # check if found all query columns
        if query_col_index < len(query_column_names):
            self.printError(
                f"SELECT failed because table '{table_name}' doesn't have the column '{query_column_names[query_col_index]}'"
            )
            return

        # if the filter index was set
        if filter_index >= 0:
            # check if column type is correct
            filter_col_def = self.tables[table_name].col_defs[filter_index]
            if (ctx.value().STRING_VALUE() and filter_col_def[1] == "string") or (
                ctx.value().INT_VALUE() and filter_col_def[1] == "int"
            ):
                filter_val = (
                    ctx.value().STRING_VALUE().getText()
                    if ctx.value().STRING_VALUE()
                    else ctx.value().INT_VALUE().getText()
                )
            else:
                self.printError(
                    f"SELECT failed because column '{filter_col_def[0]}' (in WHERE clause) must be of type {filter_col_def[1]}"
                )
                return

        # display the filtered table
        table_object.display(col_indices, filter_index, filter_val)
        print()


del SQLGrammarParser