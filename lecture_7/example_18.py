# noinspection SpellCheckingInspection
"""
პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანa შემდეგ გამოიმუშავოს შემთხვევითი რიცხვი 0-დან 8-ის ჩათვლით
თუ გამოიმუშავებს:
0  დათვალოს "a" სიმბოლოების რაოდენობა შეყვანილ სტრიქონში
1 დაბეჭდოს "b სიმბოლოს ინდექსი
2 ‘c’ სიმბოლო შეცვალოს ‘*’-ით
3 ყველა სიმბოლო გადაიყვანოს ზედა რეგისტრში
4 ყველა სიმბოლო გადაიყვანოს ქვედა რეგისტრში
5 გაადიდოს პირველი სიმბოლი
6 გადაიყვანოს ქვედა რეგისტრის სიმბოლოები ზედაში და პირიქით
7-შეამოწმოს არის თუ არა სტრიქონში ‘d’ სიმბოლო
8-წაშალოს  ყველა e სიმბოლო
"""
import random

text = input("please enter your text - ")
number = random.randint(0, 8)

print("Number -> ", number)

if number == 0:
    print(text.count("a"))
elif number == 1:
    print(text.find("b"))
elif number == 2:
    print(text.replace("c", "*"))
elif number == 3:
    print(text.upper())
elif number == 4:
    print(text.lower())
elif number == 5:
    print(text.capitalize())
elif number == 6:
    print(text.swapcase())
elif number == 7:
    print("d" in text)
else:
    print(text.replace("e", ""))