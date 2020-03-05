# https://www.programiz.com/python-programming/json

import json

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
parsed_json = (json.loads(json_data))
print (json.dumps(parsed_json, indent=4, sort_keys=True))


with open("person.json") as f:
    loaded_json = json.load(f)

print(loaded_json)
print(json.dumps(loaded_json, indent=4))

for x in loaded_json:
    print (x)


# Writing JSON to a file

person1 = {"name": "Bob",
               "languages": ["English", "Fench"],
               "married": True,
               "age": 32
               }
person2 = {"name": "Ali",
               "languages": ["English", "Farsi"],
               "married": True,
               "age": 33
               }
list_of_dict = [person1, person2]

with open('person_w.json', 'w') as json_file:
    json.dump(list_of_dict, json_file, indent=4, sort_keys=True)
