import json
Deets = '{ "name":"Khushi", "age":21, "state":"UP"}'
pyDeets = json.loads(Deets)
print(pyDeets)
print("Name: {}".format(pyDeets['name']))
print("Age: {}".format(pyDeets['age']))
print("State: {}".format(pyDeets['state']))
