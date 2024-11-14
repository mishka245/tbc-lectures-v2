d = dict(name="Nini", age=61)

print(id(d))

d["address"] = "UKNOWN"
del d["age"]

print(id(d))
print(d)
