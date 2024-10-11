a = 27
possible_root = 0


for possible_root in range(0, a):
    if possible_root ** 3 == a:
        print("root", possible_root)
        break
else:
    print("Could not find results")


