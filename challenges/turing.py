import json

f = open("algo.json", "r")
c = f.read()
print(c)

# Convert from Python to JSON:
js = json.loads(c)

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
#     }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)