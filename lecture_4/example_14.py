import random

a = random.randint(0, 10)  # 8
b = random.randint(0, 10)  # 2


if a > b:
    # swap places for two variables
    a, b = b, a

s = 0
for i in range(a, b):
    s += i

print("left", a)
print("right", b)
print("Sum", s)