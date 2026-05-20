sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word is:", longest)