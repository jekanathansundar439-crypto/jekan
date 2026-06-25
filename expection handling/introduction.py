# Exception handling in Python allows you to gracefully manage runtime errors and prevent your program from crashing.
#        It is implemented using four primary keywords: try, except, else, and finally
# 👉Exception Handling na Python program run aagumbodhu varra errors-ah handle panna use pannuvanga. 
#   Idhu program crash aagama smooth-aa continue aaga help pannum.
# The Core Syntax Blocks
# try: Encloses the risky code that might throw an error.
# 👉Error varalaam nu nenaikkira code-ah try block-kulla ezhuthuvom.

# except: Catches and handles specific exceptions if they occur inside the try block.
# 👉try block-la error vandha adha catch panni handle pannum. 

# else: Executes code only if the try block runs without any errors.
# 👉try block-la endha error-um varala na mattum execute aagum.
#  
# finally: Executes always, regardless of whether an error occurred or was handled.
#          This is perfect for cleanup tasks like closing database connections or files.
# 👉Error vandhalum varalainalum kandippa execute aagum.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
finally:
    print("Program finished") 

# Common Python Errors & Fixes 
# SyntaxError: You broke Python's grammar rules(e.g., missing a colon :, unclosed brackets, or a typo). 
#              Check the end of the line pointed out by the error.
# def greet()
#    print("Hello")
# SyntaxError: expected ':'

# IndentationError: Your spacing is inconsistent. Python relies on spaces or tabs to group blocks of code;
#                   ensure your code aligns perfectly
# def greet():
# print("Hello")
# IndentationError: expected an indented block

# NameError: You tried to use a variable or function that hasn't been created or imported yet. Check your spelling.
# def show_name():
#    print(name)
# show_name()
# NameError: name 'name' is not defined

# TypeError: An operation was applied to an incompatible data type, like trying to add a string to a number ("2" + 2).
# def add(a, b):
#    return a + b
# add(10)
# TypeError: add() missing 1 required positional argument: 'b'

# ValueError: The data type is correct, but the actual value is inappropriate,
#             such as trying to turn the word "hello" into an integer (int("hello")
# def convert_to_int():
#    num = int("abc")
#    return num
# convert_to_int()
# ValueError: invalid literal for int() with base 10: 'abc'

# IndexError: You tried to access an item in a list using an index position that does not exist.
# def get_item():
#    numbers = [10, 20, 30]
#    return numbers[5]
# get_item()
# IndexError: list index out of range

# KeyError: You tried to access a specific key in a dictionary that isn't there
# def get_age():
#     student = {"name": "John"}
#    return student["age"]
# get_age()
# KeyError: 'age'