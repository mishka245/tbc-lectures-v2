import random

try:
    1 / random.choice([0, 1])
except Exception  as ex:
    print("Error: ", ex)
else:
    print("whoala")
    print("whoala")

print("Done")