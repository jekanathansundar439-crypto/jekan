# Extract Vowels from a String
text = "programming"
result = list(filter(lambda x: x in "aeiou", text))
print(result)