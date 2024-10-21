cube = 27

epsilon = 0.00000000000001
low = 0
high = cube
answer = (low + high) / 2

iterations = 0
while abs(answer ** 3 - cube) >= epsilon:
    if answer ** 3 > cube:
        high = answer
    else:
        low = answer
    answer = (low + high) / 2
    iterations += 1

print(f"Number of iterations = {iterations}")
print(f"Answer = {answer}")
