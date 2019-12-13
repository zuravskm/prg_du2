import json

with open("input.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

# print(data)
# print(len(data['features']))

# feat = data["features"][0]["geometry"]
# print(feat)

coordinates = []

for feat in data["features"][0]["geometry"]:
    if feat["coordinates"] == :
        coordinates.append(feat)

print(coordinates)
print(len(coordinates))

