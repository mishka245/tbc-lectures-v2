import json

"""
json.dump - write dictionary into file as a json
json.dumps
json.load - reads json from file as a dict 
json.loads
"""


with open("test_1.json", "r") as file:
    example_json_as_dict = json.load(file)

print(type(example_json_as_dict))
print(example_json_as_dict["list"][1])

example_json_as_dict["list"].append("I am from program")

with open("task_1_modified.json", "w") as file:
    json.dump(example_json_as_dict, file, indent=2)

