USERNAME = "admin"
PASSWORD = "1234qwer"

MAX_LOGIN_ATTEMPT = 3

print("Please sign in!")
user_signed_in = False

for login_attempt in range(1, MAX_LOGIN_ATTEMPT + 1):
    username_in = input("Please enter username - ")
    password_in = input("Please enter password - ")

    if username_in == USERNAME and password_in == PASSWORD:
        user_signed_in = True
        break
    else:
        print(f"Username or Password is wrong. ({login_attempt}/{MAX_LOGIN_ATTEMPT})")

if user_signed_in:
    print("Welcome to our system!")
else:
    print("Account is blocked for next 24 hours")
