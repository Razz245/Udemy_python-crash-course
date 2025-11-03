# class_eleven_tuples.py
# Topic: Tuples — Creation, Indexing, Slicing
# Author: Razz
# Python Crash Course - Day 3 (Part 3)
# Date: November 06, 2025

"""
In this class, we will learn:
1️⃣ Creating Tuples
2️⃣ Accessing Elements (Indexing)
3️⃣ Slicing Tuples
4️⃣ Tuple Immutability
5️⃣ Useful Tuple Functions
6️⃣ Nested Tuples
"""

# ===============================
# 1️⃣ Creating Tuples
# ===============================
numbers = (10, 20, 30, 40, 50)
fruits = ("Apple", "Banana", "Cherry", "Date")
mixed = (1, "Python", 3.14, True)

print("Numbers Tuple:", numbers)
print("Fruits Tuple:", fruits)
print("Mixed Tuple:", mixed)
print("Type of fruits:", type(fruits))
print()


# ===============================
# 2️⃣ Indexing
# ===============================
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second number:", numbers[1])
print("Second last number:", numbers[-2])
print()


# ===============================
# 4️⃣ Tuple Immutability
# ===============================
# Tuples cannot be changed directly
try:
    fruits[0] = "Mango"
except TypeError:
    print("❌ Error: Tuples are immutable, cannot modify elements directly.")
print()

# ===============================
# 5️⃣ Useful Tuple Functions
# ===============================
numbers2 = (10, 20, 30, 10, 40, 10)
print("Count of 10:", numbers2.count(10))
print("Index of 30:", numbers2.index(30))
print("Length of tuple:", len(numbers2))
print("Max number:", max(numbers))
print("Min number:", min(numbers))
print("Sum of numbers:", sum(numbers))
print()

# ===============================
# 6️⃣ Nested Tuples
# ===============================
nested = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested)
print("First sub-tuple:", nested[0])
print("Second element of first sub-tuple:", nested[0][1])
print()


# ===============================
# 🧩 Practice Tasks
# ===============================
"""
1️⃣ Create a tuple of your favorite programming languages and access elements using index.
2️⃣ Try modifying a tuple and observe the TypeError.
3️⃣ Write a program to count occurrences of a number in a tuple.
4️⃣ Slice a tuple to get a sub-tuple.
5️⃣ Create a nested tuple and access inner elements.
"""

# End of class_eleven_tuples.py
# 🚀 Keep Learning — Keep Coding!
# Rajib Sharker — November 06, 2025