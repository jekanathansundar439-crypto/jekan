#✅ Match Case Definition in Python
# match case is a feature in Python used to compare a value with different patterns and execute matching code blocks.
# It works similar to switch-case in other programming languages.
# match variable:
#   case value1:
        # code block
#  case value2:
        # code block
#   case _:
        # default block
isPass = input("Enter your result status")
match (bool(isPass)):
    case True:
        print("Pass")
    case False:
        print("Fail")
    case _ :
        print("Default is working")


userName = input("Enter your name")

match(userName):
    case "aaa":
        print(f"You entered {userName}")
    case "demo":
        print(f"You entered {userName}")
    case _ :
        print(f"You entered wrong name {userName}")


x = int(input("Enter x value : "))
match x:
    case 10 if x % 2 == 0:  # Match 10 only if it's even
        print("Matched 10 and it's even!")
    case 10:
        print("Matched 10, but it's not even.")
    case _:
        print("No match found")