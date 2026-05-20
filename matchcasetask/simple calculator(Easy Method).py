#simple calculator(Easy Method)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter + or - or * or / : ")
match choice:
    case "+":
        print("Answer =", a + b)
    case "-":
        print("Answer =", a - b)
    case "*":
        print("Answer =", a * b)
    case "/":
        print("Answer =", a / b)
    case _:
        print("Invalid choice")