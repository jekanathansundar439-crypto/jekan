s = input("Enter string: ")
r = ""
for ch in s:
    if 'a' <= ch <= 'z':
        r += chr(ord(ch) - 32)
    else:
        r += ch
print("Uppercase:", r)