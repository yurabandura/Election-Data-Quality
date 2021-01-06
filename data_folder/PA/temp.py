import json
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "PA_precinct_c.geojson"
abs_file_path = os.path.join(script_dir, rel_path)


x = open(abs_file_path)
data = json.load(x)
i = 0
ie=0
for feature in data.get('features'):
    if (feature.get('geometry').get('type') != 'MultiPolygon'):
        coord = feature.get('geometry').get('coordinates')
        new_coord = [coord]
        feature['geometry']['coordinates'] = new_coord
        new_type = 'MultiPolygon'
        feature['geometry']['type'] = new_type


filename = os.path.join(script_dir, 'update_pa_precinct_c.geojson')


with open(filename, 'w') as f:
    json.dump(data, f)


print("# of multipolygons: " + str(i))
print("# of enclosed: " + str(ie))