#*positive, negative, or zero*
num=int(input("enter your number:"))
match num:
    case num if num > 0:
        print("its is positive")
    case num if num < 0:
        print("its is negative")
    case _ :
        print("its is zero")