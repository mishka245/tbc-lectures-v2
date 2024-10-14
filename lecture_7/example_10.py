word = input("Please enter your word - ")

new_word = ""

for c in word:
    if c not in "aoieu" :
        new_word += c

print(new_word)
