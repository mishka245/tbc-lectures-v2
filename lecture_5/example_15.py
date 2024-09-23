"""
გვაქვს მომხმარებელი და პაროლი განსაზღვრული,

პროგრამამ მომხმარებელს მისცეს საშუალება შემოიყვანოს მომხმარებელი და პაროლი.

3 ჯერ არასწორად ცდის შემთხვევაში დაბლოკოს შესვლა მომდევნო 24 საათით
"""

USERNAME = "admin"
PASSWORD = "1234qwer"

MAX_LOGIN_ATTEMPT = 3

print("Please sign in!")
login_attempt = 0
user_signed_in = False

while login_attempt < MAX_LOGIN_ATTEMPT:
    username_in = input("Please enter username - ")
    password_in = input("Please enter password - ")

    if username_in == USERNAME and password_in == PASSWORD:
        user_signed_in = True
        break
    else:
        login_attempt += 1
        print(f"Username or Password is wrong. ({login_attempt}/{MAX_LOGIN_ATTEMPT})")

if user_signed_in:
    print("Welcome to our system!")
else:
    print("Account is blocked for next 24 hours")
