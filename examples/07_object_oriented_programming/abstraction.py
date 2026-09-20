"""
=========================================================
Python Abstraction
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : abstraction.py

Description
-----------
Abstraction is one of the four fundamental pillars of
Object-Oriented Programming (OOP).

Abstraction means hiding the internal implementation
details and exposing only the essential functionality
to the user.

In Python, abstraction is implemented using the
abc (Abstract Base Class) module.

Topics Covered
--------------
✔ What is Abstraction?
✔ Abstract Base Class (ABC)
✔ Abstract Methods
✔ Why Abstraction?
✔ Multiple Abstract Methods
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("ABSTRACTION")
print("=" * 60)

# =====================================================
# Example 1 - Abstract Class
# =====================================================

print("\nExample 1 - Abstract Class")


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()
dog.sound()

# =====================================================
# Example 2 - Multiple Abstract Methods
# =====================================================

print("\nExample 2 - Multiple Abstract Methods")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Area      :", rectangle.area())
print("Perimeter :", rectangle.perimeter())

# =====================================================
# Example 3 - Vehicle Example
# =====================================================

print("\nExample 3 - Vehicle")


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()
car.start()

# =====================================================
# Example 4 - Payment System
# =====================================================

print("\nExample 4 - Payment System")


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1200)

# =====================================================
# Example 5 - Employee Management
# =====================================================

print("\nExample 5 - Employee")


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


employee = FullTimeEmployee(60000)

print(employee.calculate_salary())

# =====================================================
# Example 6 - AI Engineering Example
# =====================================================

print("\nExample 6 - AI Engineering")


class AIModel(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass


class ImageClassifier(AIModel):

    def train(self):
        print("Training Image Classifier...")

    def predict(self):
        print("Predicting Images...")


model = ImageClassifier()

model.train()
model.predict()

# =====================================================
# Example 7 - Database Example
# =====================================================

print("\nExample 7 - Database")


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")


database = MySQL()

database.connect()

# =====================================================
# Example 8 - Authentication System
# =====================================================

print("\nExample 8 - Authentication")


class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class GoogleLogin(Authentication):

    def login(self):
        print("Login with Google")


google = GoogleLogin()

google.login()

# =====================================================
# Example 9 - Instantiating Abstract Class
# =====================================================

print("\nExample 9 - Abstract Class Restriction")

print("""
The following is NOT allowed:

vehicle = Vehicle()

Reason:
Vehicle contains abstract methods.
Only child classes can be instantiated.
""")

# =====================================================
# Example 10 - Multiple Child Classes
# =====================================================

print("\nExample 10 - Multiple Implementations")


class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


class Email(Notification):

    def send(self):
        print("Email Sent")


class SMS(Notification):

    def send(self):
        print("SMS Sent")


notifications = [Email(), SMS()]

for notification in notifications:
    notification.send()

# =====================================================
# Why Abstraction?
# =====================================================

print("\nWhy Abstraction?")

print("""
✔ Hides implementation details

✔ Improves security

✔ Reduces complexity

✔ Enforces common interface

✔ Makes large applications easier
to maintain
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting @abstractmethod.

❌ Instantiating an abstract class.

❌ Not implementing all abstract methods.

❌ Confusing abstraction with encapsulation.

❌ Writing unnecessary abstract classes.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Create abstract classes only when needed.

✔ Define common interfaces.

✔ Keep abstract methods meaningful.

✔ Let child classes implement behavior.

✔ Use abstraction for scalable software.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is abstraction?

A. Hiding implementation details while
showing only essential functionality.

Q. Which module provides abstraction?

A. abc module.

Q. Which class is used?

A. ABC

Q. Which decorator is used?

A. @abstractmethod

Q. Can we create an object of an
abstract class?

A. No.

Q. Why is abstraction useful?

A. It reduces complexity and provides
a common interface for subclasses.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Abstraction hides implementation details.

✔ Python uses the abc module.

✔ Abstract classes inherit from ABC.

✔ Abstract methods use @abstractmethod.

✔ Child classes must implement all
abstract methods.

✔ Abstraction helps build clean,
maintainable, and scalable software.
""")
