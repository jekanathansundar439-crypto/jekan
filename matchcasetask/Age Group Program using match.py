# Age Group Program using match
age = int(input("Enter your age: "))
match age:
    case age if age <= 12:
        print("Child")
    case age if age <= 19:
        print("Teen")
    case age if age <= 59:
        print("Adult")
    case _:
        print("Senior")