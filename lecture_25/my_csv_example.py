
with open('example_1.csv', 'r') as f:
    print(f.readline())  # header
    for line in f:
        print(line.strip().split(','))


print('---')
# same with csv module
import csv

with open('example_1.csv', 'r') as f:
    reader = csv.reader(f, escapechar='\\')
    header = next(reader)
    print(header)
    for row in reader:
        print(row)