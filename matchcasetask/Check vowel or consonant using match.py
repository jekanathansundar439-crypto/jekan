# Check vowel or consonant using match
ch = input("Enter a character: ")
match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("It is a Vowel")
    case _:
        print("It is a Consonant")