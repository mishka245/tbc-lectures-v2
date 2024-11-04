import random

numbers = []

for _ in range(20):
    numbers.append(random.randint(1, 1000))


even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Numbers", numbers)

print("Even numbers", even_numbers)
print("Odd numbers", odd_numbers)