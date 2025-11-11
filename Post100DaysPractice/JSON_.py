
# JSON module

# JSON (JavaScript Object Notation) is a lightweight data format used for data exchange between servers
# and applications. It is widely used in APIs, web applications, and configurations.
#
# Python provides the json module to work with JSON data. You can import the json module like this:
# import json

#--------------------------------------------------------------------------------------------------------------
# Converting Python Objects to JSON (Serialization) -
# (also called encoding or dumping) is converting a Python object into a JSON-formatted string.


# json.dumps() – Convert Python object to JSON string
# example  -

# import json
# data = {"name": "Alice", "age": 25, "city": "New York"}
# json_string = json.dumps(data)
# print(json_string)  # Output: {"name": "Alice", "age": 25, "city": "New York"}
# print(type(json_string))  # <class 'str'>
#-------------------------------------------------

# json.dump() – Write JSON data to a file
# Example -

# with open("data.json", "w") as file:
#     json.dump(data, file)
-------------------------------------------------------------------------------------------------------------

# Converting JSON to Python Objects (Deserialization) -
# Deserialization (also called decoding or loading) is converting JSON-formatted data into Python objects.

# json.loads() – Convert JSON string to Python object
# example -
#
# with open("data.json", "r") as file:
#     python_data = json.load(file)
#
# print(python_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
#-------------------------------------------------------------------------------------------------------------

# Formatting JSON Output
# You can format JSON for better readability using indentation.

# example -
# formatted_json = json.dumps(data, indent=4)
# print(formatted_json)
#-------------------------------------------------------------------------------------------------------------

# Summary of Common JSON Methods

#
# Method	                          Description	                                       Example
# json.dumps(obj)	           Converts Python object to JSON string	              json.dumps(data)
# json.dump(obj, file)	   Writes JSON to a file	                              json.dump(data, file)
# json.loads(json_string)	   Converts JSON string to Python object	              json.loads(json_data)
# json.load(file)	           Reads JSON from a file	                              json.load(file)