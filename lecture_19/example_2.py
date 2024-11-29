number = input("Enter number please - ")

try:
    number = int(number)
    print(number)
except Exception as e:
    print("User in put is invalid. Cant be converted into int. Error: ", str(e))

print("Important message must be print")

