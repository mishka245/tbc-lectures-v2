# cubic root(50) -> 3.6840314 . . .
a = 50
possible_root = 0
step = 0.5
epsilon = 8

guess_count = 0
while abs(a - possible_root ** 3) > epsilon:
    guess_count += 1
    print(possible_root)
    possible_root += step


print(f"Epsilon - {epsilon}, Step - {step}, answer - {possible_root}, Guess count - {guess_count}")


cubeRoot = 1  # do not do this
cube_root = 1 # do this instead
