from cgi import print_directory
import json
import os
from traceback import print_list
from colorama import Fore, Style
import moment
import mimetypes


mimetypes.init()
mimetypes.knownfiles



# write to file
def writeTofile(file_data, file_name):
    print(Fore.BLUE+"Write to index file successful:"+Style.RESET_ALL, file_name)
    with open(file_name, 'w') as outfile:
        data = json.dumps(file_data,separators=(',', ':'))
        outfile.write(data)    

# import file details
files_metadata = json.load(open("./file_details.json"))



# Generate Index file
github_raw_baseurl = "https://raw.githubusercontent.com/Hydraean/Datasets/main"        

target_dirs = ["./data-sources", "./output-datasets"]

print(Fore.LIGHTBLUE_EX + '⬢ HYDRAEAN DATASETS: Indexing..')
print(Fore.YELLOW+"==============================="+Style.RESET_ALL) 

file_index = []
needs_description = []

for dir in target_dirs:
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            print(Fore.GREEN+"⬢ Found: => "+Style.RESET_ALL+file_path)

            file_name = file_path.split(sep="/")[-1]    
            file_extension = file_name.split(sep=".")[-1]    
            size = os.path.getsize(file_path)
            url = f'{github_raw_baseurl}{file_path.replace("./","/")}'

            file_info = {
               "id": file_name,
               "name": file_name,
               "info": "-",
               "size": size,
               "mime_type": mimetypes.guess_type(file_path)[0],
               "file_extension": f".{file_extension}".lower(),
               "url": url,
               "updated_at": moment.now().format("YYYY-M-D")
            }

            # exclude python cleaner files
            if(file_info["file_extension"] != ".py"):
                # make sure only unique files are indexed.
                if not any(d['id'] == file_info["id"] for d in file_index):
                    file_index.append(file_info)
                else:
                    print(Fore.LIGHTMAGENTA_EX+"[File Notice]: Already Indexed."+Style.RESET_ALL)

# assign file metadata
print(Fore.LIGHTBLUE_EX + '⬢ HYDRAEAN DATASETS: Assinging file Metadata...'+Style.RESET_ALL)
for fx in file_index:
    if fx["id"] in files_metadata:
        fx["info"] = files_metadata[fx["id"]];
    else:
        needs_description.append(
            {
            "title": fx["id"],
            "caption": "",
            "image": "https://raw.githubusercontent.com/Hydraean/Datasets/main/assets/default.png"
            }
        )
print(Fore.GREEN+"✅ Assinging Metadata: [DONE]"+Style.RESET_ALL)




# Summary
print(Fore.YELLOW+"==============================="+Style.RESET_ALL) 
print(Fore.LIGHTBLUE_EX + '⬢ HYDRAEAN DATASETS: Summary.')
print(Fore.YELLOW+"==============================="+Style.RESET_ALL) 

if len(needs_description) > 0:
   print(Fore.RED+"❌ Found Files with file details please add a description for each"+Style.RESET_ALL)
   for file in needs_description:
       print(file["title"])
       # push template description to file details.json
       files_metadata[file["title"]] = file


# check for incomplete descriptions
incomplete_description = []     
  
for kx in files_metadata.keys():
    if(files_metadata[kx]["caption"] == ""):
        incomplete_description.append(files_metadata[kx])

if len(incomplete_description) > 0:
   print(Fore.RED+"❌ Found Files no description"+Style.RESET_ALL)
   for fx in incomplete_description:
       print(fx["title"])


print(Fore.GREEN+"✅ Indexing Process: [DONE]"+Style.RESET_ALL)


writeTofile(file_index, "./hydraean-datasets.json")
writeTofile(files_metadata, "./file_details.json")