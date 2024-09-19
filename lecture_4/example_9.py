input_word = input("Please enter your word - ")
repeat_count = input("Please enter count - ")

repeat_count_as_float = float(repeat_count)
repeat_count_as_int = int(repeat_count_as_float)

if repeat_count_as_float != repeat_count_as_int:
    print("Please enter integer")
    exit(1)

if repeat_count_as_int <= 0:
    print("Please enter positive integer")
    exit(137)


for i in range(repeat_count_as_int):
    print(input_word)

