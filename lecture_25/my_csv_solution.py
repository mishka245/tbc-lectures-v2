
import csv

class Person:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    @classmethod
    def from_csv_row(cls, row):
        return cls(row[0], row[1], int(row[2]), row[3])

    @classmethod
    def from_csv_string(cls, s):
        return cls(*s.strip().split(','))



    def __str__(self):
        return f'{self.name} {self.surname} ({self.age}) from {self.city}'

persons = []

with open('example_1.csv', 'r') as f:
    reader = csv.reader(f, escapechar='\\')
    header = next(reader)
    for row in reader:
        person = Person.from_csv_row(row)
        persons.append(person)


for p in persons:
    print(p)

print("Average salary:", sum([p.age for p in persons]) / len(persons))