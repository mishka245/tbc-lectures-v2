my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#          0,   1,  2,  3
my_list.append(100000)
print(my_list)
my_list.insert(2, -1)
print(my_list)
my_list[3] = -1
print(my_list)

# my_list.remove(0)  #  list.remove(x): x not in list
my_list.remove(60)
print(my_list)

result = my_list.sort()
print(my_list)
print(result)  # Will be None



