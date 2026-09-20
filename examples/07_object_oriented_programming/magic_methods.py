"""
=========================================================
Python Magic Methods (Dunder Methods)
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : magic_methods.py

Description
-----------
Magic Methods (also called Dunder Methods because they
start and end with double underscores) are special
methods that allow Python objects to interact with
built-in functions and operators.

Examples include:
__init__, __str__, __len__, __add__, __eq__, etc.

Magic methods make custom classes behave like Python's
built-in data types.

Topics Covered
--------------
✔ What are Magic Methods?
✔ __init__()
✔ __str__()
✔ __repr__()
✔ __len__()
✔ __add__()
✔ __eq__()
✔ __lt__()
✔ __call__()
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("MAGIC METHODS (DUNDER METHODS)")
print("=" * 60)

# =====================================================
# Example 1 - __init__()
# =====================================================

print("\nExample 1 - __init__()")


class Student:

    def __init__(self, name):
        self.name = name


student = Student("Dhruvi")

print(student.name)

# =====================================================
# Example 2 - __str__()
# =====================================================

print("\nExample 2 - __str__()")


class Car:

    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car Brand: {self.brand}"


car = Car("Tesla")

print(car)

# =====================================================
# Example 3 - __repr__()
# =====================================================

print("\nExample 3 - __repr__()")


class Book:

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book('{self.title}')"


book = Book("Python for AI")

print(repr(book))

# =====================================================
# Example 4 - __len__()
# =====================================================

print("\nExample 4 - __len__()")


class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


playlist = Playlist(["Song 1", "Song 2", "Song 3"])

print(len(playlist))

# =====================================================
# Example 5 - __add__()
# =====================================================

print("\nExample 5 - __add__()")


class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"


wallet1 = Money(1000)
wallet2 = Money(2500)

print(wallet1 + wallet2)

# =====================================================
# Example 6 - __eq__()
# =====================================================

print("\nExample 6 - __eq__()")


class Employee:

    def __init__(self, employee_id):
        self.employee_id = employee_id

    def __eq__(self, other):
        return self.employee_id == other.employee_id


employee1 = Employee(101)
employee2 = Employee(101)
employee3 = Employee(102)

print(employee1 == employee2)
print(employee1 == employee3)

# =====================================================
# Example 7 - __lt__()
# =====================================================

print("\nExample 7 - __lt__()")


class Product:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


product1 = Product(1200)
product2 = Product(1800)

print(product1 < product2)

# =====================================================
# Example 8 - __call__()
# =====================================================

print("\nExample 8 - __call__()")


class Greeter:

    def __call__(self, name):
        print(f"Hello, {name}!")


greet = Greeter()

greet("Dhruvi")

# =====================================================
# Example 9 - AI Engineering Example
# =====================================================

print("\nExample 9 - AI Engineering")


class AIModel:

    def __init__(self, model_name):
        self.model_name = model_name

    def __str__(self):
        return f"AI Model: {self.model_name}"

    def __call__(self, data):
        print(f"Predicting on: {data}")


model = AIModel("Image Classifier")

print(model)

model("sample_image.jpg")

# =====================================================
# Example 10 - Multiple Magic Methods
# =====================================================

print("\nExample 10 - Multiple Magic Methods")


class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"Team with {len(self.members)} members"


team = Team(["A", "B", "C", "D"])

print(team)
print(len(team))

# =====================================================
# Commonly Used Magic Methods
# =====================================================

print("\nCommon Magic Methods")

print("""
__init__   -> Constructor

__str__    -> User-friendly string

__repr__   -> Developer representation

__len__    -> len()

__add__    -> +

__sub__    -> -

__mul__    -> *

__eq__     -> ==

__lt__     -> <

__gt__     -> >

__call__   -> Object behaves like a function
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting double underscores.

❌ Returning non-string from __str__().

❌ Comparing incompatible objects.

❌ Overloading operators unnecessarily.

❌ Ignoring readability.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Implement only necessary magic methods.

✔ Keep behavior intuitive.

✔ Return appropriate data types.

✔ Make custom classes behave like
Python built-in objects.

✔ Improve readability with __str__().
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What are Magic Methods?

A. Special methods surrounded by
double underscores that customize
object behavior.

Q. Why are they called Dunder Methods?

A. Because they begin and end with
double underscores (__).

Q. Which magic method is the constructor?

A. __init__()

Q. What is the difference between
__str__() and __repr__()?

A.
__str__()  -> User-friendly output

__repr__() -> Developer representation

Q. What does __call__() do?

A. It allows an object to behave
like a function.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Magic methods customize object behavior.

✔ They integrate custom classes with
Python's built-in functions and operators.

✔ __init__ initializes objects.

✔ __str__ improves readability.

✔ Operator overloading uses methods
like __add__() and __eq__().

✔ Magic methods make Python classes
more powerful and flexible.
""")
