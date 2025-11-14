import json

# json_data = '{"nombre": "Luis", "edad": 30}'

# python_data = json.loads(json_data)
# print(python_data)
# print(type(python_data))

python_data = {"nombre": "Luis", "edad": 30}
print(type(python_data))
json_data = json.dumps(python_data)
print(json_data)
print(type(json_data))
