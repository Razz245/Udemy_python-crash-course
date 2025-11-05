# class_twelve_dictionaries.py
# Topic: Dictionaries in Python
# Author: Razz
# Python Crash Course - Day 2 (Part 1)

"""
In this class, we will learn about:
1️⃣ What is a Dictionary?
2️⃣ Creating Dictionaries
3️⃣ Accessing Items
4️⃣ Adding & Updating Items
5️⃣ Removing Items
6️⃣ Looping through Dictionaries
7️⃣ Nested Dictionaries
"""

# ===============================
# 🧱 1. WHAT IS A DICTIONARY?
# ===============================
# A dictionary stores data in key-value pairs.

student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "English", "Science"]
}

print("Student Dictionary:", student)
print("Type of student:", type(student))
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))
print("Student Subjects:", student["subjects"])
print()


# ===============================
# ✏️ 2. ADDING & UPDATING ITEMS
# ===============================
student["city"] = "New York"        # Add new key-value
student["grade"] = "A+"             # Update existing key
print("After Adding & Updating:", student)
print()


# ===============================
# ❌ 3. REMOVING ITEMS
# ===============================
student.pop("age")                  # Remove by key
print("After Removing 'age':", student)

del student["city"]                 # Delete by key
print("After Deleting 'city':", student)

student.clear()                     # Clear all items
print("After Clearing Dictionary:", student)
print()

# ===============================
# 🔁 4. LOOPING THROUGH DICTIONARY
# ===============================
person = {
    "name": "Razz",
    "country": "Bangladesh",
    "language": "Python"
}

print("Keys:")
for key in person.keys():
    print("-", key)

print("\nValues:")
for value in person.values():
    print("-", value)

print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"{key} → {value}")
print()

# ===============================
# 🧩 5. NESTED DICTIONARIES
# ===============================
students = {
    "student1": {"name": "Alice", "marks": 85},
    "student2": {"name": "Bob", "marks": 90},
    "student3": {"name": "Charlie", "marks": 78}
}

print("Nested Dictionary Example:")
for key, info in students.items():
    print(f"{key}: Name = {info['name']}, Marks = {info['marks']}")
print()

# ===============================
# 💡 Practice Tasks
# ===============================
"""
1️⃣ Create a dictionary of 3 employees (name, age, salary)
2️⃣ Print all keys and values using loops
3️⃣ Update one employee’s salary
4️⃣ Remove one employee from dictionary
5️⃣ Create nested dictionary for departments
"""

# End of class_twelve_dictionaries.py
# Date: November 07, 2025
# Python Crash Course - Class 12