import os
import json

script_dir = os.path.dirname(__file__)
txt_path = "data.json"
file = os.path.join(script_dir, txt_path)

jsonFile = open(file, "r")
data = json.load(jsonFile)

