# MODULE
# A Python module is a file containing Python code—including functions, classes, and variables—that
#          you can reuse across different programs. Any standard Python file ending in .py acts as a module.
# 👉Python-la module na oru .py file.
#          Andha file-kulla:Functions irukkalam,Classes irukkalam,Variables irukkalam,Vera Python code-um irukkalam
#          Indha file-la irukkura code-a namma multiple programs-la reuse panna mudiyum.

# three type of module
# The three primary types of modules in Python are categorized based on their origin and how they are integrated
#          into your environment.They are Built-in Modules, User-defined Modules, and External (Third-Party) Modules.
# 1. Built-in Modules
# Definition: Pre-installed modules that come bundled with the official Python distribution.
# Usage: You can import them directly without downloading external packages.
# Examples: The math module for calculations, os for operating system tasks, and random for generating random values.
# Sourcing: A full directory of these can be found in the Python Standard Library Documentation.
# 2. User-Defined Modules
# Definition: Custom modules created manually by developers to organize and reuse code across a project.
# Usage: Written as standard .py files containing functions, classes, or variables.
# Example: Saving a file as my_operations.py and referencing it in another file via import my_operations.
# 3. External (Third-Party) Modules
# Definition: Modules built by external developers that are not part of the core Python installation.
# Usage: Must be explicitly downloaded via package managers like the standard installer tool pip.
# Examples: Popular options include requests for HTTP requests, pandas for data analysis, 
#           and numpy for scientific computations.
# Sourcing: These libraries are hosted publicly on the Python Package Index (PyPI).

import random
#The Python random module is a built-in tool used to generate pseudo-random numbers for games, simulations, and testing
# 👉random module-ai import panrom. Idhu random values generate panna use aagum.

# random.random()
print(random.random())
# Generates a random floating-point number between 0.0 and 1.0.
# 👉0.0 to 1.0 kulla oru random float value generate pannum.

# random.randint(0, 10)
print(random.randint(0,10))
# Returns a random integer between 0 and 10 (both included).
# 👉0 lendhu 10 varaikkum oru random integer value return pannum.

# random.uniform(2, 15)
print(random.uniform(2,15))
# Returns a random floating-point number between 2 and 15.
# 👉2 lendhu 15 varaikkum oru random float value return pannum.

# random.choice(myList)
myList = [100,20,487,38,2390]
print(random.choice(myList))
# Selects and returns one random element from the list.
# 👉List-la irukkura elements-la edhavadhu oru element-ai random-aa select pannum.

# random.sample(myList, k=2)
print(random.sample(myList, k=2))
# Returns a new list containing 2 unique random elements from the original list.
# 👉Original list-la irundhu 2 unique random elements eduthu pudhu list-a return pannum.

# random.shuffle(myList)
random.shuffle(myList)
print(myList)
# Shuffles the elements of the list in random order.
# 👉List-oda order-ai random-aa mix pannum.

# The Python math module is a built-in library that provides access to essential mathematical functions and constants.
# Importing the Module
# You must import the module before accessing its contents: 
import math
# Or import with an alias
import math as m
              
# Core Mathematical Constants
# The module includes predefined floating-point constants:
# math.pi: Ratio of a circle's circumference to its diameter (π ≈ 3.14159).
# math.e: Euler's number (e ≈ 2.71828).
# math.tau: Full circle constant (τ = 2π ≈ 6.28318).
# math.inf: Floating-point positive infinity.
# math.nan: Floating-point "Not a Number" value.
                  
# Common Number Functions
# Function                Operation                            Example             Output
#  ceil(x)        Rounds up to the nearest integer.          math.ceil(4.2)          5
#  floor(x)       Rounds down to the nearest integer.        math.floor(4.8)         4
#  trunc(x)       Drops decimals to leave just the integer.  math.trunc(4.8)         4       
#  fabs(x)        Returns the absolute value as a float.     math.fabs(-5)           5.0
#  factorial(n)    Calculates the factorial                  math.factorial(5)       120
#                   of a positive integer.                   
#  gcd(*integers)  Finds the greatest common divisor.        math.gcd(24, 36)         12   

# Powers and Logarithms
# math.sqrt(x): Returns the square root of a number as a float.
# math.pow(x, y): Raises x to the power of y (x**y).
# math.log(x, [base]): Computes the logarithm of x. It defaults to the natural logarithm (base e) if 
#                      the base argument is left out.
# math.log10(x): Computes the base-10 logarithm.          