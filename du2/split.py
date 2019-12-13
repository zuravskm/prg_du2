import json

with open("input.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(len(data['features']))
