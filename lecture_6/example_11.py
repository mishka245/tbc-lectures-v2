a = -27
possible_root = 0

abs_a = abs(a)

while possible_root * possible_root * possible_root != abs_a:
    possible_root += 1


if a < 0:
    possible_root = -1 * possible_root

print("root", possible_root)