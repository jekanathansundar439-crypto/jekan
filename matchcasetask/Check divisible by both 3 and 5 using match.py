# Check divisible by both 3 and 5 using match
num = int(input("Enter a number: "))
match num:
    case num if num % 3 == 0 and num % 5 == 0:
        print("The number is divisible by both 3 and 5")
    case _:
        print("The number is NOT divisible by both 3 and 5")