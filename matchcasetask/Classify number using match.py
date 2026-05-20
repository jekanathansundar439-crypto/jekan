# Classify number using match

num = int(input("Enter a number: "))

match num:
    case 0:
        print("Zero")
    case num if num > 0 and num % 2 == 0:
        print("Positive Even")
    case num if num > 0 and num % 2 != 0:
        print("Positive Odd")
    case _:
        print("Negative")