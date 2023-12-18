"""Module containing the database classes."""


class Database:
    """Class representing a database."""

    def __init__(self):
        """Initialize the database."""
        self.database = []

    def insert(self, table):
        """Insert a table into the database."""
        self.database.append(table)

    def find_table(self, table_name):
        """Find a table in the database by name."""
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


class Table:
    """Class representing a table in the database."""

    def __init__(self, table_name, rows):
        """Initialize the table."""
        self.table_name = table_name
        self.rows = rows

    def filter(self, condition):
        """Filter the table using the given condition."""
        filtered_table = Table(f"{self.table_name}_filtered", [])
        for row in self.rows:
            if condition(row):
                filtered_table.rows.append(row)
        return filtered_table

    def join(self, other_table, my_key, another_key):
        """Join the table with another table using the given key."""
        joined_table = Table(f"{self.table_name}_joined", [])
        for row in self.rows:
            for other_row in other_table.rows:
                if row[my_key] == other_row[another_key]:
                    joined_table.rows.append({**row, **other_row})
        return joined_table

    def aggregate(self, function, aggregation_key):
        """Aggregate the table using the given function."""
        temps = [float(getattr(row, aggregation_key)) for row in self.rows]
        return function(temps)

    def insert(self, data):
        """Insert a row into the table."""
        self.rows.append(data)

    def update(self, row_id, column, value):
        """Update a row in the table."""
        for row in self.rows:
            if row["ID"] == row_id:
                row[column] = value
                break

    def __str__(self):
        """Return a string representation of the table."""
        return f"{self.table_name}:{[str(row) for row in self.rows]}"
