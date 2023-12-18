# import database module

# define a funcion called initializing
# import database module

# define a function called initializing

import csv
from database import Table, Database
from admin import Admin
from lead_student import Lead
from member import Member

database = Database()
admin = Admin()


def data_file(file):
    with open(file) as variable:
        data = []
        for new_data in csv.DictReader(variable):
            data.append(new_data)
        return data


def initializing():
    table = Table('persons', data_file('persons.csv'))
    table2 = Table('login', data_file('login.csv'))
    table3 = Table('advisor', data_file('Advisor_pending_request.csv'))
    table4 = Table('member', data_file('Member_pending_request.csv'))
    table5 = Table('project', data_file('Project_table.csv'))


    database.insert(table)
    database.insert(table2)
    database.insert(table3)
    database.insert(table4)
    database.insert(table5)


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

if val[1] == 'admin':
    admin.update(database)
    admin.new_data()

    # see and do admin related activities
elif val[1] == 'student':

    pass
#     # see and do student related activities
elif val[1] == 'member':
    member = Member(
        val[0],
        database.find_table("project"),
        database.find_table('member'),
        database.find_table('persons'),
    )
    member.show_choice()

     # see and do member related activities
elif val[1] == 'lead':
    lead = Lead(val[0], database)
    lead.find_member()
    lead.show_function()
    lead.create_project()
    lead.show_member()
    lead.sent_invitation()


#     see and do lead related activities
# elif val[1] == 'faculty':
#     see and do faculty related activities
# elif val[1] == 'advisor':
#     see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit('output_file')
