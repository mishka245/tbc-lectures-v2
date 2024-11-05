my_list = []
for i in range(10):
    my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(10)]
print(my_list)