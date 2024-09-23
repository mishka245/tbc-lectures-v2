from random import randint

count = 1
found = False

while count < 10 and found == False:
    r = randint(0, 1000)
    if r % 17 == 0:  # False
        print(f"17-ის ჯერადი რიცხვია : {r}, ცდების რაოდენობა - {count}")
        found = True
    count += 1

if not found:
    print("Can not find a number in 10 iterations")