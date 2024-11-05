my_list = []
t = ["even", "odd"]
for i in range(10):
    my_list.append(t[i%2])


print(my_list)

my_list = [t[x%2] for x in range(10)]
print(my_list)