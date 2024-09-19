import random

left = random.randint(0, 10)
right = random.randint(10, 20)


s = 0
for i in range(left, right):
    s += i

print("left", left)
print("right", right)
print("Sum", s)