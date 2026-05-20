#odd or even with match
num = int(input("enter your num:"))
match num:
    case num if  num % 2 == 0:  
        print(" it's even!")
    case num :
        print(" but it's not even.")
    