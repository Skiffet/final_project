from database import Table, Database
class student:
    def __init__(self,id, database):
        self.project_table: Table = database.find_table("project")
        self.member_table: Table = database.find_table("person")
        self.id = id


    def show_student_function(self):
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


    def find_member(self): # หาชื่อของ lead
        for member in self.member_table.rows:
            if self.id == member['ID']:
                return member['first'] + ' ' + member['last']

    def id_project(self): # หา id ของ project
        for member in self.member_table.rows:
            if self.id == member['Lead']:
                return member["ID"]

    def show_invitation(self):
        pass

    def accept_invitation(self):
        pass


