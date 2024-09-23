from random import randint

left = randint(0, 10)
right = randint(10, 20)

# Print -  {5, 15}

#     {   5,      15   }
s = f"{{{left}, {right}}}"
print(s)

