#!/usr/bin/env python

import json

try:
    f = open('data.json')
    data = json.load(f)
except (FileNotFoundError):
    print("The file cannot be found.")
except (json.JSONDecodeError):
    print("The file is not in a JSON format")

with open("database.txt", "w") as outfile:
    json.dump(data, outfile)