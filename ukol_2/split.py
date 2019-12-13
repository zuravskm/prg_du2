import json

### loading input GeoJSON data

with open("input.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)


### find and save coordinates to a new list

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


###sorting_animate data by coordinates




### distribution data by quadtree




### finally saving the output to a new GoeJSON file

# gj_structure = {'type': 'FeatureCollection'}
# gj_structure['features'] = something

# with open("output.geojson", "w", encoding="utf-8") as f:
    # json.dump(gj_structure, f, indent=2, ensure_ascii=False)
