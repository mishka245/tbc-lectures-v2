def multiply_n_10(x):
    return x * 10

def main():
    my_list = [-1, 0, 10, -3, 20]
    for i in map(multiply_n_10, my_list):
        print(i)

if __name__ == "__main__":
    main()


