"""
=========================================================
Python Function Best Practices
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : best_practices.py

Description
-----------
Writing good functions is not only about making code work.
Professional developers focus on readability, maintainability,
reusability, and performance.

This file demonstrates the most important best practices
for writing clean and efficient Python functions.

Topics Covered
--------------
✔ Meaningful Function Names
✔ Single Responsibility Principle
✔ Small Functions
✔ Return Instead of Print
✔ Default Parameters
✔ Avoid Global Variables
✔ Type Hints
✔ Docstrings
✔ Error Handling
✔ Real-world Examples
✔ AI Engineering Example
"""

print("=" * 60)
print("FUNCTION BEST PRACTICES")
print("=" * 60)

# =====================================================
# Practice 1 - Use Meaningful Names
# =====================================================

print("\nPractice 1 - Meaningful Names")


def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


print(calculate_area(10, 5))

# =====================================================
# Practice 2 - Keep Functions Small
# =====================================================

print("\nPractice 2 - Small Functions")


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0


print(is_even(20))

# =====================================================
# Practice 3 - Return Instead of Print
# =====================================================

print("\nPractice 3 - Return Instead of Print")


def multiply(a, b):
    return a * b


result = multiply(6, 8)

print(result)

# =====================================================
# Practice 4 - Default Parameters
# =====================================================

print("\nPractice 4 - Default Parameters")


def greet(name="Guest"):
    return f"Welcome, {name}"


print(greet())
print(greet("Dhruvi"))

# =====================================================
# Practice 5 - Type Hints
# =====================================================

print("\nPractice 5 - Type Hints")


def add(a: int, b: int) -> int:
    return a + b


print(add(15, 25))

# =====================================================
# Practice 6 - Docstrings
# =====================================================

print("\nPractice 6 - Docstrings")


def square(number: int) -> int:
    """
    Return the square of a number.

    Parameters:
        number (int): Input value.

    Returns:
        int: Square of the number.
    """
    return number ** 2


print(square(7))

# =====================================================
# Practice 7 - Avoid Global Variables
# =====================================================

print("\nPractice 7 - Avoid Globals")


def increase_salary(current_salary, bonus):
    return current_salary + bonus


print(increase_salary(50000, 5000))

# =====================================================
# Practice 8 - Error Handling
# =====================================================

print("\nPractice 8 - Error Handling")


def divide(a, b):

    if b == 0:
        return "Division by zero is not allowed."

    return a / b


print(divide(20, 5))
print(divide(20, 0))

# =====================================================
# Practice 9 - Single Responsibility
# =====================================================

print("\nPractice 9 - Single Responsibility")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


print(f"BMI: {calculate_bmi(65, 1.72):.2f}")

# =====================================================
# Practice 10 - AI Engineering Example
# =====================================================

print("\nPractice 10 - AI Engineering")


def normalize(scores):

    minimum = min(scores)
    maximum = max(scores)

    return [
        (score - minimum) / (maximum - minimum)
        for score in scores
    ]


dataset = [40, 60, 80, 100]

print(normalize(dataset))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Using unclear function names.

❌ Writing one huge function.

❌ Using global variables.

❌ Printing instead of returning.

❌ Missing documentation.

❌ No error handling.

❌ Ignoring type hints.
""")

# =====================================================
# Best Practices Checklist
# =====================================================

print("\nBest Practices Checklist")

print("""
✔ Keep functions short.

✔ One function = One responsibility.

✔ Use meaningful names.

✔ Return values.

✔ Add type hints.

✔ Write docstrings.

✔ Avoid global variables.

✔ Handle errors gracefully.

✔ Reuse code.

✔ Follow PEP 8 style guide.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Why should functions be small?

A. Small functions are easier to understand,
test, debug, and reuse.

Q. Why should we return values instead of printing?

A. Returned values can be reused elsewhere
in the program.

Q. What is the Single Responsibility Principle?

A. A function should perform only one task.

Q. Why are type hints useful?

A. They improve readability and help IDEs
detect errors.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Write clear and reusable functions.

✔ Keep each function focused on one task.

✔ Prefer return over print.

✔ Add type hints and docstrings.

✔ Handle errors gracefully.

✔ Follow Python coding standards.
""")
