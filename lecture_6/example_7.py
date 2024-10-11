a = 26
possible_root = 0

# a bit better
while possible_root * possible_root * possible_root < a:
    print(possible_root * possible_root * possible_root)
    possible_root += 1


print("root", possible_root)