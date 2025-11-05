# class_sixteen_modules_libraries.py
# Topic: Modules and Libraries in Python (Basic to Advanced)
# Author: Razz
# Python Crash Course - Day 3 (Part 1)

"""
In this class, we will learn:
1️⃣ What is a Module
2️⃣ Importing Built-in Modules
3️⃣ Using External Libraries
4️⃣ Creating Custom Modules
5️⃣ The 'from ... import ...' syntax
6️⃣ pip install and requirements.txt
"""


# ===============================
# 📦 1. WHAT IS A MODULE?
# ===============================
# ➤ A module is a file containing Python definitions and statements.
# ➤ It helps you organize your code logically and reuse it easily.

# Example: Using built-in module 'math'
import math

print("Square root of 25:", math.sqrt(25))
print("Power 2^3:", math.pow(2, 3))
print("Pi value:", math.pi)
print("Factorial of 5:", math.factorial(5))
print()


# ===============================
# ⏰ 2. DATETIME MODULE
# ===============================
import datetime

today = datetime.date.today()
print("Today's Date:", today)
print("Current Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

now = datetime.datetime.now()
print("Current Time:", now.strftime("%H:%M:%S"))
print()

# ===============================
# 🧠 3. OS & SYS MODULES
# ===============================
import os
import sys

print("Current Working Directory:", os.getcwd())
print("Python Executable Path:", sys.executable)
print("Python Version:", sys.version)
print()

# Create and list files
os.system("touch test_file.txt")
print("Files in current directory:", os.listdir("."))


# ===============================
# 🌐 4. JSON MODULE
# ===============================
import json

student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

# Convert Python dict → JSON string
json_data = json.dumps(student)
print("\nJSON String:", json_data)

# Convert JSON string → Python dict
python_data = json.loads(json_data)
print("Back to Python dict:", python_data)
print()

# ===============================
# 📚 5. EXTERNAL LIBRARIES (Install using pip)
# ===============================
# To install:
#   pip install requests

# Example: Using 'requests' to fetch a webpage
try:
    import requests
    response = requests.get("https://api.github.com")
    print("GitHub API Status Code:", response.status_code)
    print("Response Headers:", response.headers)
except ModuleNotFoundError:
    print("⚠️ Please install requests: pip install requests")
print()


# ===============================
# 🧩 6. CREATING CUSTOM MODULE
# ===============================
# Suppose we create a file: mymodule.py
# Content of mymodule.py:
"""
def greet(name):
    return f"Hello, {name}! Welcome to Python Modules."
"""

# Now, we can import and use it like:
# import mymodule
# print(mymodule.greet("Razz"))

print("✅ Custom module example explained (see comments).")
print()


# ===============================
# 📄 7. REQUIREMENTS.TXT
# ===============================
# ➤ Use `pip freeze > requirements.txt` to save all installed packages.
# ➤ Use `pip install -r requirements.txt` to install them later.

print("✅ Use requirements.txt to share project dependencies.")
print()


# ===============================
# 🧩 PRACTICE TASKS
# ===============================
"""
1️⃣ Import math and find the area of a circle using math.pi
2️⃣ Get current date & time using datetime
3️⃣ Use os module to create a new folder named 'data'
4️⃣ Convert a Python dictionary to JSON and back
5️⃣ Try using requests to fetch a website status code
6️⃣ Create your own custom module with a simple function
"""

# End of class_sixteen_modules_libraries.py
## Happy Coding! 🚀
# Rajib Sharker — November 2025