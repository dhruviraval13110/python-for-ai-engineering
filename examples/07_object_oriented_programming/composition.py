"""
=========================================================
Python Composition
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : composition.py

Description
-----------
Composition is an Object-Oriented Programming (OOP)
relationship where one class contains an object of
another class.

It represents a strong "HAS-A" relationship.

In composition, the contained object usually cannot
exist independently of the owner object.

Topics Covered
--------------
✔ What is Composition?
✔ HAS-A Relationship
✔ Creating Objects Inside Classes
✔ Strong Ownership
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("COMPOSITION")
print("=" * 60)

# =====================================================
# Example 1 - Basic Composition
# =====================================================

print("\nExample 1 - Basic Composition")


class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is Moving")


car = Car()

car.drive()

# =====================================================
# Example 2 - Computer and CPU
# =====================================================

print("\nExample 2 - Computer")


class CPU:

    def process(self):
        print("CPU Processing...")


class Computer:

    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cpu.process()
        print("Computer Running")


computer = Computer()

computer.run()

# =====================================================
# Example 3 - House and Room
# =====================================================

print("\nExample 3 - House")


class Room:

    def show(self):
        print("Room Created")


class House:

    def __init__(self):
        self.room = Room()

    def display(self):
        self.room.show()
        print("House Ready")


house = House()

house.display()

# =====================================================
# Example 4 - Library and Book
# =====================================================

print("\nExample 4 - Library")


class Book:

    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)


class Library:

    def __init__(self):
        self.book = Book("Python Programming")

    def show_book(self):
        self.book.display()


library = Library()

library.show_book()

# =====================================================
# Example 5 - Human and Heart
# =====================================================

print("\nExample 5 - Human")


class Heart:

    def beat(self):
        print("Heart is Beating")


class Human:

    def __init__(self):
        self.heart = Heart()

    def live(self):
        self.heart.beat()
        print("Human is Alive")


human = Human()

human.live()

# =====================================================
# Example 6 - AI Engineering Example
# =====================================================

print("\nExample 6 - AI Engineering")


class DataPreprocessor:

    def preprocess(self):
        print("Cleaning Dataset...")


class AIModel:

    def __init__(self):
        self.preprocessor = DataPreprocessor()

    def train(self):
        self.preprocessor.preprocess()
        print("Training AI Model...")


model = AIModel()

model.train()

# =====================================================
# Example 7 - Mobile and Battery
# =====================================================

print("\nExample 7 - Mobile")


class Battery:

    def charge(self):
        print("Battery Charging...")


class Mobile:

    def __init__(self):
        self.battery = Battery()

    def power_on(self):
        self.battery.charge()
        print("Mobile Started")


mobile = Mobile()

mobile.power_on()

# =====================================================
# Example 8 - Bank Account
# =====================================================

print("\nExample 8 - Bank")


class DebitCard:

    def swipe(self):
        print("Card Swiped")


class BankAccount:

    def __init__(self):
        self.card = DebitCard()

    def payment(self):
        self.card.swipe()
        print("Payment Successful")


account = BankAccount()

account.payment()

# =====================================================
# Example 9 - School and Student
# =====================================================

print("\nExample 9 - School")


class Student:

    def study(self):
        print("Student Studying")


class School:

    def __init__(self):
        self.student = Student()

    def conduct_class(self):
        self.student.study()


school = School()

school.conduct_class()

# =====================================================
# Example 10 - Composition Diagram
# =====================================================

print("\nExample 10 - Composition Diagram")

print("""
        Car
         │
         │ HAS-A
         ▼
      Engine

If Car is destroyed,
Engine is also destroyed.

This is Composition.
""")

# =====================================================
# Composition vs Inheritance
# =====================================================

print("\nComposition vs Inheritance")

print("""
Composition
-----------
HAS-A Relationship

Example:
Car HAS-A Engine

Inheritance
-----------
IS-A Relationship

Example:
Dog IS-A Animal
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Confusing Composition with Inheritance.

❌ Using inheritance where composition
would be better.

❌ Creating unnecessary dependencies.

❌ Making objects tightly coupled.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use Composition for HAS-A relationships.

✔ Keep classes independent.

✔ Reuse small components.

✔ Prefer Composition over deep inheritance.

✔ Design modular classes.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is Composition?

A. Composition is a HAS-A relationship
where one class owns another class.

Q. Is Composition stronger than Aggregation?

A. Yes.

Q. Give an example.

A.
Car HAS-A Engine

Human HAS-A Heart

Computer HAS-A CPU

Q. Composition or Inheritance?

A. Use Composition when one object
contains another object.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Composition represents a HAS-A relationship.

✔ One object owns another object.

✔ Composition promotes modular design.

✔ It reduces unnecessary inheritance.

✔ Professional Python projects often prefer
Composition over complex inheritance hierarchies.
""")
