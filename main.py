from users import actions

print("""
Available actions:
      _ register
      _ login
      """)

user = actions.Actions()

action =input("What do you want to do?: ")

if action == "register":
    user.register()


elif action == "login":
    user.login()