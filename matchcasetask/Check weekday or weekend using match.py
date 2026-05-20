# Check weekday or weekend using match
day = input("Enter a day: ")
match day:
    case "saturday" | "sunday":
        print("It is a Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It is a Weekday")
    case _:
        print("Invalid day name")