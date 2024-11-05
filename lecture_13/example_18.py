my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append("even")
    else:
        my_list.append("odd")


print(my_list)

my_list = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(my_list)