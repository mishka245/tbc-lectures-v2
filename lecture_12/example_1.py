def foo(a, b):
    print(a, b)

def main():
    # test case 1
    user_input_a_1 = input("Please enter a - ")
    user_input_b_1 = input("Please enter b - ")
    foo(user_input_a_1, user_input_b_1)

    # test case 2
    user_input_a_1 = input("Please enter a - ")
    user_input_b_1 = input("Please enter b - ")
    foo(user_input_a_1, user_input_b_1)


# SOLID
if __name__ == "__main__":
    main()

