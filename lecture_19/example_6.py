try:
    exit(1)
    number_a = input("Please enter number a - ")
    number_b = input("Please enter number b - ")

    number_a = int(number_a)
    number_b = int(number_b)
    result = number_a / number_b
    print(result)

except ValueError as e:
    print("can not convert into numbers")
except ZeroDivisionError as e:
    print("Can not divide by 0")
except:
    print("Unknown exception occurred")

print("Important message must be print")

