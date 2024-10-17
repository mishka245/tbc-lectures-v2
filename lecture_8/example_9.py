user_input = input("Please enter your name and surname - ").strip()
name, surname = user_input.split(" ")


result = name[0].upper() + ". " + surname.capitalize()
print(result)