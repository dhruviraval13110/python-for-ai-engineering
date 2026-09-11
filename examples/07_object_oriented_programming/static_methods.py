"""
=========================================================
Python Static Methods
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : static_methods.py

Description
-----------
Static methods are methods that belong to a class but do
not depend on either the class (cls) or the object (self).

They are created using the @staticmethod decorator and
behave like regular functions that are grouped inside a
class for better organization.

Static methods are commonly used for utility functions,
validation, calculations, and helper methods.

Topics Covered
--------------
✔ What are Static Methods?
✔ @staticmethod Decorator
✔ Difference from Instance & Class Methods
✔ Utility Functions
✔ Validation Functions
✔ Mathematical Operations
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("STATIC METHODS")
print("=" * 60)

# =====================================================
# Example 1 - Basic Static Method
# =====================================================

print("\nExample 1 - Basic Static Method")


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))

# =====================================================
# Example 2 - Calling Through Object
# =====================================================

print("\nExample 2 - Calling Through Object")


class Math:

    @staticmethod
    def multiply(a, b):
        return a * b


math = Math()

print(math.multiply(6, 7))

# =====================================================
# Example 3 - Even Number Checker
# =====================================================

print("\nExample 3 - Even Number")


class NumberUtils:

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(NumberUtils.is_even(20))
print(NumberUtils.is_even(13))

# =====================================================
# Example 4 - Temperature Converter
# =====================================================

print("\nExample 4 - Temperature Converter")


class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(30))

# =====================================================
# Example 5 - Email Validation
# =====================================================

print("\nExample 5 - Email Validation")


class Validator:

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


print(Validator.is_valid_email("user@gmail.com"))
print(Validator.is_valid_email("python"))

# =====================================================
# Example 6 - Password Validation
# =====================================================

print("\nExample 6 - Password Validation")


class Security:

    @staticmethod
    def strong_password(password):
        return len(password) >= 8


print(Security.strong_password("Python123"))
print(Security.strong_password("abc"))

# =====================================================
# Example 7 - Area Calculator
# =====================================================

print("\nExample 7 - Area Calculator")


class Geometry:

    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def circle_area(radius):
        return 3.14159 * radius ** 2


print(Geometry.rectangle_area(10, 5))
print(round(Geometry.circle_area(5), 2))

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class DataPreprocessor:

    @staticmethod
    def normalize(data):

        minimum = min(data)
        maximum = max(data)

        return [
            round((value - minimum) / (maximum - minimum), 2)
            for value in data
        ]


dataset = [20, 40, 60, 80, 100]

print(DataPreprocessor.normalize(dataset))

# =====================================================
# Example 9 - Unit Conversion
# =====================================================

print("\nExample 9 - Unit Conversion")


class Converter:

    @staticmethod
    def km_to_miles(km):
        return round(km * 0.621371, 2)


print(Converter.km_to_miles(10))

# =====================================================
# Example 10 - Utility Functions
# =====================================================

print("\nExample 10 - Utility Function")


class StringUtils:

    @staticmethod
    def capitalize_words(text):
        return text.title()


print(StringUtils.capitalize_words("python for ai engineering"))

# =====================================================
# Difference Between Methods
# =====================================================

print("\nDifference Between Methods")

print("""
Instance Method
---------------
✔ Uses self
✔ Works with object data

Class Method
------------
✔ Uses cls
✔ Works with class data

Static Method
-------------
✔ Uses neither self nor cls
✔ Works like a normal utility function
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting @staticmethod.

❌ Using self inside a static method.

❌ Using cls inside a static method.

❌ Using static methods when object
data is required.

❌ Confusing static methods with
class methods.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use static methods for utility functions.

✔ Keep static methods independent.

✔ Do not access instance variables.

✔ Do not modify class variables.

✔ Give meaningful method names.

✔ Keep logic simple and reusable.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a static method?

A. A method that belongs to a class but
does not use self or cls.

Q. Which decorator is used?

A. @staticmethod

Q. Can static methods access instance variables?

A. No.

Q. Can static methods access class variables?

A. Not directly through self or cls.

Q. When should static methods be used?

A. For helper functions, calculations,
validation, and utility operations.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Static methods belong to a class.

✔ They do not use self or cls.

✔ Use @staticmethod decorator.

✔ Best for utility and helper functions.

✔ They improve code organization and
reusability.
""")
