# class_eight_scope_variable.py
# Topic: Scope of Variables in Python
# Author: Razz
# Python Crash Course - Day 2 (Part 3)
# Date: November 05, 2025

"""
In this class, we will learn:
1️⃣ What is Variable Scope
2️⃣ Types of Scope (LEGB Rule)
3️⃣ Local & Global Variables
4️⃣ Enclosed Scope (Nested Functions)
5️⃣ Global Keyword
6️⃣ Nonlocal Keyword
7️⃣ Practice Examples
"""
# ===============================
# 1️⃣ What is Variable Scope?
# ===============================
"""
Scope defines the part of the program where a variable is accessible.
Python follows the LEGB rule:
L = Local
E = Enclosed
G = Global
B = Built-in
"""

# ===============================
# 2️⃣ Global Scope
# ===============================
x = 10  # Global variable

def show_global():
    print("Global x:", x)

show_global()
print("Accessing global x outside function:", x)
print()


# ===============================
# 3️⃣ Local Scope
# ===============================
def local_example():
    y = 20  # Local variable
    print("Inside function (local y):", y)

local_example()
# print(y)  # ❌ This would cause an error (y not defined outside)
print()


# ===============================
# 4️⃣ Enclosed Scope (Nested Functions)
# ===============================
def outer_function():
    name = "Outer"

    def inner_function():
        print("Accessing enclosed variable:", name)

    inner_function()

outer_function()
print()


## ===============================
# 5️⃣ Global Keyword
# ===============================
counter = 0

def increment():
    global counter
    counter += 1
    print("Counter inside function:", counter)

increment()
increment()
print("Counter outside function:", counter)
print()

# ===============================
# 6️⃣ Nonlocal Keyword
# ===============================
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print("Count inside inner:", count)
    inner()
    inner()

outer()
print()

# ===============================
# 7️⃣ Built-in Scope
# ===============================
# Python has built-in names like len(), sum(), print(), etc.
print("Example of Built-in function:", len([10, 20, 30]))
print()


# ===============================
# 🧩 Practice Tasks
# ===============================
"""
1️⃣ Write a program that uses both global and local variables.
2️⃣ Create a nested function that modifies the variable using 'nonlocal'.
3️⃣ Demonstrate what happens if you use a variable before declaring it global.
4️⃣ Write a function to show LEGB order in action.
"""

# End of class_eight_scope_variable.py
# 🚀 Keep Coding & Keep Learning!
# Rajib Sharker — November 05, 2025