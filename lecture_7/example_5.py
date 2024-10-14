text = input("Please enter your word - ")

found = False

for i in range(len(text)):
    if "a" == text[i]:
        found = True
        break

if found:
    print("არის")
else:
    print("არ არის")
