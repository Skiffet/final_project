from database import Table


class Admin:

    def __init__(self):
        self.table_data: Table = None

    def update(self, database):
        print("-------UPDATE-------")
        print("1. Advisor")
        print("2. Login.")
        print("3. Member.")
        print("4. Persons.")
        print("5. Project.")
        print("6. Exit.")
        while True:
            try:
                many = int(
                    input("Choose the data to update: "))
                if isinstance(many, int):
                    if many in [1, 2, 3, 4, 5, 6]:
                        break

                    if many < 0:
                        print("Please enter a positive number.")

                    else:
                        print("Please enter a valid number of data.")

            except ValueError:
                print("Please enter a number.")

        if many == 1:
            self.table_data = database.find_table("advisor")

        elif many == 2:
            self.table_data = database.find_table("login")

        elif many == 3:
            self.table_data = database.find_table("member")

        elif many == 4:
            self.table_data = database.find_table("persons")

        elif many == 5:
            self.table_data = database.find_table("project")

        elif many == 6:
            exit()

    def new_data(self):
        while True:
            choice = input("Please enter the topic to update: ")
            if choice in self.table_data.rows[0].keys():
                break

            else:
                print("Please enter a valid topic.")

        while True:
            id = input("Please enter the Project id: ")
            if id in self.table_data.rows[0].values():
                new = input(f"Please enter new {choice}: ")
                self.table_data.update(id, choice, new)

            else:
                print("Please enter a valid Project id.")



























# admin = Admin()
# admin.update()





