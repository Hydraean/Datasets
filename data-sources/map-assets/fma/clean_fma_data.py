#script for cleaning fma_data

import json

print("Cleaning FMA data...")

fma_file = open("./fma_data.json")
fma_data = json.load(fma_file)

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
    with open('fma.json', 'w') as outfile:
        data = json.dumps(file_data,separators=(',', ':'))
        outfile.write(data)    

outData = {"type":"FeatureCollection","features":[]}

for i, x in enumerate(fma_data["features"]):
    new_geometry = round_floats(x["geometry"])
    outData["features"].append({"id":i,"type":"Feature","geometry":new_geometry,"properties":{
        "fma": x["properties"]["FMA"],
        "area_sqkm": x["properties"]["Area_sqkm"],
    }})
    print(len(x["geometry"]["coordinates"]))

writeTofile(outData)
print("fma cleanup complete. [100%]")
