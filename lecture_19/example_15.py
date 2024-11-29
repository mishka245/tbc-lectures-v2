import random

try:
    1 / random.choice([0, 1])
    print("whoala")
    print("whoala")
except Exception  as ex:
    print("Error: ", ex)

print("Done")