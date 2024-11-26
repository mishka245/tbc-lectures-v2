
d = {"name": "Giorgi", "age": 49}
l = [1,2,3,4]
t = (1,2,3,4)

with open("task_3.txt", "w") as file:
    file.write(str(d))
    file.write("\n")
    file.write(str(l))
    file.write("\n")

    file.write(str(t))

print(d)
print(l)
print(t)