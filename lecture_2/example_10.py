user = "user"
password = "admin"

input_user = input("Please enter username - ")
input_password = input("Please enter password - ")

if input_user == user and input_password == password:
    print("Welcome!")
elif input_user == user or input_password == password:
    print("Try again")
else:
    print("You are hacker :D")