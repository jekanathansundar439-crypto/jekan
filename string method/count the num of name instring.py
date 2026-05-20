st = input("Enter sentence: ")
wc = 0

for ch in st:
    if ch != " ":
        wc = 1
        break

for ch in st:
    if ch == " ":
        wc += 1

print("Words:", wc)