text = input("Please enter any word - ")

counter = 0

for i in range(len(text)):
    if text[i] == "a":
        counter += 1


print(counter)