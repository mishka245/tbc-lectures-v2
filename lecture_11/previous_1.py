# write small example about keyword arguments
def create_person(name, age, **kwargs):
    print('name', name)
    print('age', age)

    for key, value in kwargs.items():
        print(key, value)


def main():
    create_person('John', 30, city='New York', country='USA')
    print("\n\n\n")
    create_person('Jane', 25, country="Georgia", region="Imereti")
    print("\n\n\n")
    create_person('Jack', 35)


if __name__ == "__main__":
    main()
