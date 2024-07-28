import json

with open('person.json', 'r') as file:
    data = json.load(file)
    
print(data)