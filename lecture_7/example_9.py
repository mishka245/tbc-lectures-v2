word = input("Please enter your word - ")

new_word = ""

for c in word:
    if c != "a" and c != "o" and c != "i" and c != "e" and c != "u":
        new_word = new_word + c


print(new_word)