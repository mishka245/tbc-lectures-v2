import random

a = random.randint(0, 10)  # 8
b = random.randint(0, 10)  # 2

print("a", a)
print("b", b)

s = 0

if a > b:
    for i in range(b, a):
        s += i
else:
    for i in range(a, b):
        s += i

print("Sum", s)
