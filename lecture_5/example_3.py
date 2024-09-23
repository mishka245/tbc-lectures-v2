from random import randint

left = randint(0, 10)
right = randint(10, 20)
old_left = left

s = 0  # Save sum here

while left < right:
    s += left
    left += 1

print("left", old_left)
print("right", right)

print("sum = ", s)
