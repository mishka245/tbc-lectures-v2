from random import randint

left = randint(0, 10)
right = randint(10, 20)

s = "hello" + " " + "world"
print(s)

s = "Left = " + str(left) + ", Right = " + str(right) + ", sum = " + str(left + right) + "."
print(s)

s = f"Left = {left}, Right = {right}, sum = {left + right}."
print(s)

