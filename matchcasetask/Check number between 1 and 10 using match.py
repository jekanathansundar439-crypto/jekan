# Check number between 1 and 10 using match
num = int(input("Enter a number: "))
match num:
    case num if 1 <= num <= 10:
        print("The number is between 1 and 10")
    case _:
        print("The number is NOT between 1 and 10")