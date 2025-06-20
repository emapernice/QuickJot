import users.user as model

class Actions:

    def register(self):
        print("\nOk. Let's register you in the system.")
        name = input("What's your name?: ")
        last_names = input("What are your last names?: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = model.User(name, last_names, email, password)
        register = user.register()

        if register[0] >= 1:
            print(f"\nPerfect {register[1].name} you registered with the email {register[1].email}")

        else:
            print("\nYou did not register correctly!!")

    def login(self):
        print("\nOkay!! Log in to the system")

        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")    

            user = model.User('', '', email, password)
            login = user.login()

            if email == login[3]:
                print(f"\nWelcome {login[1]}, you registered on the system on {login[5]}")
                self.nextActions(login)

        except Exception as e:
            # print(type(e))   
            # print(type(e).__name__)
            print(f"Login incorrecto!! Intente mas tarde")     

    def nextActions(self, user):
        print("""
        Available Actions:
        - Create note (create)
        - Show your notes (show)
        - Delete note (delete) 
        - Exit (exit)                       
              """)
        
        action = input("What do you want to do?: ")

        if action == "create":
            print("Let's create")
            self.nextActions(user)

        elif action == "show":
            print("Let's show")
            self.nextActions(user)

        elif action == "delete":
            print("Let's delete")
            self.nextActions(user)

        elif action == "exit":
            print(f"Ok {user[1]}, see you later")
            exit()    
    
        return None        