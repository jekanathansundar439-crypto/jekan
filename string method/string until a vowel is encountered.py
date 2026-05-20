s = input("Enter a string: ")

for ch in s:
    if ch in "aeiouAEIOU":
        break
    print(ch, end="")