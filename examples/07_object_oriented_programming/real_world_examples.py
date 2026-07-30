"""
=========================================================
Python Real-World OOP Examples
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : real_world_examples.py

Description
-----------
This file demonstrates how Object-Oriented Programming
(OOP) is used in real-world applications.

These examples combine the concepts learned throughout
this module, including:
- Classes & Objects
- Constructors
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Properties
- Dataclasses

Topics Covered
--------------
✔ Banking System
✔ Student Management System
✔ E-Commerce System
✔ Library Management
✔ Employee Management
✔ Hospital Management
✔ AI Engineering Example
✔ Vehicle Rental System
✔ Restaurant Ordering System
✔ Inventory Management System
"""

from dataclasses import dataclass

print("=" * 60)
print("REAL-WORLD OOP EXAMPLES")
print("=" * 60)

# =====================================================
# Example 1 - Banking System
# =====================================================

print("\nExample 1 - Banking System")


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Balance: ₹{self.__balance}")


account = BankAccount("Dhruvi", 10000)

account.deposit(2000)
account.withdraw(3000)
account.show_balance()

# =====================================================
# Example 2 - Student Management System
# =====================================================

print("\nExample 2 - Student Management")


@dataclass
class Student:
    name: str
    marks: int


student = Student("Rahul", 88)

print(student)

# =====================================================
# Example 3 - E-Commerce Product
# =====================================================

print("\nExample 3 - E-Commerce")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ₹{self.price}")


product = Product("Wireless Mouse", 899)

product.display()

# =====================================================
# Example 4 - Library Management
# =====================================================

print("\nExample 4 - Library")


class Book:

    def __init__(self, title):
        self.title = title

    def issue(self):
        print(f"{self.title} Issued")


book = Book("Python for AI Engineering")

book.issue()

# =====================================================
# Example 5 - Employee Management
# =====================================================

print("\nExample 5 - Employee")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print(self.name, "-", self.salary)


employee = Employee("Amit", 65000)

employee.details()

# =====================================================
# Example 6 - Hospital Management
# =====================================================

print("\nExample 6 - Hospital")


class Doctor:

    def consult(self):
        print("Doctor is consulting patient")


class Hospital:

    def __init__(self):
        self.doctor = Doctor()

    def start(self):
        self.doctor.consult()


hospital = Hospital()

hospital.start()

# =====================================================
# Example 7 - AI Engineering
# =====================================================

print("\nExample 7 - AI Engineering")


class AIModel:

    def train(self):
        print("Training AI Model...")


class ImageClassifier(AIModel):

    def predict(self):
        print("Predicting Images...")


model = ImageClassifier()

model.train()
model.predict()

# =====================================================
# Example 8 - Vehicle Rental System
# =====================================================

print("\nExample 8 - Vehicle Rental")


class Vehicle:

    def rent(self):
        print("Vehicle Rented")


class Bike(Vehicle):

    def rent(self):
        print("Bike Rented")


class Car(Vehicle):

    def rent(self):
        print("Car Rented")


vehicles = [Bike(), Car()]

for vehicle in vehicles:
    vehicle.rent()

# =====================================================
# Example 9 - Restaurant Ordering System
# =====================================================

print("\nExample 9 - Restaurant")


class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} : ₹{self.price}")


pizza = MenuItem("Veg Pizza", 299)

pizza.show()

# =====================================================
# Example 10 - Inventory Management
# =====================================================

print("\nExample 10 - Inventory")


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_inventory(self):

        for product in self.products:
            print(product)


inventory = Inventory()

inventory.add_product("Laptop")
inventory.add_product("Keyboard")
inventory.add_product("Mouse")

inventory.show_inventory()

# =====================================================
# Where OOP is Used
# =====================================================

print("\nWhere OOP is Used")

print("""
✔ Web Development

✔ Mobile Applications

✔ AI & Machine Learning

✔ Game Development

✔ Banking Software

✔ ERP Systems

✔ Hospital Management

✔ Inventory Systems

✔ Robotics

✔ Cloud Computing
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Creating unnecessary classes.

❌ Breaking encapsulation.

❌ Overusing inheritance.

❌ Ignoring code reuse.

❌ Large classes with multiple responsibilities.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Design reusable classes.

✔ Follow SOLID principles.

✔ Use Composition when appropriate.

✔ Keep classes focused.

✔ Use meaningful names.

✔ Write clean documentation.

✔ Add type hints where possible.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Why is OOP used in software development?

A. It improves code reusability,
maintainability, and scalability.

Q. Name some industries that use OOP.

• Banking
• Healthcare
• AI
• E-Commerce
• ERP
• Gaming

Q. Which OOP concept is used most in
real-world applications?

A.
All four:
• Encapsulation
• Inheritance
• Polymorphism
• Abstraction
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ OOP powers most modern software.

✔ Classes model real-world entities.

✔ Encapsulation protects data.

✔ Inheritance enables code reuse.

✔ Polymorphism provides flexibility.

✔ Composition creates modular systems.

✔ Professional AI applications heavily
use OOP principles for scalable code.
""")
