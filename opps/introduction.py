# OPPS  
# Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects,
#     which represent real-world entities containing data and behavior.
# 👉Object-Oriented Programming (OOP) na oru programming method. Idhula software-a objects nu sollra units-a use 
#   panni design pannuvanga.Indha objects real-world la irukkura vishayangalai (entities) represent pannum. 
# ----------------------------------------------------------------------------------------------------------------------
# The Foundation: Classes and Objects
# Class: A user-defined blueprint or template that defines the properties
#        (data variables) and behaviors (methods) of what you want to create.
# 👉Class na, objects create panna use aagura blueprint/template; adhu object oda data-um methods-um define pannum.

# Object: A specific instance created from a class blueprint that contains actual data and executes code.
# 👉Object na, oru class blueprint-ai use panni uruvakkappatta real entity. Adhula actual data irukkum, 
# mela class-la define pannirukka functions-ai use panna mudiyum.
# -----------------------------------------------------------------------------------------------------------------------
# The Four Pillars of OOPs
# Encapsulation (Data Hiding):
#  Definition: Wrapping data (attributes) and methods (functions) together into a single 
#              unit (a class) while restricting direct outside access.
#  👉Encapsulation na, data (variables) um methods (functions) um orae class-kulla serthu vechitu, 
#    andha data-va veliya irundhu direct-a access panna mudiyama protect pannuradhu.  
#  Mechanism: Handled via access specifiers like private, protected, and public.
#  Access: External code can only interact with private data through controlled public 
#          methods known as getters and setters.
#  Analogy: A capsule or pill. The internal chemical formula is safely 
#           sealed away; you only interact with the pill by swallowing it.

# Abstraction (Hiding Complexity):
#  Definition: Displaying only the essential, relevant features of an object while hiding the complex 
#              background or implementation details.
#  👉Important features-a mattum show panni, implementation details-a hide pannuradhu Abstraction.
#  Mechanism: Achieved using abstract classes and interfaces.
#  Analogy: Driving a car. You only need to know how to use the steering wheel, accelerator, and brakes.
#           You do not need to understand how the internal combustion engine operates under the hood

# Inheritance (Code Reuse)
#  Definition: A mechanism where a new class (subclass/child) inherits the attributes and behaviors
#              of an existing class (superclass/parent).
#  👉Parent class-oda properties and methods-a child class inherit pannuradhu Inheritance.
#  Relationship: Establishes a natural "is-a" relationship (e.g., a Car is a Vehicle).
#  Benefit: Greatly reduces code redundancy and promotes the DRY (Don't Repeat Yourself) principle.
# -----------------------------------------------------------------------------------------------------------------------
# Single Inheritance
# A single child class inherits directly from exactly one parent class. 
# 👉Oru child class, ore oru parent class-kitta mattum inherit pannuvadhu Single Inheritance. 
# Structure: Class A ➔ Class B

# Multilevel Inheritance
# A child class inherits from a parent class, which itself acts as a child class to a grandparent class .
# 👉Multilevel Inheritance na, oru class inherit pannina class-a marubadiyum vera oru class inherit pannum.
# Structure: Class A ➔ Class B ➔ Class C

# Hierarchical Inheritance
# Multiple child classes inherit their properties from the exact same single parent class.
#👉Ore oru parent class-lendhu pala child classes inherit pannuvadhu Hierarchical Inheritance.
# Structure: Class A ➔ Class B AND Class A ➔ Class C

# Multiple Inheritance
# A single child class inherits properties and behaviors from more than one parent class.
# 👉Multiple Inheritance na, oru child class rendu illa athuku mela parent classes-la irundhu inherit pannuradhu.
# Structure: Class A + Class B ➔ Class C
# -----------------------------------------------------------------------------------------------------------------------
# single inheritance
class vehicle:
    def start(self):
        print("start is working")

class car(vehicle):
    def drive(self):
        print("drive is working")

objDog = car()
objDog.drive()
# -----------------------------------------------------------------------------------------------------------------------
# multiple inhertance
class Vehicle:
    def drive(self):
        print("drive is working")

class Engine:
    def start(self):
        print("start is working")

class Car(Vehicle, Engine):
    def run(self):
        print("run is working")

objCar = Car()
objCar.run() 
# -----------------------------------------------------------------------------------------------------------------------
# Hierarchical Inheritance
class Vehicle:
    def drive(self):
        print("drive is working")

class Car(Vehicle):
    def ac(self):
        print("ac is working")

class Bike(Vehicle):
    def kick(self):
        print("kick start is working")

objCar = Car()
objCar.ac()
# -----------------------------------------------------------------------------------------------------------------------
# Multilevel Inheritance
class Vehicle:
    def drive(self):
        print("Drive is working")

class Car(Vehicle):
    def start(self):
        print("Start is working")

class SportsCar(Car):
    def race(self):
        print("Race is working")

obj = SportsCar()
obj.race()    
# -----------------------------------------------------------------------------------------------------------------------
