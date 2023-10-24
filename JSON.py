import json


person = {
  "name": "Alice",
  "age": 30,
  "address": {
    "street": "Dunajska",
    "city": "Ljubljana"
  },
  "married": True
}
with open('./person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=True)



with open('./person.json', 'r') as f:
    deserialized_person = json.load(f)

deserialized_person['age'] = 31
deserialized_person['married'] = False
deserialized_person['address']['street'] = "Trzaska"

with open('./person.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4, sort_keys=True)

    import os

file_size = os.path.getsize("./DATA/POMOC/person.json")
print(f"JSON file size: {file_size} bytes")

import json

with open("./DATA/POMOC/person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")

file_size = os.path.getsize("./DATA/POMOC/person.xml")
print(f"XML file size: {file_size} bytes")