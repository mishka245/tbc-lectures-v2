def process_user_input():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "3", "4", "exit"]:
        print("Invalid input")
        return process_user_input()
    if user_input == "exit":
        print("Goodbye")
        exit()
    return user_input
