# arithemetic operator(+,-,*,\,%,\\,**)
# assignment operator (+,=+,=-,*=,\=)
# comparison operator (==,!=,<,>,<=,>=)("its all way return the boolean value")
# logical operator    (and,or,not)
# bitwise operator    (&,|,^,~,<<,>>)(&-AND,|-OR,^-XOR,~-NOT,<<-left shift,>>-right shift)
# membership operator (in,not in)
# indentity operator  (is,is not,)

#         (AND,OR,NOT)Truth table
# A       B       A AND B       A OR B
# True    True    True          True
# True    False   False         True
# False   True    False         True
# False   False   False         False
# A       NOT A
# True    False
# False   True

# MEMBERSHIP AND INDENTITY OPERATOR(in,not in;is.is not)
# "The "in" operator returns True if the given element exists inside a sequence, otherwise it returns False."
# "The "not in" operator works the opposite of "in" operator, it returns True if the element is not found in a sequence."
# "The "is" operator checks if two variables point to the same object (same memory location)."
# "The "is not" operator checks if two variables point to different objects."
# They are mainly used to test whether a value exists within a sequence or whether two variables refer to same object in memory.
# *The equality operator (==) is used to compare value of two variables,
# *whereas identity operator (is) is used to compare memory location of two variables.

# BITWISE OPERATOR
# AND-Sets each bit to 1 if both bits are 1
# OR-Sets each bit to 1 if one of two bits is 1
# XOR-Sets each bit to 1 if only one of two bits is 1
# NOT-Inverts all the bits
# LEFT SHIFT-Shift left by pushing zeros in from the right and let the leftmost bits fall off
# RIGHT SHIFT-Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#                  XOR truth table
# A       B       A XOR B
# True    True    False
# True    False   True
# False   True    True
# False   False   False


print("task-1")
a=True
b=False
c=False
d=True
print("comparison operator")
print( a == b )
print( a != b)
print( b != c)
print( a != d)
print( b > c)
print( c < d)
print( a >= d)
print( c <= b)
print( a == d)
print(b == c)
print( a and b)
print("logical operator")
print( a or b )
print( not (a and c) )
print( not (b or d) )
print( a and (b or c))
print( (a or b) and (c or d) )
print(  not (a and d)) 
print( (b and c) or (a and d))
print( a or (b and d))
print((a and b) or (c and d))
print("logical and comparsion")
print((a and b) or (not (c or d) and (a == b)))
print(((a or b) and (c == d)) or (not (a == c)))
print(((a == b or c < d) and (a != d or b > c)))
print((a and (b or c)) and not (d or (b and c)))
print((a and b and c) or not (d and (a == b)))
print(not (a or (b and c) or (d == True)) and (a or b))
print((a == d or (b and c) and not (a != b)) or (c <= d))
print(((a and b) or (c > d)) and not (a == c) and (b!= c))
print(((a and b) or (c == d)) and not (a != d) and (c < b) )
print((a or (b and not c) or (d == True)) and not (a == b and c != d))
print(not (a and b) or (c < d and (b == False or d == True)))
print(not (a or b) and (c <= d or not (a == b)) and (c == b))
print((a and (b or c)) or not (a == b) and (c != d)) 
print((a == True and b == False) or not (c == d) and (a or d))
print(((a == b) or not (c <= d)) and ((b or c) and (a != d)))
print((a or (b and (c <= d))) or not (a == c and d != True))
print(not (a and (b or (c and d))) or (c == b and (a == d)))
print((a and (b == False or c == True)) and not (d and b))
print( (a or (b and (c or d))) and not (a == c or b != d))
print((a and b) or (c and d)) and not (a == c and b != d) or (a == d)
print(not (a and b) and (c != d) or (a == b and not (c == d)))
print(((a or b) and (c == True)) or (a == d and not (c != b)))
print(((a and b) or not (c == True)) and (a == b or (c < d)))
print((a or (b and not (c == d))) and (a != d or not (b == False)))
print(((a == d and not (b and c)) or (a != c and b == True)) and (c != d))
print(((a or (b and c)) and d == True) or not (a == c))
print((a and not (b or c) and (d == True)) or not (a and b))
print(((a and b) or ((c == True) and (d != False))) and not (a == b))
print((a == b and not (c and d)) or (a != d and c == b))
print(((a== b and c != d) or not (a and c)) and (a or (b and d)))
print("task-2")
print("membership and indentity operator")
print(1)
x = [10, 20, 30]
y = [10, 20, 30]
print(x==y)
print(x in y)
print(20 in x and 48 not in y)
print (2)
a="hello"
b="he"+"llo"
print(a is b)
print(a== b)
print(3)
a=[1, 2, 3]
b=a
c = a * 1
a = a + [4]
print(b is c)
print(c is a)
print(2 in c)


