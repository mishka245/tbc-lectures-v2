a = 26
possible_root = 0
step = 1
epsilon = 10

guess_count = 0
while abs(a - possible_root ** 3) > epsilon:
    guess_count += 1
    possible_root += step


print(f"Epsilon - {epsilon}, Step - {step}, answer - {possible_root}, Guess count - {guess_count}")