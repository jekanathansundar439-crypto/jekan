# In Python, a tuple is a built-in data type used to store a collection of items in a single variable.
# Core Characteristics
# Ordered: Items have a defined order that will not change.
# Immutable: Once created, you cannot change, add, or remove elements.
# Allows Duplicates: Since items are indexed, multiple items can have the same value.
# Heterogeneous: A single tuple can store different data types, such as integers, 
#                strings, and even other tuples
# Basic Syntax 
# Tuples are written with round brackets (), with items separated by commas. 
#  Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Creating a single-item tuple (requires a trailing comma)
single_tuple = ("apple",) 

# Accessing by index (starts at 0)
print(my_tuple[1])  # Output: banana

# Common Operations  
# Unpacking: Assigning tuple values to individual variables in one line.
# Built-in Methods: 
# Tuples have only two: .count() (counts occurrences) and .index() (finds the first position of a value).
# Joining: You can combine tuples using the + operator to create a new one.
# Functions: Many Python functions return multiple values as a tuple by default