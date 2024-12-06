
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.exams = []

    def __str__(self):
        return f"Student({self.name}, {self.surname}) - Exams - {self.exams}"

def main():
    s1 = Student("Giorgi", "Beridze")
    s2 = Student("Nini", "Akhvlediani")
    print(s1)
    print(s2)


if __name__ == "__main__":
    main()
