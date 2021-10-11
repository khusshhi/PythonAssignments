import json
python_object = '{"khushi": 1, "Ramya": 1, "Ramya": 3, "Khushi": 4, "Pragya": 2, "Maniya": 2}'
print("Original Python object: {}".format(python_object))
json_object = json.loads(python_object)
print("Unique Keys in JSON object: {}".format(json_object))
