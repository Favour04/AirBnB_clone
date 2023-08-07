#!/usr/bin/python3

import json
with open('file.json', 'r') as file:
    data = json.load(file)
    print("-- Reloaded objects --")
    for obj_id in data.keys():
            obj = data[obj_id]
            print(obj)

