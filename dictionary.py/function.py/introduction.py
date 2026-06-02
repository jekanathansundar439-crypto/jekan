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

# SCOPE
# scope refers to the specific region of a program where a variable or name is accessible.
# Python resolves names using the LEGB rule
# L: Local – Names defined inside the current function or lambda expression.
# E: Enclosing (Non-local) – Names in the local scope of any enclosing functions (relevant for nested functions).
# G: Global – Names defined at the top level of a script or module, or declared with the global keyword.
# B: Built-in – Special names pre-loaded by Python (like print, len, and range)
# Key Scope Types
# Local Scope: A variable created inside a function belongs to that function's local scope and cannot be used outside it.
def my_function():
    local_var = "I am local!"
    print(local_var) 

# Global Scope: A variable created in the main body of a Python script is global.
#      It is accessible from anywhere within that file.
global_var = "I am global!"

def read_global():
    print(global_var)  
read_global()
print(global_var)

# Enclosing (Non-local) Scope: Used in nested functions.
#     An inner function can access variables from its outer (enclosing) function.
def outer_function():
    enclosing_var = "I am enclosing!"
    
    def inner_function():
        print(enclosing_var)  
    inner_function()

outer_function()

# abs() Function
# abs() means absolute value.It converts a negative number into a positive number.Positive numbers stay the same.
# 👉abs() function use pannina negative number positive ah maarum.-10 → 10 ah convert aaguthu.
#             Positive number irundha same ah irukkum.
print(abs(-10))

# round() Function
# round() rounds the decimal number to the nearest whole number.5.6 becomes 6.
# 👉round() decimal value ah nearest whole number ku convert pannum.5.6 → 6, 5.4 na 5 varum.
print(round(5.6))

# min() Function
# min() finds the smallest value.
# 👉min() function smallest value ah kandupidikkum.3,6,1,8 la smallest number 1.
print(min(3,6,1,8))

# max() Function
# max() finds the largest value.
# 👉max() function biggest value ah return pannum.3,6,1,8 la biggest number 8. 
print(max(3,6,1,8))

# sum() Function
# sum() adds all numbers in a list.
# 👉sum() list la irukka numbers ellam add pannum.10 + 20 + 30 = 60
print(sum([10,20,30]))

# sorted() Function
# sorted() arranges values in ascending order.
# 👉sorted() values ah small to big order la arrange pannum.1,3,6,8 nu order aagum.
print(sorted([3,6,1,8]))

# reversed() Function
# reversed() reverses the list items.
# 👉reversed() list ah reverse pannum.Last item first ku வரும்.
listData = [3,6,1,8]
data = reversed(listData)
print(list(data))

# all() Function
# all() returns True only if all values are True.
# 👉all() la ellame True irundha dhan True return pannum.Oru value False na output False.
print(all([True, True]))

# any() Function
# any() returns True if at least one value is True.
# 👉any() la atleast oru value True irundha podhum.Appo output True.
print(any([False, True]))

# map() Function
# map() applies a function to every item in a list.Here, 2 is added to every number.
# 👉map() function list la irukka every item ku same operation apply pannum.Inga every number kooda 2 add aaguthu. 
myList = [1,2,3,4]
def addNumber(x):
    return x + 2
mappedData = map(addNumber, myList)
print(list(mappedData))

# map() with Lambda
# lambda is a short anonymous function.Each number is multiplied by 2.
# 👉lambda small shortcut function.Every number um 2 nala multiply aaguthu. 
nums = [1, 2, 3, 4]
result = map(lambda x: x * 2, nums)
print(list(result))

# map() with Two Lists
# map() can work with multiple lists.It adds items position by position.
# 👉Rendu list values same position la add aagum.1+4, 2+5, 3+6
a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))

# filter() Function
# filter() selects values based on a condition.Only values greater than or equal to 450 are selected.
# 👉filter() condition satisfy panna values mattum edukkum.450 ku mela irukka values mattum return aagum.
total = [360,470,260,455,500,450]
filteredData = filter(lambda x : x >= 450, total)
print(list(filteredData)) 

# filter() using Normal Function
# Same filtering process using a normal function.
# 👉Inga lambda use pannaama normal function use pannirukom.Condition same dhan.
def getData(n):
    return n >= 450
dataFilter = filter(getData,total)
print(list(dataFilter))

# reduce() Function
# reduce() combines all values into a single value.Here it adds all prices together.
# 👉reduce() list la irukka values ellam one by one combine pannum.Inga total addition nadakkuthu.
price = [1000,5000,7500,3700,8500]
result = reduce(lambda a,b : a + b, price )
print(result) 

# reduce() with Initial Value
# 10 is the starting value.Calculation starts from 10.
# 👉Inga 10 initial value ah use pannirukom.Addition 10 la start aaguthu. 
nums = [1, 2, 3]
result = reduce(lambda x, y: x + y, nums, 10)
print(result)
