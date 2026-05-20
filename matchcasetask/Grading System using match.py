# Grading System using match
marks = int(input("Enter your marks: "))
match marks:
    case mark if mark >= 90:
        print("Grade: A")
    case mark if mark >= 75:
        print("Grade: B")
    case mark if mark >= 60:
        print("Grade: C")
    case mark if mark >= 40:
        print("Grade: D")
    case _:
        print("Grade: Fail")