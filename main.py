print("""
Available actions:
      _ register
      _ login
      """)

action =input("What do you want to do?: ")

if action == "register":
    print("\nOk. Let's register you in the system.")

    name = input("What's your name?: ")
    last_names = input("What are your last names?: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

elif action == "login":
    print("Okay!! Log in to the system")
    email = input("Enter your email: ")
    password = input("Enter your password: ")