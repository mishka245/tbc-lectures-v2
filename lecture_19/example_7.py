a = [1,2,3,4,5,600]
b = [1,200,3,0,5,6]
c = []

for i in range(len(a)):
    try:
        c.append(a[i] / b[i])
    except ZeroDivisionError:
        c.append("Err")

print(c)