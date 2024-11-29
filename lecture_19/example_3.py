number = input("Enter number please - ")

try:
    number = int(number)
    print(number)
except Exception as e:
    print(str(e))

print("Important message must be print")

