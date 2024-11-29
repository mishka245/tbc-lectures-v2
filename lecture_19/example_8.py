a = [1,2,3,4,5,600]
b = [1,200,3,0,5,6]
c = []

for element_a, element_b in zip(a, b):
    try:
        c.append(element_a / element_b)
    except ZeroDivisionError:
        c.append("Err")

print(c)