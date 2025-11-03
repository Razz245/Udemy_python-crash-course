# class_nine_list_methods.py
# Topic: Lists — Creation, Indexing, Slicing & Methods
# Author: Razz
# Python Crash Course - Day 3 (Part 1)
# Date: November 06, 2025

"""
In this class, we will learn:
1️⃣ Creating Lists
2️⃣ Accessing Elements (Indexing)
3️⃣ Slicing Lists
4️⃣ Updating Lists
5️⃣ Common List Methods
6️⃣ Iterating through Lists
7️⃣ Nested Lists
"""
# ===============================
# 1️⃣ Creating Lists
# ===============================

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = ['hello', 42, 3.14, True]
print("Fruits List:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed)
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
# 3️⃣ Slicing
# ===============================
print("Fruits (1 to 3):", fruits[1:3])
print("Numbers (0 to 4, step 2):", numbers[0:5:2])
print("Reverse Fruits:", fruits[::-1])
print()

# ===============================
# 4️⃣ Updating Lists
# ===============================
fruits[0] = "Mango"
print("After updating first fruit:", fruits)
fruits[1:3] = ["Orange", "Papaya"]
print("After slice update:", fruits)
print()

# ===============================
# 5️⃣ Common List Methods
# ===============================
fruits.append("Kiwi")  # Add one item
print("After append:", fruits)

fruits.insert(2, "Grapes")  # Insert at position
print("After insert at index 2:", fruits)

fruits.remove("Papaya")  # Remove by value
print("After remove Papaya:", fruits)

popped_item = fruits.pop()  # Remove last item
print("Popped item:", popped_item)
print("After pop:", fruits)

fruits.sort()  # Sort alphabetically
print("Sorted list:", fruits)

fruits.reverse()  # Reverse order
print("Reversed list:", fruits)

print("Index of Mango:", fruits.index("Mango"))
print("Count of Mango:", fruits.count("Mango"))
print()


# ===============================
# 6️⃣ Iterating through Lists
# ===============================
print("Looping through fruits:")
for fruit in fruits:
    print("-", fruit)
print()

# Using enumerate()
print("Using enumerate():")
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
print()

# ===============================
# 7️⃣ Nested Lists
# ===============================
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested)
print("First list inside nested:", nested[0])
print("Second element of first sublist:", nested[0][1])
print()

# Modifying nested list
nested[1][0] = 9
print("After modification:", nested)
print()

# ===============================
# 🧩 Practice Tasks
# ===============================
"""
1️⃣ Create a list of 5 favorite movies and perform all major list operations.
2️⃣ Write a Python program to find the largest number in a list.
3️⃣ Reverse a list without using reverse() method.
4️⃣ Count occurrences of an element in a list.
5️⃣ Work with a nested list and access deep elements.
"""

# End of class_nine_list_methods.py
# 🚀 Keep Learning — Keep Coding!
# Rajib Sharker — November 06, 2025