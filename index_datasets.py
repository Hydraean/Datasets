import json
import os
from colorama import Fore, Style
import moment



# write to file
def writeTofile(file_data):
    print("Write to index file successful.")
    with open('./hydraean-datasets.json', 'w') as outfile:
        data = json.dumps(file_data,separators=(',', ':'))
        outfile.write(data)    



# Generate Index file
github_raw_baseurl = "https://raw.githubusercontent.com/Hydraean/Datasets/main"        
rootdir = './data-sources'
dataset_index = []

target_dirs = ["./data-sources/", "./output_datasets/"]

print(Fore.LIGHTBLUE_EX + '⬢ HYDRAEAN DATASETS: Indexing..')
print(Fore.YELLOW+"==============================="+Style.RESET_ALL) 

file_index = []

for dir in target_dirs:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(subdir, file)
            print(Fore.GREEN+"⬢ Found: => "+Style.RESET_ALL+file_path)

            file_name = file_path.split(sep="/")[-1]      
            file_type = file_name.split(sep=".")[-1]    
            size = os.path.getsize(file_path)
            url = f'{github_raw_baseurl}{file_path.replace("./","/")}'

            file_info = {
               "id": file_name,
               "name": file_name,
               "info": "-",
               "size": size,
               "type": file_type,
               "url": url,
               "updated_at": moment.now().format("YYYY-M-D")
            }

            # exclude python cleaner files
            if(file_info["type"] != "py"):
                # make sure only unique files are indexed.
                if not any(d['id'] == file_info["id"] for d in file_index):
                    file_index.append(file_info)
                else:
                    print(Fore.LIGHTMAGENTA_EX+"[File Notice]: Already Indexed."+Style.RESET_ALL)



writeTofile(file_index)