"""
=========================================================
Python Classes and Objects
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : classes_objects.py

Description
-----------
Classes and Objects are the foundation of Object-Oriented
Programming (OOP).

A class acts as a blueprint, while an object is an
actual instance created from that blueprint.

Topics Covered
--------------
✔ Creating Classes
✔ Creating Objects
✔ Class Attributes
✔ Object Attributes
✔ Accessing Attributes
✔ Multiple Objects
✔ Updating Attributes
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("CLASSES AND OBJECTS")
print("=" * 60)

# =====================================================
# Example 1 - Creating a Class
# =====================================================

print("\nExample 1 - Creating a Class")


class Student:
    pass


student1 = Student()

print(student1)

# =====================================================
# Example 2 - Class with Attributes
# =====================================================

print("\nExample 2 - Class Attributes")


class Car:

    brand = "Tesla"
    color = "White"


car = Car()

print(car.brand)
print(car.color)

# =====================================================
# Example 3 - Object Attributes
# =====================================================

print("\nExample 3 - Object Attributes")


class Employee:
    pass


employee = Employee()

employee.name = "Dhruvi"
employee.age = 20
employee.salary = 50000

print(employee.name)
print(employee.age)
print(employee.salary)

# =====================================================
# Example 4 - Multiple Objects
# =====================================================

print("\nExample 4 - Multiple Objects")


class Mobile:

    brand = "Samsung"


mobile1 = Mobile()
mobile2 = Mobile()

print(mobile1.brand)
print(mobile2.brand)

# =====================================================
# Example 5 - Updating Object Attributes
# =====================================================

print("\nExample 5 - Updating Attributes")


class Laptop:

    brand = "HP"


laptop = Laptop()

print("Before:", laptop.brand)

laptop.brand = "Dell"

print("After :", laptop.brand)

# =====================================================
# Example 6 - Real-World Example
# =====================================================

print("\nExample 6 - Student Example")


class Student:

    school = "ABC School"


student1 = Student()
student2 = Student()

student1.name = "Rahul"
student1.roll = 101

student2.name = "Priya"
student2.roll = 102

print(student1.name, student1.roll)
print(student2.name, student2.roll)
print(student1.school)

# =====================================================
# Example 7 - AI Engineering Example
# =====================================================

print("\nExample 7 - AI Model")


class AIModel:

    framework = "TensorFlow"


model1 = AIModel()

model1.name = "Image Classifier"
model1.accuracy = 98.4

print(model1.name)
print(model1.framework)
print(model1.accuracy)

# =====================================================
# Example 8 - Dynamic Attributes
# =====================================================

print("\nExample 8 - Dynamic Attributes")


class Book:
    pass


book = Book()

book.title = "Python for AI"
book.author = "Dhruvi"
book.pages = 350

print(book.title)
print(book.author)
print(book.pages)

# =====================================================
# Example 9 - hasattr()
# =====================================================

print("\nExample 9 - hasattr()")


print(hasattr(book, "title"))
print(hasattr(book, "price"))

# =====================================================
# Example 10 - getattr()
# =====================================================

print("\nExample 10 - getattr()")


print(getattr(book, "title"))
print(getattr(book, "price", "Not Available"))

# =====================================================
# Example 11 - setattr()
# =====================================================

print("\nExample 11 - setattr()")


setattr(book, "price", 499)

print(book.price)

# =====================================================
# Example 12 - delattr()
# =====================================================

print("\nExample 12 - delattr()")


delattr(book, "pages")

print(hasattr(book, "pages"))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Confusing class and object.

❌ Creating too many unrelated attributes.

❌ Using class variables when instance
variables are needed.

❌ Giving unclear class names.

❌ Forgetting to create an object.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Class names should use PascalCase.

✔ Variable names should use snake_case.

✔ Keep one class responsible for one task.

✔ Use meaningful attribute names.

✔ Create multiple objects from one class
instead of duplicate code.

✔ Keep classes simple and reusable.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a class?

A. A blueprint used to create objects.

Q. What is an object?

A. An instance of a class.

Q. Can one class create multiple objects?

A. Yes.

Q. What is an attribute?

A. A variable belonging to an object
or a class.

Q. Difference between class and object?

Class:
Blueprint

Object:
Actual instance created from that blueprint.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ A class is a blueprint.

✔ An object is an instance of a class.

✔ Attributes store object data.

✔ Multiple objects can be created from
the same class.

✔ Classes and objects form the
foundation of Object-Oriented Programming.
""")
