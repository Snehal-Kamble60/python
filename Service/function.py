import json

openFile = open("data/data.json")
data = json.load(openFile)

def emp (empdata):
    print(empdata)
    listData = []
    for empage in empdata:
        if  empage["age"] > 35:
            print("cheking above 40",empage["age"] > 40)
            listData.append(empage["name"])
        else:
            print('invalid')
    print(listData)
emp(data)