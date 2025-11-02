# class_five_conditions.py
# Topic: Conditions & Loops
# Author: Razz
# Python Crash Course - Day 1 (Part 5)

"""
In this class, we will learn:
1️⃣ if statement
2️⃣ if-else statement
3️⃣ if-elif-else statement
"""
# ===============================
# 🧵 1. IF Statement
# ===============================
num = 10
if num > 0:
    print(f"{num} is positive")
    print("This number is greater than zero.")

# ===============================
# 🧵 2. IF-ELSE Statement
# ===============================
num = -5
if num >= 0:
    print(f"{num} is non-negative")
else:
    print(f"{num} is negative")

# ===============================
# 🧵 3. IF-ELIF-ELSE Statement
# ===============================

marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:    
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# ===============================
# 🔄 Nested IF Example
# ===============================

age = 20
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You can also drink alcohol in some countries.")
    else:
        print("You cannot drink alcohol in some countries.")
else:
    print("You are not eligible to vote.")
    
    
    
# ===============================
# 🧩 Practice Tasks:
# ===============================
"""
1️⃣ Take user input for age and print eligibility for voting.
2️⃣ Take marks input and print grade using if-elif-else.
3️⃣ Nested if: check if a number is even or odd and positive or negative.
"""