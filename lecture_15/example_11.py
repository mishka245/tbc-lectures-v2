data = {'Anna': 100, 'John': 73, 'Denise': 85, 'Katy': 49}


print(data["Anna"])
# print(data["Giorgi"])
print(data.get("Anna"))
print(data.get("Giorgi"))  # -> None
print(data.get("Giorgi", 0))  # -> 0


print("Giorgi" in data)  # -> False