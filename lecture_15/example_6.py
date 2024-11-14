names = ['Anna', 'John', 'Denise', 'Katy']
grades=[100, 73, 85, 49]

d = {}

for i in range(len(names)):
    d[names[i]] = grades[i]

print(d)