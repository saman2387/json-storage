import json

data = {"name": "Sara", "languages": ["Python", "C++"]}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    print(json.load(f))
