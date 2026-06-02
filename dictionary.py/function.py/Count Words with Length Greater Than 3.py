# Count Words with Length Greater Than 3
words = ["cat", "apple", "dog", "banana"]
result = len(list(filter(lambda x: len(x) > 3, words)))
print(result)