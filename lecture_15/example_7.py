names = ['Anna', 'John', 'Denise', 'Katy']
grades = [100, 73, 85, 49]

d_2 = {}
for name, grade in zip(names, grades):
    d_2[name] = grade

print(d_2)