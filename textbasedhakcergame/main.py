import time
class text_based_jacer_game:
    def __init__(self):
        self.components = ["laptop", "android phone"]
        self.users = []
        self.money = 0
        self.tasks = ["hack fb id", "hack nasa", "hack insta id", "hack bank id", "hack google", "hack apple"]
    
    def login(self):
        self.usr_name = input("Enter your username: ")
        self.passwd = input("Enter your password: ")

    def main_menu(self):
        while True:
            usr_chs = int(input("1.View Tasks\n2.Complete task\n3.View Components\n4.Check balance\n5.Exit\nEter your choice: "))

            if usr_chs == 1:
                self.view_tasks()
            elif usr_chs == 2:
                self.comp_tasks()
            elif usr_chs == 3:
                self.view_components()
            elif usr_chs == 4:
                self.check_bal()
            elif usr_chs == 5:
                print("BYBYBYBYBBYBYBBYBBYYB")
                break
            else:
                print("Try again!!!!!!!!!!!")
                continue
        
    def view_tasks(self):
        print(f"Tasks: {self.tasks}")
    def comp_tasks(self):
        print(self.tasks)
        self.chs_taks = int(input("Which task you want to complete 0-5: "))

        if self.chs_taks == 0:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
        if self.chs_taks == 1:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
        if self.chs_taks == 2:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
        if self.chs_taks == 3:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
        if self.chs_taks == 4:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
        if self.chs_taks == 5:
            print("Type this 'sudo hack/collect--data'")
            usr_command = input(": ")
            if usr_command == "sudo hack/collect--data":
                print("Hacking in process...")
                time.sleep(10)
                print("hacking completed")
                self.money += 50
    def view_components(self):
        print(f"Your Components: {self.components}")
    def check_bal(self):
        print(f"Your balance: {self.money}")

if __name__ == "__main__":
    app = text_based_jacer_game()
    app.login()
    app.main_menu()