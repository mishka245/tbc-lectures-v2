


def main():
    file_name = input("Please enter file name - ")
    file_name = f"{file_name}.txt"

    with open(file_name, "w") as file:
        for _ in  range(5):
            word = input("please enter word - ")
            file.write(word)
            file.write("\n")



if __name__ == "__main__":
    main()
