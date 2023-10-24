import os

file_size = os.path.getsize("./person.json")
print(f"JSON file size: {file_size} bytes")

import json

with open("./person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")

file_size = os.path.getsize("./person.xml")
print(f"XML file size: {file_size} bytes")
import xml.etree.ElementTree as ET

tree = ET.parse('./person.xml')
root = tree.getroot()

for elem in root:
    print(f"Element: {elem.tag}, Text: {elem.text}")