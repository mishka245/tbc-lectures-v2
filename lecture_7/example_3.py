text = input("Please enter any word - ")

for i in range(len(text)):
    if text[i] == "e":
        continue
    print(text[i])
