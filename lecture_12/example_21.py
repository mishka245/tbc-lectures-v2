a = [5, 6, 7, 100, 5, 52, -1, 5]

print(a)
# sorted(a)  # sorted is not inplace function, returns new object
a.sort()  # .sort is inplace function, changes object data
print(a)
