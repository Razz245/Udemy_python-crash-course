# class_four_index_slice_loop.py
# Topic: Indexing, Slicing, Looping
# Author: Razz
# Python Crash Course - Day 1 (Part 3)

"""
In this class, we will learn:
1️⃣ Indexing
2️⃣ Slicing
3️⃣ Looping (for, while)
"""
# ===============================
# 🧵 1. INDEXING
# ===============================
# Strings
name="Python"
print("String:", name)
print("First character (index 0):", name[0])
print("Last character (index -1):", name[-1])
print("Second character (index 1):", name[1])
print("Second last character (index -2):", name[-2])
print()


# 📋 List
fruits = ["Apple", "Banana", "Cherry", "Date"]
print("Fruits List:", fruits)
print("First fruit (index 0):", fruits[0])
print("Last fruit (index -1):", fruits[-1])
print("Second fruit (index 1):", fruits[1])
print("Second last fruit (index -2):", fruits[-2])
print()


# Tuple
number = (10, 20, 30, 40)
print("\nNumber Tuple:", number)
print("First number (index 0):", number[0])
print("Last number (index -1):", number[-1])
print("Second number (index 1):", number[1])
print("Second last number (index -2):", number[-2])
print()


# ===============================
# 🔪 2. SLICING
# ===============================
# Syntax: variable[start:stop:step]
# Strings
print("\nString Slice (0-4):", name[0:4])
print("List Slice (1-3):", fruits[1:3])
print("Tuple Slice (0:3):", number[0:3])

# Step slicing
print("String with step 2:", name[0:6:2])
print("Reverse String:", name[::-1])

# ===============================
# 🔄 3. LOOPING
# ===============================
# For loop
print("\nFor loop through list:")
for fruit in fruits:
    print(fruit)

# Using range()
print("\nNumbers from 0 to 4:")
for i in range(5):
    print(i)

# While loop
print("\nWhile loop counting:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Nested loop example
print("\nMultiplication table of 3:")
for i in range(1, 11):
    for j in range(3, 4):
        print(f"{j} x {i} = {i*j}")

# Loop with break & continue
print("\nLoop with break & continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    if i == 5:
        print("Breaking at 5")
        break
    print("Number:", i)

# ===============================
# 🧩 Practice Tasks:
# ===============================
"""
1️⃣ Take a string input and print each character using a loop.
2️⃣ Take a list of numbers and print the even numbers using for loop.
3️⃣ Use slicing to reverse a list or string.
4️⃣ Create a nested loop to print a simple pattern.
"""
# End of class_four_index_slice_loop.py
## Happy Coding! 🚀
#Rajib Sharker--November 03, 2025
# Python Crash Course - Day 1 (Part 4)