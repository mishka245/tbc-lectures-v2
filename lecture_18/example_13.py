import json



json_str = '{"some_key": 123}'
d = json.loads(json_str)
print(d)
print(d["some_key"])
print(type(d))
