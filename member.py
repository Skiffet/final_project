from database import Table, Database


class Member:
    def __init__(self, id, project_table, member_response_table, person_table):
        self.id = id
        self.project_table = project_table
        self.member_response_table = member_response_table
        self.person_table = person_table

    def show_choice(self):
        while True:
            try:
                print("1. Show Project")
                print("2. Show Response Request")
                print("3. Exit")
                select = int(input("Select : "))
                if not isinstance(select, int):
                    print("Please enter a valid answer.")
                if select == 1:
                    self.show_project()
                elif select == 2:
                    self.show_response_request()
                elif select == 3:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")

    def convert_to_name(self):
        for person in self.person_table.rows:
            if person["ID"] == self.id:
                return person["first"] + ' ' + person["last"]

    def show_project(self):
        name = self.convert_to_name()
        for project in self.project_table.rows:
            if name in project.values():
                print(f"Project ID: {project['ID']}, {project['Title']}, Status: {project['Status']}")

    def show_response_request(self):
        my_project = []
        name = self.convert_to_name()
        for project in self.project_table.rows:
            if name in project.values():
                my_project.append(project["ID"])

        for project in self.project_table.rows:
            if project["ID"] in my_project:
                print(f"Leader: {project['Lead']}, Title: {project['Title']}, Status: {project['Status']}")