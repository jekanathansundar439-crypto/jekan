text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
if text == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    