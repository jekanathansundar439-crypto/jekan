# list - used to store multiple elements in a single variable
# ordered, indexed, allow duplicates, changable
# a list of three elements
ages = [19, 26, 29]
print(ages)

# a list containing strings, numbers and another list
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)

# an empty list
empty_list = []
print(empty_list)
languages = ['Python', 'Swift', 'C++']

# access the first element
print('languages[0] =', languages[0])

# access the third element
print('languages[2] =', languages[2])
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

fruits.append('cherry')

print('Updated List:', fruits)
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits) 

fruits.insert(2, 'cherry')

print("Updated List:", fruits)
numbers = [1, 3, 5]
print('Numbers:', numbers)

even_numbers  = [2, 4, 6]
print('Even numbers:', numbers)

# adding elements of one list to another
numbers.extend(even_numbers)

print('Updated Numbers:', numbers) 
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers) 

cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements:', len(cars))

# Method	Description
# append()	Adds an item to the end of the list
# extend()	Adds items of lists and other iterables to the end of the list
# insert()	Inserts an item at the specified index
# remove()	Removes the specified value from the list
# pop()	    Returns and removes item present at the given index
# clear()	Removes all items from the list
# index()	Returns the index of the first matched item
# count()	Returns the count of the specified item in the list
# sort()    Sorts the list in ascending/descending order
# reverse()	Reverses the item of the list
# copy()	Returns the shallow copy of the list

