first_number = float(input("Enter first number, please - "))
second_number = float(input("Enter second number, please - "))

_sum = first_number + second_number

if _sum > 50:
    print("რიცხვები დიდია")
elif _sum < 50:
    print("რიცხვები პატარაა")
else:
    print("რიცხვები საშუალოა")
