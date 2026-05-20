s = input("Enter string: ")
count = 0

for ch in s:
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        if ch not in "aeiouAEIOU":
            count += 1

print("Consonants:", count)