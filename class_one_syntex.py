"""Topic : One----Print, Variables, Input, Type Casting"""

#Print Statement
print("Hello, World!")
print("Welcome to Python Programming")
print("This is a sample code.")
print("Enjoy coding!")
print(10+5)

name = "Alice"
age = 30
print("Name:", name, "| Age:", age)




"""Topic ---Two: Variables, Data Types, and Indentation"""


#Correct Identation
if 5>3:
    print("True")
else:
    print("False")
    
#Variables and Data Types
# Integer
age = 25
print("Age:", age)

# Float
price = 19.99
print("Price:", price)

# String
name = "John"
print("Name:", name)

# Boolean
is_student = True
print("Is Student:", is_student)


"""Topic ---Three: Input Function and Type Casting"""

name = input("Enter your name: ")
print("Welcome,", name)
age = int(input("Enter your age: "))
print("You are", age, "years old.")
school = input("Enter your school name: ")
print("School:", school)
height = float(input("Enter your height in meters: "))
print("Height:", height, "meters")
blood_group = input("Enter your blood group: ")
print("Blood Group:", blood_group)
your_address = input("Enter your address: ")
print("Address:", your_address)


"""Type Casting Examples"""


x = "100"
y = int(x)  # Convert string to integer
print(y+50)


a = int(input("Enter a number: "))
b = float(input("Enter another number: "))
print("Sum is:", a + b)


x = 10
print(type(x))   # <class 'int'>

y = "Hello"
print(type(y))   # <class 'str'>

#Improvement Tips
#Input Section — Optional Type Hints
age = int(input("Enter your age (in years): "))
height = float(input("Enter your height (in meters): "))


#Type Casting Demonstration
num = 25
print(str(num))   # Convert int → string

pi = 3.1416
print(int(pi))    # Convert float → int (decimal part lost)

#Data Type Checking
value = input("Enter something: ")
print("Value:", value, "| Type:", type(value))

#Bonus Suggestion – Section Separation
def print_examples():
    print("Hello, World!")
    print("Enjoy coding!")

def variable_examples():
    age = 25
    name = "John"
    print("Name:", name, "| Age:", age)

#Optional Practice Idea
print(f"Hi {name}, you are {age} years old, {height}m tall, and your blood group is {blood_group}.")
print_examples()
print_variable_examples()
