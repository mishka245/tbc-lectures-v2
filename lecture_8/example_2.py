from decimal import Decimal

s = Decimal("0.0")
for i in range(10):
    s += Decimal("0.1")

print(s)

if s == 1:
    print("Equal")