file_name = input("Please enter file name - ")


try:
    with open(f"{file_name}.txt", "r") as file:
        print(file.read())
except OSError as error:
    print(type(error))
    print(error)