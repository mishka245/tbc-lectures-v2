
class Student:
    def __init__(self, name, surname="Unknown"):
        self.name = f"{name} {surname}"
        self.exams = []

    def __str__(self):
        return f"Student({self.name}) - Exams - {self.exams}"

def main():
    s1 = Student("Giorgi", "Beridze")
    s2 = Student("Nini", "Akhvlediani")
    s3 = Student("Suliko", )
    print(s1)
    print(s2)
    print(s3)


if __name__ == "__main__":
    main()
