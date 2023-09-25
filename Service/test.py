print("Hello")

import json

openFile = open("data/data.json")
loadFile = json.load(openFile)

# print(loadFile)
for data in loadFile:
    for key,value in data.items():
        print(key,value)
openFile.close()