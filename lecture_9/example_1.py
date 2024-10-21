cube = 27

epsilon = 0.001
answer = 0
iterations = 0
step = 0.001

while abs(answer ** 3 - cube) >= epsilon:
    answer = answer + step
    iterations += 1

print(f"Number of iterations = {iterations}")
print(f"Answer = {answer}")
