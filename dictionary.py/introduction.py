# dictionary
# A dictionary in Python is a built-in data structure used to store data in key-value pairs.
# 👉Python la dictionary nu sonna, data ah key-value pair format la store panna use pannuvom.

# Key Characteristics
# Ordered: Since Python 3.7, dictionaries maintain the order in which items were inserted.
# 👉Python 3.7 ku apram dictionary la items insert panna order save aagum.

# Changeable (Mutable): You can add, remove, or modify items after the dictionary is created.
# 👉Dictionary create pannina apram athula data add / change / delete panna mudiyum.

# Unique Keys: Keys must be unique; if you add a duplicate key, it will overwrite the old value.
# 👉Same key rendu thadava use panna koodathu.Duplicate key vandha old value overwrite aagum.

# Key Requirements: Keys must be of an immutable type, such as strings, numbers, or tuples.
# 👉Keys immutable type ah irukanum.Immutable na change panna mudiyatha type.

# Basic Syntax
# Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Print the number of items in the dictionary:
print(len(thisdict))

# Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Get the value of the "model" key:
x = thisdict.get("model")

# Get a list of the keys:
x = thisdict.keys()

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

