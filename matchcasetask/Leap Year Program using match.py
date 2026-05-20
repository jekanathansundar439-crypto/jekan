# Leap Year Program using match
year = int(input("Enter a year: "))
match year:
    case year if (year % 400 == 0):
        print("It is a Leap Year")
    case _:
        print("It is Not a Leap Year")