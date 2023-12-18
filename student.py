"""Module for student class"""
from database import Table, Database


class Student:
    """Class representing a student."""

    def __init__(self, _id, database):
        """Initialize the student."""
        self.project_table = database.find_table("project")
        self.member_table = database.find_table("member_pending")
        self.id = _id
        self.person_table = database.find_table("persons")

    def show_student_function(self):
        """Show the student function."""
        while True:
            try:
                print("1. Show invitational message")
                print("2. Accept invitation")
                print("3. Exit")
                select = int(input("Select : "))
                if not isinstance(select, int):
                    print("Please enter a valid answer.")
                if select == 1:
                    self.show_invitation()
                elif select == 2:
                    self.accept_invitation()
                elif select == 3:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")

    def find_member(self):  # Find Lead Name
        """Find the name of the lead."""
        for member in self.member_table.rows:
            if self.id == member['ID']:
                return member['first'] + ' ' + member['last']

    def id_project(self):  # Find ID of Project
        """Find the ID of the project."""
        for member in self.member_table.rows:
            if self.id == member['Lead']:
                return member["ID"]

    def show_invitation(self):
        my_name = ""
        for p in self.person_table.rows:
            if p['ID'] == self.id:
                my_name = p['first'] + ' ' + p['last']
        no_message = True
        for request in self.member_table.rows:
            if request['to_be_member'] == my_name \
                    and 'Pending' == request['Response']:
                print(f"Project ID: {request['ID']} want you to be a member.")
                no_message = False
                while True:
                    select = input("Would you like to accept? (Y/N): ").upper()
                    if select == "Y":
                        self.member_table.update(request['ID'], 'Response',
                                                 'Approved')
                        print("The message has been sent "
                              "to the project leader.")
                        break
                    elif select == "N":
                        self.member_table.update(request['ID'], 'Response', 'Reject')
                        print("You are not a member of this project.")
                        break
                    else:
                        print("Please enter a valid answer.\n")
        if no_message:
            print("You have no messages.")

    def accept_invitation(self):
        pass


