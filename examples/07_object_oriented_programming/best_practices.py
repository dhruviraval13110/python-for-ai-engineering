"""
=========================================================
Python OOP Best Practices
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : best_practices.py

Description
-----------
Writing Object-Oriented code is not only about using
classes and objects. Professional developers follow
certain design principles and coding standards that make
their code clean, reusable, maintainable, and scalable.

This file covers the most important OOP best practices
used in real-world Python projects.

Topics Covered
--------------
✔ Meaningful Class Design
✔ Encapsulation
✔ Composition over Inheritance
✔ SOLID Principles
✔ Single Responsibility Principle
✔ Naming Conventions
✔ Type Hints
✔ Docstrings
✔ Avoid Global Variables
✔ Real-world AI Engineering Example
"""

print("=" * 60)
print("OOP BEST PRACTICES")
print("=" * 60)

# =====================================================
# Best Practice 1 - Keep Classes Focused
# =====================================================

print("\nBest Practice 1 - Single Responsibility")


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()

print(calculator.add(10, 5))

print("""
Good Practice:
Each class should have only one responsibility.
""")

# =====================================================
# Best Practice 2 - Use Meaningful Class Names
# =====================================================

print("\nBest Practice 2 - Naming")

print("""
Good

Customer
Employee
BankAccount
ImageClassifier

Bad

Data
Temp
ABC
Object1
""")

# =====================================================
# Best Practice 3 - Encapsulation
# =====================================================

print("\nBest Practice 3 - Encapsulation")


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

account.deposit(5000)

print(account.get_balance())

# =====================================================
# Best Practice 4 - Composition Over Inheritance
# =====================================================

print("\nBest Practice 4 - Composition")


class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car Moving")


car = Car()

car.drive()

print("""
Prefer Composition when classes have
a HAS-A relationship.
""")

# =====================================================
# Best Practice 5 - Use Type Hints
# =====================================================

print("\nBest Practice 5 - Type Hints")


class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


student = Student("Dhruvi", 21)

print(student.name)

# =====================================================
# Best Practice 6 - Write Docstrings
# =====================================================

print("\nBest Practice 6 - Docstrings")


class Rectangle:
    """Represents a rectangle."""

    def area(self, length, width):
        """Calculate rectangle area."""
        return length * width


rectangle = Rectangle()

print(rectangle.area(5, 4))

# =====================================================
# Best Practice 7 - Use Properties
# =====================================================

print("\nBest Practice 7 - Properties")


class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):

        if amount >= 0:
            self._salary = amount


employee = Employee(50000)

employee.salary = 65000

print(employee.salary)

# =====================================================
# Best Practice 8 - Follow SOLID Principles
# =====================================================

print("\nBest Practice 8 - SOLID")

print("""
S - Single Responsibility Principle

O - Open/Closed Principle

L - Liskov Substitution Principle

I - Interface Segregation Principle

D - Dependency Inversion Principle
""")

# =====================================================
# Best Practice 9 - AI Engineering Example
# =====================================================

print("\nBest Practice 9 - AI Engineering")


class DataLoader:

    def load_data(self):
        print("Loading Dataset...")


class ModelTrainer:

    def train(self):
        print("Training AI Model...")


class ModelEvaluator:

    def evaluate(self):
        print("Evaluating Model...")


loader = DataLoader()
trainer = ModelTrainer()
evaluator = ModelEvaluator()

loader.load_data()
trainer.train()
evaluator.evaluate()

print("""
Each class has only one responsibility.
""")

# =====================================================
# Best Practice 10 - Keep Methods Small
# =====================================================

print("\nBest Practice 10 - Small Methods")


class EmailService:

    def send_email(self):
        print("Email Sent")


service = EmailService()

service.send_email()

print("""
Small methods are easier to
read, test, and maintain.
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Very large classes.

❌ Too many responsibilities.

❌ Deep inheritance hierarchies.

❌ Public access to sensitive data.

❌ Poor variable names.

❌ No documentation.

❌ No type hints.

❌ Copy-paste code.
""")

# =====================================================
# Professional Tips
# =====================================================

print("\nProfessional Tips")

print("""
✔ Follow PEP 8.

✔ Write reusable classes.

✔ Keep classes loosely coupled.

✔ Prefer Composition over Inheritance.

✔ Use Properties for validation.

✔ Add Docstrings.

✔ Use Type Hints.

✔ Write Unit Tests.

✔ Keep code readable.

✔ Refactor regularly.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Why should a class have only one responsibility?

A. It becomes easier to maintain,
test, and extend.

Q. Why is Composition preferred over Inheritance?

A. It creates flexible and reusable
software with lower coupling.

Q. What is encapsulation?

A. Protecting object data by restricting
direct access.

Q. What is the Single Responsibility Principle?

A. Every class should have only one reason
to change.

Q. Why use Type Hints?

A. They improve readability,
IDE support, and static analysis.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Keep classes small and focused.

✔ Use meaningful class names.

✔ Prefer Composition over Inheritance.

✔ Follow SOLID principles.

✔ Use Encapsulation and Properties.

✔ Write Docstrings and Type Hints.

✔ Follow PEP 8.

✔ Build reusable and maintainable code.

✔ Professional OOP code is simple,
clean, scalable, and easy to understand.
""")
