from lecture_16.admin import admin_loop
from lecture_16.common import process_user_input


def list_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. my tickets")
    print("4. admin")
    return process_user_input()

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                print("Listing sessions")
            case "2":
                print("Searching movie")
            case "3":
                print("Listing tickets")
            case "4":
                admin_loop()
            case _:
                print("Invalid input")

def main():
    greetings()
    program_loop()


if __name__ == "__main__":
    main()
