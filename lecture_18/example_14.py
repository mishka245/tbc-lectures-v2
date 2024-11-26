import datetime
import json

now = datetime.datetime.now()
print(type(now))

d = {"name": "Giorgi", "age": 49, "time": now}


with open("example_1.json", "w") as file:
    json.dump(d, file)  # will fail, can be solved with custom serializer
