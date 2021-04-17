import json

data = {
        'Name': 'Ericpig',
        'height': 180.5,
        "Male": True}

jsonData = json.dumps(data)
with open('practice.json', 'w')as f:
    f.write(jsonData)

with open('practice.json', 'r') as f:
    text = json.load(f)
    
    
print(text['height'])
















