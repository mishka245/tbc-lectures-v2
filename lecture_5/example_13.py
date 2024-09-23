import random

NUMBER_COUNT = 100

for i in range(NUMBER_COUNT):
    r = random.randint(0, 1000)
    if r % 2 == 0:
        continue
    print(r)
