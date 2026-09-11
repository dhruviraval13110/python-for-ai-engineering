"""
=========================================================
Python Dataclasses
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : dataclasses_intro.py

Description
-----------
Dataclasses were introduced in Python 3.7 to reduce
boilerplate code when creating classes.

By using the @dataclass decorator, Python automatically
generates common methods like __init__(), __repr__(),
__eq__(), and more.

Dataclasses are especially useful when a class is mainly
used to store data.

Topics Covered
--------------
✔ What are Dataclasses?
✔ @dataclass Decorator
✔ Automatic __init__()
✔ Automatic __repr__()
✔ Automatic __eq__()
✔ Default Values
✔ field()
✔ Frozen Dataclasses
✔ AI Engineering Example
✔ Best Practices
"""

from dataclasses import dataclass, field

print("=" * 60)
print("DATACLASSES")
print("=" * 60)

# =====================================================
# Example 1 - Traditional Class
# =====================================================

print("\nExample 1 - Traditional Class")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Dhruvi", 21)

print(student.name)
print(student.age)

# =====================================================
# Example 2 - Basic Dataclass
# =====================================================

print("\nExample 2 - Basic Dataclass")


@dataclass
class Student:

    name: str
    age: int


student = Student("Rahul", 20)

print(student)

# =====================================================
# Example 3 - Automatic Equality
# =====================================================

print("\nExample 3 - Automatic Equality")


@dataclass
class Employee:

    id: int
    name: str


employee1 = Employee(101, "Amit")
employee2 = Employee(101, "Amit")

print(employee1 == employee2)

# =====================================================
# Example 4 - Default Values
# =====================================================

print("\nExample 4 - Default Values")


@dataclass
class Product:

    name: str
    price: int = 100


product = Product("Keyboard")

print(product)

# =====================================================
# Example 5 - field()
# =====================================================

print("\nExample 5 - field()")


@dataclass
class Course:

    name: str
    students: list = field(default_factory=list)


course = Course("Python")

course.students.append("Dhruvi")
course.students.append("Rahul")

print(course)

# =====================================================
# Example 6 - Frozen Dataclass
# =====================================================

print("\nExample 6 - Frozen Dataclass")


@dataclass(frozen=True)
class Country:

    name: str
    capital: str


country = Country("India", "New Delhi")

print(country)

# Uncommenting the next line will raise an error.
# country.name = "USA"

# =====================================================
# Example 7 - Dataclass with Methods
# =====================================================

print("\nExample 7 - Dataclass with Methods")


@dataclass
class Rectangle:

    length: int
    width: int

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area())

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


@dataclass
class AIModel:

    model_name: str
    accuracy: float
    framework: str


model = AIModel(
    "Image Classifier",
    98.75,
    "TensorFlow"
)

print(model)

# =====================================================
# Example 9 - Sorting Dataclasses
# =====================================================

print("\nExample 9 - Sorting Dataclasses")


@dataclass(order=True)
class StudentScore:

    marks: int
    name: str


students = [
    StudentScore(75, "Rahul"),
    StudentScore(92, "Dhruvi"),
    StudentScore(81, "Amit")
]

students.sort()

for student in students:
    print(student)

# =====================================================
# Example 10 - Inventory System
# =====================================================

print("\nExample 10 - Inventory System")


@dataclass
class Item:

    name: str
    quantity: int
    price: float

    def total_value(self):
        return self.quantity * self.price


item = Item(
    "Laptop",
    5,
    55000
)

print(item)

print("Total Value:", item.total_value())

# =====================================================
# Advantages of Dataclasses
# =====================================================

print("\nAdvantages")

print("""
✔ Less Boilerplate Code

✔ Automatic __init__()

✔ Automatic __repr__()

✔ Automatic __eq__()

✔ Easy to Read

✔ Cleaner Code
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting @dataclass decorator.

❌ Using mutable default values directly.

❌ Not using field(default_factory=list).

❌ Using frozen dataclass when
object modification is required.

❌ Adding unnecessary custom __init__().
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use dataclasses for data containers.

✔ Use type hints for all attributes.

✔ Use field(default_factory=list)
for mutable objects.

✔ Use frozen=True for immutable objects.

✔ Keep business logic minimal.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a Dataclass?

A. A special Python class that
automatically generates methods
like __init__(), __repr__(), and __eq__().

Q. Which module provides dataclasses?

A. dataclasses

Q. Which decorator is used?

A. @dataclass

Q. Why use field(default_factory=list)?

A. To safely create mutable default values.

Q. What does frozen=True do?

A. It makes objects immutable.

Q. When should dataclasses be used?

A. When a class mainly stores data.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Dataclasses reduce boilerplate code.

✔ @dataclass automatically creates
__init__(), __repr__(), and __eq__().

✔ field() is used for mutable defaults.

✔ frozen=True creates immutable objects.

✔ Dataclasses are widely used in AI,
Machine Learning, APIs, automation,
and enterprise Python applications.
""")
