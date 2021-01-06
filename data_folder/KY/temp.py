import json
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "ky_for_preprocessing.geojson"
abs_file_path = os.path.join(script_dir, rel_path)

x = open(abs_file_path)
data = json.load(x)
i = 0
ie=0
for feature in data.get('features'):
    level_1_coord = feature.get('geometry').get('coordinates')
    level_2_coord = feature.get('geometry').get('coordinates')[0]
    if (len(level_1_coord) != 1):
        print("MULTIPOLYGON: " + str(feature.get('properties').get('vtd')))
        i=i+1
    if (len(level_2_coord) != 1):
        print("ENCLOSED: " + str(feature.get('properties').get('vtd')))
        ie=ie+1

print("# of multipolygons: " + str(i))
print("# of enclosed: " + str(ie))