import random

NUMBER_COUNT = 10
i = 0

while i < NUMBER_COUNT:
    i += 1
    r = random.randint(0, 1000)
    if r % 2 == 0:
        continue
    print(r)
