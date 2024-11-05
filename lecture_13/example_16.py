my_list = []
for i in range(10):
    if i % 2 != 0:
        my_list.append(i ** 2)

print(my_list)

# my_list = [10 / x for x in range(10) if x != 0]
#         |  III  |        I       |      II      |
my_list = [x ** 2 for x in range(10) if x % 2 != 1]
print(my_list)