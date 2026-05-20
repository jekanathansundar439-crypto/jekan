text = input("Enter a string: ")
for ch in text:
    if (ch < 'A' or ch > 'Z') and (ch < 'a' or ch > 'z'):
        print("Not only alphabets")
        break
else:
    print("Only alphabets")
    