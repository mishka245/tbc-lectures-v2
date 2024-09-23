from random import randint

count = 10

while count > 0:
    r = randint(0, 1000)
    if r % 17 == 0:  # False
        print(f"17-ის ჯერადი რიცხვია : {r}, ცდების რაოდენობა - {10 - count}")
        break
    count -= 1
else:  # else შევდივართ მაშინ და მხოლოდ მაშინ, თუ while ციკლი დასრულდა break ის გარეშე
    print("ვერ ვიპოვეთ")
