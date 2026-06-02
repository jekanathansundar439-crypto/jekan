# Filter Words Longer Than 4 Characters
words = ["cat", "elephant", "dog", "tiger"]
result = list(filter(lambda x: len(x) > 4, words))
print(result)