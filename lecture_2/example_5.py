a = 10
b = 15

"""
and 
t t -> t
t f -> f
f t -> f
f f -> f

or 
t t -> t
t f -> t
f t -> t
f f -> f
"""

if a > 10 and b > 10:
    print("Both are true")
else:
    print("One or both are false")