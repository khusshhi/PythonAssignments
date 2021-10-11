model=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("original model list is: {}".format(model))
model.sort(key=lambda x:x['make'])
print('sorted list of model is: {}'.format(model))
