# Defining and Calling a Function
# To define a function, use the def keyword followed by the function name, parentheses, and a colon.
# 👉 Function create panna def keyword use panni, adhuku apram function name, brackets () and colon : podanum.
# Key Components
# Parameters & Arguments: Parameters are placeholders defined in the function header, 
#    while arguments are the actual data passed into the function when called.
# 👉Parameters na function create pannum pothu use panna variables, 
#       arguments na function call pannum pothu kudukkura real values.
# Return Statement: Use the return keyword to send a result back to the caller. 
#     If no return is specified, the function returns None by default.
# 👉result-ah thirupi anuppa return keyword use pannuvom. 
# Indentation: Unlike many other languages, Python uses indentation (typically 4 spaces)
#     to define the block of code belonging to a function.
# 👉Python la function-ku belong aana code-ah define panna proper spacing (usually 4 spaces) use pannuvanga.  
# Types of Arguments
# Python offers flexible ways to pass data into functions:
# Positional: Matched based on their order.
# 👉Values order base panni match aagum.
# Keyword: Passed using the parameter name (e.g., greet(name="Alice")), allowing them to be in any order.
# 👉Parameter name use panni value pass pannalam, order important illa. 
# Default: Predefined values used if no argument is provided (e.g., def greet(name="User"):).
# 👉Value kudukkalana already set panna default value use aagum.  
# Arbitrary (*args, **kwargs): Used when the number of arguments is unknown beforehand.
# 👉Evlo arguments varumnu theriyadha time la *args and **kwargs use pannuvom 

a= input("enter the name:")
b= input("enter the gmail:")
def jd(name,gmail):
    print("its your name:",name)
    print("its is your gmail:",gmail)
jd(a , b)

# RETURN
# The return statement in Python is used inside a function (defined with def) to send a result back to the caller
#       and exit the function immediately.The return statement in Python is used inside a function (defined with def)
#       to send a result back to the caller and exit the function immediately.
# 👉return keyword use pannradhu function-la irundhu result-ah veliya anuppa use pannuvom.
# 👉Simple-ah sonna 👇
# 👉 Function work mudichitu oru value back kudukkum.
# 👉 Athukapparam function immediately stop aagidum.
def add(a, b):
    return a + b

print(add(2, 3))

# Arbitrary Arguments (*args)
# The *args parameter captures extra positional arguments into a single tuple inside the function.
# 👉*args use pannradhu function-ku எத்தனை arguments வரும் nu தெரியாத போது use pannuvom.
# 👉Simple-ah sonna 👇
# 👉 Multiple values-ah receive panna use pannuvom.
# 👉 Ella values-um tuple format-la store aagum.  
def myNumber(*nums):
    print(nums)
    
myNumber(10,20,30,40,50,60)

# Arbitrary Keyword Arguments (**kwargs)
# The **kwargs parameter captures extra keyword arguments into a single dictionary inside the function.
# 👉**kwargs use pannradhu function-ku எத்தனை keyword arguments வரும் nu தெரியாத போது use pannuvom.
# 👉Simple-ah sonna 👇
# 👉 Key-value format-la வரும் multiple data-ah receive panna use pannuvom.
# 👉 Ella data-um dictionary format-la store aagum.
def userData(**myData):
    print(myData)

userData(firstName = "aaa", lastName= "bbb")

# Default Parameters
# A default parameter assigns a fallback value in the function definition using the assignment operator (=).
# 👉Default parameter na function definition-la already oru value assign pannirupom.
# 👉Simple-ah sonna 👇
# 👉 User value kudukkalana default value use aagum.
# 👉 Value kudutha default value replace aagidum.
def defaultParams(a,b,c = 50):
    print(a + b + c)
    
defaultParams(5,10,6)
