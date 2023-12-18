"""Module for managing the project management system."""
import csv
from database import Table, Database
from admin import Admin
from lead_student import Lead
from member import Member
from student import Student

database = Database()
admin = Admin()


def data_file(file):
    """Read in the csv files and transform it into a list of dictionaries."""
    with open(file, mode='r', encoding='utf-8') as variable:
        data = []
        for new_data in csv.DictReader(variable):
            data.append(new_data)
        return data


def initializing():
    """Read in the csv files and create tables for each of them."""
    table = Table("persons", data_file("persons.csv"))
    table2 = Table("login", data_file("login.csv"))
    table3 = Table("advisor_pending", data_file("advisor_pending.csv"))
    table4 = Table("member_pending", data_file("member_pending.csv"))
    table5 = Table("project", data_file("project.csv"))

    database.insert(table)
    database.insert(table2)
    database.insert(table3)
    database.insert(table4)
    database.insert(table5)


def login():
    """Ask the user to enter username and password."""
    user_name = input("Enter user name: ")
    password = input("Enter password: ")
    for name in data_file("login.csv"):
        if user_name in name.values() and password in name.values():
            return [name["ID"], name["role"]]
    return None


def exits():
    """write out all the tables that have been modified to the csv files."""
    for table in database.database:
        with open(f"{table.table_name}.csv", mode="w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(table.rows[0].keys())
            for row in table.rows:
                csv_writer.writerow(row.values())


initializing()
val = login()

if val[1] == "admin":
    admin.update(database)
    admin.new_data()

elif val[1] == "student":
    student = Student(val[0], database)
    student.show_student_function()

elif val[1] == "member":
    member = Member(
        val[0],
        database.find_table("project"),
        database.find_table("member"),
        database.find_table("persons"),
    )
    member.show_choice()

elif val[1] == "lead":
    lead = Lead(val[0], database)
    lead.show_function()

elif val[1] == 'faculty':
    pass
elif val[1] == 'advisor':
    pass

exits()
