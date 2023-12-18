"""This module is used to create a lead student."""
from datetime import datetime


class Lead:
    """Class representing a lead student."""

    def __init__(self, lead_id, database):
        """Initialize the lead."""
        self.id = lead_id
        self.project_table = database.find_table("project")
        self.member_table = database.find_table("member_pending")
        self.persons_table = database.find_table("persons")
        self.advisor_pending_table = database.find_table("advisor_pending")
        self.login_table = database.find_table("login")

    def show_function(self):
        """Show the lead function."""
        while True:
            try:
                print("1. Create project")
                print("2. Find member")
                print("3. Send invitation to person")
                print("4. Add member to project")
                print("5. Add advisor to project")
                print("6. Submit project")
                print("7. See message project status")
                print("8. Change Project Status")
                print("9. Exit")
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
                    self.submit_project()
                elif select == 7:
                    self.message_response_status()
                elif select == 8:
                    self.change_project_status()
                elif select == 9:
                    break
            except ValueError:
                print("Please enter a number.")
                print(" ")

    def create_project(self):
        """Create project for lead."""
        project = {
            "ID": "PRJ200" + str(len(self.project_table.rows) + 1),
            "Title": input("Enter Title: "),
            "Lead": self.find_leader_name(),
            "Member1": '',
            "Member2": '',
            "Advisor": '',
            "Status": "Pending",
        }

        self.project_table.insert(project)
        print(f"Project {project['ID']} created successfully.")

    def find_leader_name(self):
        """Find the name of the leader."""
        for member in self.persons_table.rows:
            if self.id == member["ID"]:
                return member["first"] + " " + member["last"]

        return None

    def show_member(self):
        """Show the member."""
        name_lead = self.find_leader_name()
        print(name_lead)
        for project in self.project_table.rows:
            if project["Lead"] == name_lead:
                print(
                    f"Project ID: {project['ID']} "
                    f"Member1: {project['Member1']} "
                    f"Member2: {project['Member2']}"
                )
        print('')

    def id_project(self):
        """Find the ID of the project."""
        lead = ""
        for name in self.persons_table.rows:
            if self.id == name["ID"]:
                lead = name["first"] + " " + name["last"]

        for member in self.project_table.rows:
            if lead == member["Lead"]:
                return member["ID"]
        return None

    def sent_invitation(self):
        """Sent invitation to person."""
        id_project = self.id_project()
        for project in self.project_table.rows:
            if id_project == project["ID"]:
                print(
                    f"Project ID: {project['ID']} Title: {project['Title']} "
                    f"Status: {project['Status']}"
                )
        while True:
            student_id = input("Enter Student ID: ")
            found = self.persons_table.filter(
                lambda row: row["ID"] == student_id)

            if found.rows:
                self.member_table.insert(
                    {
                        "ID": id_project,
                        "to_be_member": found.rows[0]["first"]
                        + " " + found.rows[0]["last"],
                        "Response": "Pending",
                        "Response_date": datetime.today().date()
                    }
                )
                print(f'The message has been sent to the student ID {student_id}.')
                break
            print("Please enter a valid Student ID and not have a project.")

    def add_member(self):
        """Add member to project."""
        id_project = self.id_project()
        join = self.member_table.join(self.project_table, "ID", "ID")
        print(join.rows)
        not_found = True
        for i in join.rows:
            if id_project == i["ID"] and i["Response"] == "Approved":
                print(f"Do you want to add {i['to_be_member']} to project?")
                select = input("Enter (Y)es or (N)o: ").upper()
                while True:
                    if select == "Y":
                        if i["Member1"] == "":
                            self.project_table.update(id_project, "Member1", i["to_be_member"])
                            not_found = False
                            self.login_table.update(
                                i["to_be_member"], "role", "member")
                        elif i["Member2"] == "":
                            self.project_table.update(id_project, "Member2", i["to_be_member"])
                            not_found = False
                            self.login_table.update(
                                i["to_be_member"], "role", "member")
                        else:
                            print("Project is full.")
                        break
                    if select == "N":
                        print("You denied the request.")
                        break
                    print("Please enter a valid answer.")
        if not_found:
            print("No have student response.")
        print('')

    def add_advisor(self):
        """Add advisor to project."""
        join = self.advisor_pending_table.join(self.project_table, "ID", "ID")
        id_project = self.id_project()
        not_found = True
        for i in join.rows:
            if id_project == i["ID"] and i["Response"] == "Approved":
                print(f"Do you want to add {i['to_be_advisor']} to project?")
                select = input("Enter (Y)es or (N)o: ").upper()
                while True:
                    if select == "Y":
                        if i["Advisor"] == "":
                            self.project_table.update(id_project, "Advisor",
                                                      i["to_be_advisor"])
                            not_found = False
                            self.login_table.update(
                                i["to_be_advisor"], "role", "advisor"
                            )
                        else:
                            print("Project is full.")
                            not_found = False
                        break
                    if select == "N":
                        print("You denied the request.")
                        break
                    print("Please enter a valid answer.")
        if not_found:
            print("No have advisor response.")
        print('')

    def submit_project(self):
        """Submit project."""
        id_project = self.id_project()
        not_found = True
        for project in self.project_table.rows:
            if id_project == project["ID"] and project["Status"] == "Completed":
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
                not_found = False
        if not_found:
            print("No have project completed yet.")
            print('')
            return
        while True:
            select = input("Do you want to submit project? (Y/N): ").upper()
            if select == "Y":
                self.project_table.update(id_project, "Status", "Submitted")
                print("Project submitted.")
                break
            if select == "N":
                print("You project status is still not submitted.")
                break
            print("Please enter a valid answer.")
        print('')

    def message_response_status(self):
        """See message project status."""
        id_project = self.id_project()
        print("---Project Response Member---")
        for status in self.member_table.rows:
            if id_project == status["ID"]:
                print(f"Project ID: {status['ID']} "
                      f"Send to {status['to_be_member']} "
                      f"Status: {status['Response']} {status['Response_date']}")
        print("---Project Response Advisor---")
        for status in self.advisor_pending_table.rows:
            if id_project == status["ID"]:
                print(f"Project ID: {status['ID']} "
                      f"Send to {status['to_be_advisor']} "
                      f"Status: {status['Response']} {status['Response_date']}")
        print('')

    def change_project_status(self):
        """Change Project Status."""
        id_project = self.id_project()
        not_found = True
        for project in self.project_table.rows:
            if id_project == project["ID"]:
                print(f"Project ID: {project['ID']} Title: {project['Title']} "
                      f"Status: {project['Status']}")
                not_found = False
        if not_found:
            print("No have project.")
            print('')
            return
        while True:
            select = input("Do you want to change project status? (Y/N): ").upper()
            if select == "Y":
                self.project_table.update(id_project, "Status", "Completed")
                print("Project status changed.")
                break
            if select == "N":
                print("You project status is still not change.")
                break

            print("Please enter a valid answer.")
        print('')
