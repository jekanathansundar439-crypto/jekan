#conditional statement
#if-👉 “If this condition is true, then do something.”
#if syntax:
#if condition:
    # code runs if condition is True
#else-else runs when the condition is False.
#else syntax
#else:
    # runs if all above conditions are False
#elif-Used to check multiple conditions.
#elif syntax
#elif condition2:
    # runs if condition1 is False AND condition2 is True
print("even or odd")#1
num = int(input("enter your number:"))
if(num % 2 == 0 ):
    print("its is even num")
else:
    print("its is odd num")
print("positive or negative")#2
if(num>=0):
    print("its is postive")
else:
    print("its is negative")
print("eligible for vote")#3
if(num>=18):
    print("you are eligible for vote")
else:
    print("you are not eligible")
print("Pass or fail")#6
if(num>=35):
    print("pass")
else:
    print("fail")
print("divisible by 5")#5
if(num%5==0):
    print("its is divisible")
else:
    print("its is not divisible")
print("divisible by 10")#8
if(num%10):
    print("its is divisible")
else:
    print("its not divisible")
print("greater than 100")#9
if(num>100):
    print("its is greater")
else:
    print("its not greater")
print("number less than 5")#13
if(num<5):
    print("its is less")
else:
    print("its is not less")
print("check its it is two digit num")#7
if(10<=(num)<=99):
    print("its is two digit num")
else:
     print("It is not a two-digit number")
print(" number divisible by 2 and 3")#11
if(num % 2 == 0 and num % 3 == 0):
    print("The number is divisible by both 2 and 3")
else:
    print("The number is NOT divisible by both 2 and 3")
print("number is zero or non-zero")#12
if num == 0:
    print("The number is zero")
else:
    print("The number is non-zero")

print("----------------------------------------------------------------------------------------------------------------------")
print("number is positive, negative, or zero.")#1
if(num > 0 ):
    print("its is postive")
elif(num < 0):
    print("its is negative")
else:
    print("The number is zero.")
print("largest of three numbers using if-elif-else.")#2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
print("year is a leap year.")#3
year = int(input("Enter a year: "))
if(year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
print("assign grades based on marks (e.g., A, B, C, Fail).")#6
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
