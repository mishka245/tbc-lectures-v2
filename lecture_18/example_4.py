
file = open("hi.txt", "r")
content = file.read()
print("-" * 100)
print(content)
print("-" * 100)

file.seek(0)
content = file.read()
print("-" * 100)
print(content)
print("-" * 100)

file.close()
