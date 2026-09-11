"""
=========================================================
Python Docstrings
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : docstrings.py

Description
-----------
Docstrings are string literals used to document Python
functions, classes, and modules.

They help developers understand what the code does and
are accessible using the help() function and __doc__
attribute.

Topics Covered
--------------
✔ Function Docstrings
✔ Single-line Docstrings
✔ Multi-line Docstrings
✔ Module Docstrings
✔ Class Docstrings
✔ Accessing Docstrings
✔ Type Hints with Docstrings
✔ Best Practices
✔ Real-world Examples
"""

print("=" * 60)
print("DOCSTRINGS")
print("=" * 60)

# =====================================================
# Example 1 - Simple Docstring
# =====================================================

print("\nExample 1")


def greet():
    """Display a welcome message."""
    print("Welcome to Python!")


greet()

# =====================================================
# Example 2 - Accessing a Docstring
# =====================================================

print("\nExample 2")

print(greet.__doc__)

# =====================================================
# Example 3 - Function with Parameters
# =====================================================

print("\nExample 3")


def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of two numbers.
    """
    return a + b


print(add(10, 20))

# =====================================================
# Example 4 - Multi-line Docstring
# =====================================================

print("\nExample 4")


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Formula:
        BMI = weight / height²

    Parameters:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: BMI value.
    """
    return weight / (height ** 2)


print(calculate_bmi(65, 1.72))

# =====================================================
# Example 5 - help()
# =====================================================

print("\nExample 5")

help(add)

# =====================================================
# Example 6 - Module Docstring
# =====================================================

print("\nExample 6")

print(__doc__)

# =====================================================
# Example 7 - Class Docstring
# =====================================================

print("\nExample 7")


class Student:
    """
    Represents a student.

    Attributes:
        name (str)
        age (int)
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Student.__doc__)

# =====================================================
# Example 8 - Method Docstring
# =====================================================

print("\nExample 8")


class Calculator:

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Returns:
            int
        """
        return a * b


calc = Calculator()

print(calc.multiply(5, 6))

# =====================================================
# Example 9 - AI Engineering Example
# =====================================================

print("\nExample 9")


def normalize(data):
    """
    Normalize values between 0 and 1.

    Parameters:
        data (list)

    Returns:
        list
    """

    minimum = min(data)
    maximum = max(data)

    return [
        (value - minimum) / (maximum - minimum)
        for value in data
    ]


print(normalize([10, 20, 30, 40]))

# =====================================================
# Example 10 - Real World Example
# =====================================================

print("\nExample 10")


def login(username, password):
    """
    Authenticate a user.

    Parameters:
        username (str)
        password (str)

    Returns:
        bool
    """

    return username == "admin" and password == "1234"


print(login("admin", "1234"))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Writing unclear docstrings.

❌ Forgetting parameter descriptions.

❌ Not updating docstrings after
changing the function.

❌ Using comments instead of docstrings.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Write meaningful descriptions.

✔ Explain parameters.

✔ Explain return values.

✔ Keep docstrings updated.

✔ Follow a consistent format.

✔ Write docstrings for public functions.
""")

# =====================================================
# Interview Notes
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a docstring?

A. A string literal used to document
functions, classes, and modules.

Q. How do you access a docstring?

• help(function)
• function.__doc__

Q. Are comments and docstrings the same?

No.

Comments are ignored by Python.
Docstrings become part of the object.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Docstrings document code.

✔ They improve readability.

✔ They work with help().

✔ Access them using __doc__.

✔ Essential for professional Python code.
""")
