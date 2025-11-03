# class_six_functions.py
# Topic: Python Functions (Basic to Advanced)
# Author: Razz
# Python Crash Course - Day 2 (Part 1)
# Date: November 04, 2025

"""
In this class, we will learn:
1️⃣ What is a Function
2️⃣ Defining and Calling Functions
3️⃣ Function Parameters & Arguments
4️⃣ Return Statement
5️⃣ Default & Keyword Arguments
6️⃣ *args and **kwargs
7️⃣ Lambda Functions
8️⃣ Recursion
"""

# ===============================
# 1️⃣ What is a Function
# ===============================
# A function is a reusable block of code that performs a specific task.

def greet():
    print("Hello, Python Learner!")

# Function call
greet()
print()


# ===============================
# 2️⃣ Function with Parameters
# ===============================
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 10)
print()


# ===============================
# 3️⃣ Return Statement
# ===============================
def multiply(a, b):
    return a * b

result = multiply(6, 7)
print("Multiplication Result:", result)
print()

# ===============================
# 4️⃣ Default Arguments
# ===============================
def power(base, exp=2):
    return base ** exp

print("Square of 5:", power(5))
print("Cube of 3:", power(3, 3))
print()


# ===============================
# 5️⃣ Keyword Arguments
# ===============================
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info(age=22, name="Razz", course="Python Crash Course")
print()

# ===============================
# 6️⃣ *args and **kwargs
# ===============================
def show_args(*args):
    print("Positional arguments:", args)

def show_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)

show_args(10, 20, 30)
show_kwargs(name="Razz", country="Bangladesh", skill="Python")
print()


# ===============================
# 7️⃣ Lambda Functions
# ===============================
# Anonymous one-line function
square = lambda x: x * x
add = lambda a, b: a + b

print("Square using lambda:", square(4))
print("Addition using lambda:", add(5, 7))
print()


# ===============================
# 8️⃣ Recursive Function
# ===============================
def factorial(n):
    """Return factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print()

# ===============================
# 🧩 Practice Tasks
# ===============================
"""
1️⃣ Create a function to check whether a number is even or odd.
2️⃣ Write a function that takes a list of numbers and returns their sum.
3️⃣ Create a recursive function to calculate Fibonacci numbers.
4️⃣ Use lambda to sort a list of tuples by the second value.
5️⃣ Combine *args and **kwargs in one function and print all.
"""

# End of class_six_functions.py
# 🚀 Keep Coding & Keep Learning!
# Rajib Sharker — November 04, 2025



