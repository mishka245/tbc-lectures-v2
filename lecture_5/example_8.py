"""
დაწერეთ პროგრამა რომელიც დააგენერირებს რიცხვებს 0 დან 1000,
და პირველივე 17 ის ჯერადის პოვნის შემდეგ შეწყვეტს მუშაობას

პროგრამამ უნდა დაბეჭდოს ნაპოვნი 17 ის ჯერადი რიცხვი და ცდების რაოდენობა

"""
from random import randint

count = 1

while True:
    r = randint(0, 1000)
    if r % 17 == 0:
        print(f"17-ის ჯერადი რიცხვია : {r}, ცდების რაოდენობა - {count}")
        break
    count += 1