# class_three_datatypes.py
# Topic: Data Types & Structures
# Author: Razz
# Python Crash Course - Day 1 (Part 2)

"""
In this class, we will learn about:
1️⃣ String
2️⃣ List
3️⃣ Tuple
4️⃣ Set
5️⃣ Dictionary
"""

# ===============================
# 🧵 1. STRING
# ===============================
name="Python Programming"
print("String:", name)
print("Type of name:", type(name))
print("Length of string:", len(name))
print("First character:", name[0])
print("Substring (0-6):", name[0:6])
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Replace 'Python' with 'Java':", name.replace("Python", "Java"))
print("Split by space:", name.split(" "))
print()


# ===============================
# 📋 2. LIST
# ===============================

fruits = ["Apple", "Banana", "Cherry", "Date"]
print("\nFruits List:", fruits)
print("Type of fruits:", type(fruits))
print("Length of list:", len(fruits))
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice (1-3):", fruits[1:3])
print("Add 'Elderberry':", fruits + ["Elderberry"])
print("Remove 'Banana':", [fruit for fruit in fruits if fruit != "Banana"])
print("Sort list:", sorted(fruits))
print("Reverse list:", list(reversed(fruits)))
print ("After removing Banana:", fruits)
print("After changing first fruit to Mango:")
fruits[0] = "Mango"
print(fruits)
print("Total fruits now:")
print ("Sliced list:", fruits[1:3])
print()


# ===============================
# 🎯 3. TUPLE
# ===============================
# Tuple is immutable (cannot change)
number = (10, 20, 30, 40)
print("\nNumber Tuple:", number)
print("Type of number:", type(number))
print("Length of tuple:", len(number))
print("First element:", number[0])
print("Last element:", number[-1])
print("Slice (1-3):", number[1:3])
print("Count of 20 in tuple:", number.count(20))
print("Index of 30 in tuple:", number.index(30))
print()


# ===============================
# 🧮 4. SET
# ===============================
# Set is unordered, unindexed, and stores unique items
languages = {"Python", "C", "Java", "Python"}
print("\nLanguages Set:", languages)
print("Type of languages:", type(languages))
print("Length of set:", len(languages))
print("Add 'JavaScript':", languages.union({"JavaScript"}))
print("Remove 'C':", languages.difference({"C"}))
print("Check if 'Java' in set:", "Java" in languages)
print("After removing C:", languages)
print("Is Python in set?", "Python" in languages)



# ===============================
# 📚 5. DICTIONARY
# ===============================
# Key-Value pair data structure


student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
} 

print("\nStudent Dictionary:", student)
print("Type of student:", type(student))
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))
print("Student Subjects:", student["subjects"])
print("Add 'address':")
student["grade"] = "A+"
print("Updated Grade:", student["grade"])
student["city"] = "New York"
print("After adding new key:", student)


# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)