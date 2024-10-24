
def square(x):
    return x ** 2


def double_square(x):
    temp = square(x)
    return square(temp)

print(double_square(2))
