import random


a = random.randrange(1, 100)
b = random.randrange(1, 100)

print("a = ", a)
print("b = ", b)

if a > b:
    print("First number is bigger")
elif b > a:
    print("Second number is bigger")
else:
    print("Numbers are equal")

