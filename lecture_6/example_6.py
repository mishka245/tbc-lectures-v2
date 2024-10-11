a = 27
possible_root = 0

while possible_root * possible_root * possible_root != a:
    possible_root += 1


print("root", possible_root)