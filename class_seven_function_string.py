# class_seven_function_string.py
# Topic: Function + String Handling in Python
# Author: Razz
# Python Crash Course - Day 2 (Part 2)
# Date: November 04, 2025

"""
In this class, we will learn:
1️⃣ String Functions and Methods
2️⃣ Function with String Arguments
3️⃣ String Formatting (f-string)
4️⃣ Useful String Operations
5️⃣ Practice Tasks
"""

# ===============================
# 1️⃣ String Functions & Methods
# ===============================

text = "  Hello Python Learners!  "
print("Original Text:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Stripped:", text.strip())
print("Replace:", text.replace("Python", "World"))
print("Count 'l':", text.count("l"))
print("Starts with 'H':", text.strip().startswith("H"))
print("Ends with '!':", text.strip().endswith("!"))
print()


# ===============================
# 2️⃣ Function with String Argument
# ===============================

def greet_user(name):
    return f"Hello, {name}! Welcome to Python."

user_message = greet_user("Razz")
print(user_message)
print()

def word_count(sentence):
    words = sentence.split()
    return len(words)

print("Word count:", word_count("Python is an amazing programming language"))
print()


# ===============================
# 3️⃣ f-String Formatting
# ===============================

name = "Razz"
age = 24
language = "Python"

print(f"My name is {name}, I am {age} years old, and I love {language}.")
price = 49.9999
print(f"Price formatted: ${price:.2f}")
print()

# ===============================
# 4️⃣ Useful String Operations
# ===============================

text = "python programming"
print("Reversed String:", text[::-1])
print("Check if alphabetic:", text.isalpha())
print("Check if numeric:", "12345".isnumeric())
print("Join Example:", "-".join(["learn", "python", "fast"]))
print("Split Example:", "a,b,c".split(","))
print()


# ===============================
# 🧩 Practice Tasks
# ===============================
"""
1️⃣ Write a function that checks if a given string is palindrome.
2️⃣ Create a function that returns the number of vowels in a string.
3️⃣ Use f-string to format a sentence with user input.
4️⃣ Write a program to count each character's frequency using a dictionary.
5️⃣ Write a function to capitalize the first and last letter of each word.
"""

# End of class_seven_function_string.py
# 🚀 Keep Coding & Keep Learning!
# Rajib Sharker — November 04, 2025