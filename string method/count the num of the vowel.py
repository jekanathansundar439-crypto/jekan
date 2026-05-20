text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0 
for c in text:
    if c in vowels:
        count += 1
print(count)
