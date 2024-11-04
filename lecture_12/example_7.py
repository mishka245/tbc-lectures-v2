s = "Python"

result = ""

for i in s:
    if i != "o":
        print(id(result))
        result = result + i

print(result)