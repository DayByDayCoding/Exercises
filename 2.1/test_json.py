"""This is just so I can test that I wrote the JSON correctly."""

import json

json_file = open("cities_data.json")

dict_from_json = json.load(json_file)
print("type:", type(dict_from_json))
print("data:", dict_from_json)

json_file.close()
