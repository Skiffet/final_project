"""Module for student class"""


class Student:
    """Class representing a student."""

    def __init__(self, _id, database):
        """Initialize the student."""
        self.project_table = database.find_table("project")
        self.member_table = database.find_table("member_pending")
        self.id = _id
        self.person_table = database.find_table("persons")
        self.login_table = database.find_table("login")

    def show_student_function(self):
        """Show the student function."""
        while True:
            try:
                print("1. Show invitational message")
                print("2. Create Project")
                print("3. Exit")
                select = int(input("Select : "))
                if not isinstance(select, int):
                    print("Please enter a valid answer.")
                if select == 1:
                    self.show_invitation()
                elif select == 2:
                    self.create_project()
                elif select == 3:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")

    def find_name(self):
        """Find the name of the student."""
        for person in self.person_table.rows:
            if self.id == person['ID']:
                return person['first'] + ' ' + person['last']

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
        """Show the invitation."""
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

    def create_project(self):
        """Create a project."""
        project_name = input("Enter Title: ")
        project = {"ID": f"PRJ20" + str(len(self.project_table.rows) + 1),
                      "Title": project_name,
                     "Lead": self.find_name(),
                     "Member1": "",
                     "Member2": "",
                     "Advisor": "",
                     "Status": "Pending"
                     }
        print(f"Project {project['ID']} {project['Title']} created successfully.")
        self.project_table.insert(project)
        self.login_table.update(self.id, 'role', 'lead')
