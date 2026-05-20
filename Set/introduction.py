# SET
# a set is an unordered collection of unique elements. 
# Sets are primarily used to eliminate duplicate values and
# perform mathematical operations like unions and intersections.

# Key Characteristics
# Unique Elements: Sets automatically remove duplicate entries. 
# If you try to add the same value twice, it will only appear once.

# Unordered: Elements do not have a defined order, so they cannot be accessed by an index or key.

# Mutable (Mostly): While the set itself is mutable (you can add or remove items), 
# the individual elements inside it must be immutable (like strings, numbers, or tuples).

# Efficient: Sets use a hash table internally, 
# making membership tests (checking if an item is "in" the set) extremely fast compared to lists.

# How to Create a Set
# You can create a set using curly braces {} or the built-in set() function.

# Adding and Removing Elements:

# add(element): Adds a single element to the set.
# 👉 One item add pannum.

# update(iterable): Adds multiple elements from another iterable (like a list or tuple) to the set.
# 👉 Multiple items add pannum.

# remove(item): Deletes a specific item. If the item is not found, it raises a KeyError
# 👉 Specific item remove pannum.

# discard(item): Removes a specific item but does not raise an error if the item is missing.
# 👉 Item remove pannum.

# pop(): Removes and returns a random element from the set.
# 👉 Random item remove pannum.

# clear(): Removes all elements, leaving the set empty.
# 👉 Set full-ah empty pannum.

# Mathematical Set Operations:

# union(*others): Returns a new set containing all elements from the original and all others.
# 👉 Rendu set elements-ah combine pannum.

# intersection(*others): Returns a new set with only the elements common to all sets.
# 👉 Common elements mattum tharuum.

# difference(*others): Returns a new set with elements in the first set that are not in the others.
# 👉 First set-la irundhu second set items remove pannum.

# symmetric_difference(other): Returns a new set with elements in either set, but not both.
# 👉 Common items remove pannitu remaining items tharuum.  

# Comparison and Relationships:

# issubset(other): Returns True if all elements of the set are in the other set.
# 👉 Meaning:
# Oru set-la irukkura ella elements-um another set-la irukka nu check pannum.

# issuperset(other): Returns True if the set contains every element of the other set.
# 👉 Meaning:
# Current set-ku another set oda ella elements-um irukka nu check pannum.

# isdisjoint(other): Returns True if the two sets have no elements in common.
# 👉 Meaning:
# Rendu sets-kum common element irukka nu check pannum.
# Common element illa → True
# Common element irundha → False

# Additional Utility Methods:

# copy(): Returns a shallow copy of the set.
# 👉 Meaning:
# Original set oda duplicate copy create pannum.

# len(set): (Built-in function) Returns the number of items in the set.
# 👉 Meaning:
# Set-la evlo items irukku nu count pannum.

# sorted(set): (Built-in function) Returns a new sorted list from the set's elements
# 👉 Meaning:
# Set elements-ah ascending order-la sort pannum.