l = list("Python")

result = []  # list is mutable data structure

for i in l:
    if i != "o":
        print(id(result))
        result.append(i)

print(result)