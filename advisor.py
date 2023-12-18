from database import Table, Database
class advisor:
    def __init__(self, id, database):
        self.person_table = None
        self.id = id
        self.project_table: Table = database.find_table("project")
        self.member_table: Table = database.find_table("person")


    def advisor_function(self):
        while True:
            try:
                print("1. See request to advisor")
                print("2. Sent accept response to member")
                print("3. Exit")
                select = int(input("Select : "))
                if not isinstance(select, int):
                    print("Please enter a valid answer.")
                if select == 1:
                    self.show_request()
                elif select == 2:
                    self.sent_accept_response()
                elif select == 3:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")


    def convert_to_name(self):
        for person in self.person_table.rows:
            if person["ID"] == self.id:
                return person["first"] + ' ' + person["last"]

    def show_request(self):
        name = self.convert_to_name()
        for project in self.project_table.rows:
            if name in project.values():
                print(f"Project ID: {project['ID']}, {project['Title']}, Status: {project['Status']}")

    def sent_accept_response(self):
        my_project = []
        name = self.convert_to_name()
        for project in self.project_table.rows:
            if name in project.values():
                my_project.append(project["ID"])

        for project in self.project_table.rows:
            if project["ID"] in my_project:
                print(f"Leader: {project['Lead']}, Title: {project['Title']}, Status: {project['Status']}")
