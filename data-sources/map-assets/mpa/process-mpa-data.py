import json
import sys

print("Cleaning Marine Protected Areas file data...")

mpa_file = "./mpa_wdpa_philippines.json"

mpa_load_file = open(mpa_file)
mpa_data = json.load(mpa_load_file)


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
    with open('mpaph.json', 'w') as outfile:
        data = json.dumps(file_data,separators=(',', ':'))
        outfile.write(data)  

# loading
def progress(count, total, status=''):
    red='\033[01;31m'
    gre='\033[02;32m'
    yel='\033[00;33m'
    blu='\033[01;34m'
    
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    
    percentage = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '-' * (bar_len - filled_len)
    
    if percentage <= 50:
        col = red
    elif percentage > 50 and percentage <= 80:
        col = yel
    elif percentage > 80 and percentage <= 99:
        col = gre
    else:
        col = blu
    
    sys.stdout.write('\r{0}[{1}] {2}%  {3}'.format(col, bar, percentage, status))
    sys.stdout.flush()


#  data processing

outData = {"type":"FeatureCollection","features":[]}

for i, x in enumerate(mpa_data["features"]):
    if x["geometry"]:
        new_geometry = round_floats(x["geometry"])
        try:
            outData["features"].append({"id":i, "type":"Feature","geometry":new_geometry,"properties":{
              "NAME": x["properties"]["NAME"],
              "MANG_AUTH": x["properties"]["MANG_AUTH"],
              "STATUS": x["properties"]["STATUS"],
              "MARINE": x["properties"]["MARINE"],
            }})
        except:
            sys.stdout.write("\r") 
        
    progress(i, len(mpa_data["features"]), status='Processing MPA Dataset..')    


writeTofile(outData)

print("MPA Data processing complete!")