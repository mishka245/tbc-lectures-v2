class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __gt__(self, other):
        return self.salary > other.salary


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def __gt__(self, other):
        return len(self.employees) > len(other.employees)


def main():
    dev_1 = Developer("Giorgi", "Kharshiladze", 100000, "Python")
    dev_2 = Developer("John", "Doe", 1000, "Java")
    dev_1.apply_raise()
    if dev_1 > dev_2:
        print("dev_1 has higher salary", dev_1.salary)
    else:
        print("dev_2 has higher salary", dev_2.salary)

    manager_1 = Manager("Sue", "Smith", 90000, [dev_1])
    manager_1.add_employee(dev_2)
    manager_2 = Manager("John", "Doe", 90000, [])
    if manager_1 > manager_2:
        print("manager_1 has more employees", len(manager_1.employees))
    else:
        print("manager_2 has more employees", len(manager_2.employees))

    print(dev_1.salary)


if __name__ == "__main__":
    main()
