# class_fifteen_error_handling.py
# Topic: Error Handling and Exceptions
# Author: Razz
# Python Crash Course - Day 3 (Part 1)

"""
In this class we will learn:
1️⃣ What is an Exception
2️⃣ try / except / else / finally
3️⃣ Multiple Exception Handling
4️⃣ Custom Exceptions
"""

# ===============================
# ⚠️ Basic try-except Example
# ===============================
try:
    num = int(input("Enter a number: "))
    print("10 divided by", num, "=", 10 / num)
except ZeroDivisionError:
    print("❌ You cannot divide by zero!")
except ValueError:
    print("❌ Please enter a valid number!")
else:
    print("✅ Operation successful!")
finally:
    print("🎯 Program finished.\n")


# ===============================
# ⚙️ Handling Multiple Exceptions
# ===============================
try:
    a = [1, 2, 3]
    print(a[5])   # Index out of range
except (IndexError, TypeError) as e:
    print("⚠️ Error occurred:", e)
finally:
    print("✅ Handled safely.\n")

# ===============================
# 🧩 Custom Exception Example
# ===============================
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("You must be 18 or older.")
    print("Access granted ✅")
except InvalidAgeError as e:
    print("🚫 Custom Exception:", e)
except ValueError:
    print("⚠️ Please enter a valid number for age!")
finally:
    print("🎯 Age verification complete.\n")


# ===============================
# 🧪 Practice Tasks
# ===============================
"""
1️⃣ Take a number input and handle both ValueError & ZeroDivisionError.
2️⃣ Try to open a file that doesn’t exist and handle FileNotFoundError.
3️⃣ Create your own custom exception (e.g., NegativeNumberError).
"""

# End of class_fifteen_error_handling.py
# Rajib Sharker — November 04, 2025
# Python Crash Course - Day 3 (Part 1)