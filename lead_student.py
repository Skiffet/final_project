from database import Table, Database
class Lead:
    def __init__(self, id, database):
        self.projects = []
        self.id = id
        self.project_table: Table = database.find_table("project")
        self.member_table: Table = database.find_table("person")

    def show_function(self):
        while True:
            try:
                print("1. Create project")
                print("2. Find member")
                print("3. Send invitation to person")
                print("4. Add member to project")
                print("5. Add advisor to project")
                print("6. Submit project")
                print("7. Exit")
                select = int(input("Select : "))
                if not isinstance(select, int):
                    print("Please enter a valid answer.")
                if select == 1:
                    self.create_project()
                elif select == 2:
                    self.show_member()
                elif select == 3:
                    self.sent_invitation()
                elif select == 4:
                    self.add_member()
                elif select == 5:
                    self.add_advisor()
                elif select == 6:

                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")


    def create_project(self):
        project = {"ID": "PRJ200" + str(len(self.projects) + 1)
            , "Title": input("Enter Title: ")
            , "Lead": self.id
            , "Member1": input("Enter Member1: ")
            , "Member2": input("Enter Member2: ")
            , "Advisor": input("Enter Advisor: ")
            , "Status": "Pending"
        }

        self.project_table.insert(project)
        self.projects.append(project)
        return f"Project {project['ID']} created successfully."


    def find_member(self): # หาชื่อของ lead
        for member in self.member_table.rows:
            if self.id == member['ID']:
                return member['first'] + ' ' + member['last']

    def show_member(self):
        name_lead = self.find_member()
        for member in self.member_table.rows:
            if name_lead in member.values():
               if member['Lead'] == name_lead:
                print(f"Project ID: {member['ID']} Member1: {member['Member1']} "
                      f"Member2: {member['Member2']}")


    def id_project(self): # หา id ของ project
        for member in self.member_table.rows:
            if self.id == member['Lead']:
                return member["ID"]


    def sent_invitation(self):
        global project
        id_project = self.id_project()
        for project in self.project_table.rows:
            if id_project == project['ID']:
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
        while True:
            try:
                id_project = input("Enter ID Project: ")
                if id_project not in project.values():
                    print("Please enter a valid answer.")
                else:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")
        for project in self.project_table.rows:
            if id_project == project['ID']:
                project['Status'] = "Pending"
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
                print("Invitation sent successfully.")
                print(" ")


    def add_member(self):
        global project
        id_project = self.id_project()
        for project in self.project_table.rows:
            if id_project == project['ID']:
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
        while True:
            try:
                id_project = input("Enter ID Project: ")
                if id_project not in project.values():
                    print("Please enter a valid answer.")
                else:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")
        for project in self.project_table.rows:
            if id_project == project['ID']:
                project['Status'] = "Approved"
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
                print("Member added successfully.")
                print(" ")


    def add_advisor(self):
        global project
        id_project = self.id_project()
        for project in self.project_table.rows:
            if id_project == project['ID']:
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
        while True:
            try:
                id_project = input("Enter ID Project: ")
                if id_project not in project.values():
                    print("Please enter a valid answer.")
                else:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")
        for project in self.project_table.rows:
            if id_project == project['ID']:
                project['Status'] = "Approved"
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
                print("Advisor added successfully.")
                print(" ")

    # def submit_project(self):
    #    while True:
    #        Y = input("Do you want to submit project? (Y)es \ (N)o: ").upper()
    #             if Y == "Y":
    #                 pass

























