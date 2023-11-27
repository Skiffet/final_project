# import database module

# define a funcion called initializing
# import database module

# define a function called initializing

import csv
from database import Table, Database

database = Database()


def data_file(file):
    with open(file) as variable:
        data = []
        for new_data in csv.DictReader(variable):
            data.append(new_data)
        return data


def initializing():
    table = Table('persons', data_file('persons.csv'))
    table2 = Table('login', data_file('login.csv'))
    database.insert(table)
    database.insert(table2)


def login():
    user_name = input("Enter user name: ")
    password = input("Enter password: ")
    for name in data_file('login.csv'):
        if user_name in name.values() and password in name.values():
            return [name['ID'], name['role']]
    return None


def exit(output_file):
    table_name = 'person'  # Replace with the actual table name
    table = database.find_table(table_name)
    if table:
        with open(output_file, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(table.table[0].keys())
            for row in table.table:
                csv_writer.writerow(row.values())




# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit('output_file')
