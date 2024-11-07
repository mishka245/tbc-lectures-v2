# string - immutable data structure

# list - mutable data structure
# tuple - immutable data structure

# tuple()
a = (1,2,3,4,5)
b = [1,2,3,4,5]

print(a[1])
print(a[1:3])
# a[1] = -100
# a.append(-100)
print(id(a))
a = a + (-100,)
print(a)
print(id(a))



