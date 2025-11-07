# class_seventeen_oop.py
# Topic: Object-Oriented Programming (OOP) in Python
# Author: Razz
# Python Crash Course - Day 2 (Part 1)

"""
In this class we will learn:
1️⃣ Class and Object
2️⃣ __init__ Constructor
3️⃣ Instance and Class Variables
4️⃣ Inheritance
5️⃣ Polymorphism
6️⃣ Encapsulation and Abstraction
"""

# ===============================
# 🎓 1. CLASS AND OBJECT
# ===============================
class Student:
    # __init__ হল constructor — object তৈরি হলে এটি স্বয়ংক্রিয়ভাবে রান হয়
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
     # Instance Method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    #Create Object
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")

student1.display_info()
student2.display_info()


# ===============================
# 🚗 2. INHERITANCE
# ===============================
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} is moving...")

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)  # Call parent constructor
        self.color = color

    def info(self):
        print(f"{self.brand} {self.model} ({self.color}) is a Car.")

car1 = Car("Toyota", "Corolla", "Red")
car1.move()
car1.info()


# ===============================
# 🏦 3. ENCAPSULATION
# ===============================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (encapsulation)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Razz", 5000)
account.deposit(1000)
account.withdraw(2000)
print("Final Balance:", account.get_balance())


# ===============================
# 🎭 4. POLYMORPHISM
# ===============================
class Bird:
    def make_sound(self):
        print("Some generic bird sound")

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp Chirp!")

class Crow(Bird):
    def make_sound(self):
        print("Caw Caw!")

birds = [Sparrow(), Crow(), Bird()]
for b in birds:
    b.make_sound()


# ===============================
# 🌟 5. ABSTRACTION (via abc module)
# ===============================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Area of Circle:", circle.area())

# End of Class Seventeen
# 🚀 Keep practicing and build real-world models using OOP! 