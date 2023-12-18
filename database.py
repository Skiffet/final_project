# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
print(persons)

# add in code for a Database class

# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated


class Database:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def find_table(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

import copy


class Table:
    def __init__(self, table_name, rows):
        self.table_name = table_name
        self.rows = rows
        # self.rows = [Row(row_data) for row_data in rows]

    # def join(self, other_table, common_key):
    #     joined_table = Table(
    #         f"{self.table_name}_joins_{other_table.table_name}", [])
    #     for row1 in self.rows:
    #         for row2 in other_table.rows:
    #             if getattr(row1, common_key) == getattr(row2, common_key):
    #                 joined_row = Row({**row1.data, **row2.data})
    #                 joined_table.rows.append(joined_row)
    #     return joined_table

    # def filter(self, condition):
    #     filtered_table = Table(f"{self.table_name}_filtered", [])
    #     for row in self.rows:
    #         if condition(row.data):
    #             filtered_table.rows.append(row)
    #     return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = [float(getattr(row, aggregation_key)) for row in self.rows]
        return function(temps)

    # def select(self, attributes_list):
    #     selected_rows = [Row({key: getattr(row, key) for key in attributes_list}) for row in self.rows]
    #     return selected_rows

    # def insert(self, data):
    #     new_row = Row(data)
    #     self.rows.append(new_row)

    def update(self, row_id, column, value):
        for row in self.rows:
            if row["ID"] == row_id:
                row[column] = value
                break
        # for row in self.rows:
        #     print(row)

    def __str__(self):
        return f"{self.table_name}:{[str(row) for row in self.rows]}"

    def insert(self, project):
        self.rows.append(project)

# class Row:
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return str(self.data)









