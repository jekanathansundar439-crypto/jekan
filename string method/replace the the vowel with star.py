st = input("Enter a string: ")
result = ""
for ch in st:
    if ch in "aeiouAEIOU":
        result = result + "*"
    else:
        result = result + ch

print("Output:", result)