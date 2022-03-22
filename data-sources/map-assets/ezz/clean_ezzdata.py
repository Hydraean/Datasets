#script for cleaning fma_data

import json

print("Cleaning EZZ data...")

ezz_file = open("./EEZ_Land_v3_202030.json")
ezz_data = json.load(ezz_file)

# coord simplifier
def round_floats(o):
    if isinstance(o, float):
        return round(o, 6)
    if isinstance(o, dict):
        return {k: round_floats(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [round_floats(x) for x in o]
    return o

# write to file
def writeTofile(file_data):
    print("File written successfully!")
    with open('ezz.json', 'w') as outfile:
        data = json.dumps(file_data,separators=(',', ':'))
        outfile.write(data)    

outData = {"type":"FeatureCollection","features":[]}

for i, x in enumerate(ezz_data["features"]):
    new_geometry = round_floats(x["geometry"])
    outData["features"].append({"id":i,"type":"Feature","geometry":new_geometry,"properties":{
        "territory": x["properties"]["TERRITORY1"],
        "pol_type": x["properties"]["POL_TYPE"],
        "sov1": x["properties"]["SOVEREIGN1"],
    }})
    print(x["geometry"]["coordinates"])

writeTofile(outData)
print("fma cleanup complete. [100%]")
