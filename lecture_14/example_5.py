my_tuple = (1,2,3,4)

a, _, _, d = my_tuple
print(a, d)

a, b = my_tuple[0], my_tuple[-1]

print(*my_tuple, sep="--")
