import json

with open('fx6_database.json') as f:
    cam_para = json.load(f)

for i in cam_para:
    print(i)