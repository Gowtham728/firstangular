
#JSON is a syntax for storing and exchanging data.

#JSON is text, written with JavaScript object notation.

'''
convert from JSON to python
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])
'''

'''
Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string 
by using the json.dumps() method.


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 

'''

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

