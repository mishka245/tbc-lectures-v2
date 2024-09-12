age = int(input("Enter your age - "))

if age < 0:
    print("Age must non negative number")
else:
    if age > 18:
        print("Lets drink beer")
    elif age == 18:
        print("You can drink beer")
    else:
        print("Drink water please!")
