'''firstNumber = int(input("Enter a first number:"))
operator = input("Enter a operator in between (+,-,*,/): ")
secondNumber = int(input("Enter a second number:"))

if operator == "+":
    print(firstNumber + secondNumber)
elif operator == "-":
    print(firstNumber - secondNumber)
elif operator == "*":
    print(firstNumber * secondNumber)
elif operator == "/":
    print(firstNumber / secondNumber)
else:
    print("Please select operator")'''

 
import json
fileData = open("data/data.json")  #opening JSON File
data = json.load(fileData)      #returns JSON object as a dictionary

List = []
for i in data:
    
    # print(i["salary"]<1000)
    if i["salary"] <200000:
        List.append(i["name"])
print(List)
    
fileData.close()          # Closing file 


