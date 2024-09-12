age = int(input("Enter your age - "))

if age < 0:
    print("Age must non negative number")
    exit(1)


if age > 18:
    print("Lets drink beer")
elif age == 18:
    print("You can drink beer")
else:
    print("Drink water please!")