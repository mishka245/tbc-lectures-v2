with open("hi.txt", "r") as file:
    content = file.read()

with open("hi.txt", "w") as file:
    file.write(f"{content} - \nI was here")


