s = "azcbobobegghbob"

numbobs = 0
for i in range(len(s) - 2):
    if s[i:i + 3] == "bob":
        numbobs += 1

print(numbobs)
