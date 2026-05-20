# Given two lists, return the set of common elements that appear more than once in both lists.
lst1 = [1,2, 3]
lst2 = [2, 3, 4]

common = set(lst1) & set(lst2)

print(common)