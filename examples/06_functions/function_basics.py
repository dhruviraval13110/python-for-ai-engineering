"""
=========================================================
Python Function Basics
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : function_basics.py

Description:
------------
This file introduces Python functions, one of the most
important concepts in programming. Functions help make
code reusable, organized, readable, and easier to maintain.

Topics Covered
--------------
✔ What is a function?
✔ Creating functions
✔ Calling functions
✔ Parameters
✔ Return values
✔ Function naming conventions
✔ Practical examples

"""

# =========================================================
# What is a Function?
# =========================================================

"""
A function is a reusable block of code that performs
a specific task.

Advantages:
------------
• Code Reusability
• Better Organization
• Easier Debugging
• Improved Readability
• Reduced Code Duplication
"""

print("=" * 60)
print("FUNCTION BASICS")
print("=" * 60)


# =========================================================
# Example 1
# Simple Function
# =========================================================

def greet():
    """Print a greeting message."""
    print("Hello, Welcome to Python!")


print("\nExample 1")
greet()


# =========================================================
# Example 2
# Function with Parameters
# =========================================================

def greet_user(name):
    """
    Greet a user by name.

    Parameters:
        name (str): User's name.
    """
    print(f"Hello, {name}!")


print("\nExample 2")
greet_user("Dhruvi")
greet_user("Python Learner")


# =========================================================
# Example 3
# Multiple Parameters
# =========================================================

def student(name, age, course):
    """Display student information."""
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")


print("\nExample 3")
student("Dhruvi", 20, "Artificial Intelligence")


# =========================================================
# Example 4
# Returning a Value
# =========================================================

def add(a, b):
    """
    Return the sum of two numbers.
    """
    return a + b


print("\nExample 4")
result = add(15, 25)

print("Result =", result)


# =========================================================
# Example 5
# Returning Multiple Values
# =========================================================

def calculate(a, b):
    """
    Return multiple arithmetic operations.
    """
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


print("\nExample 5")

add_result, sub_result, mul_result = calculate(10, 5)

print("Addition       :", add_result)
print("Subtraction    :", sub_result)
print("Multiplication :", mul_result)


# =========================================================
# Example 6
# Default Parameters
# =========================================================

def country(name, country_name="India"):
    """
    Demonstrates default parameter values.
    """
    print(f"{name} lives in {country_name}.")


print("\nExample 6")

country("Dhruvi")
country("John", "Canada")


# =========================================================
# Example 7
# Keyword Arguments
# =========================================================

def employee(name, department, salary):
    """Display employee information."""
    print(f"Employee   : {name}")
    print(f"Department : {department}")
    print(f"Salary     : ₹{salary}")


print("\nExample 7")

employee(
    salary=50000,
    name="Aarav",
    department="AI Research"
)


# =========================================================
# Example 8
# Returning Boolean
# =========================================================

def is_even(number):
    """
    Check whether a number is even.
    """
    return number % 2 == 0


print("\nExample 8")

print(is_even(8))
print(is_even(15))


# =========================================================
# Example 9
# Function Calling Another Function
# =========================================================

def square(number):
    """Return square."""
    return number ** 2


def cube(number):
    """Return cube."""
    return number ** 3


print("\nExample 9")

print("Square:", square(4))
print("Cube  :", cube(4))


# =========================================================
# Example 10
# Real-World Example
# BMI Calculator
# =========================================================

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.

    BMI = weight / height²
    """
    return weight / (height ** 2)


print("\nExample 10")

weight = 60
height = 1.70

bmi = calculate_bmi(weight, height)

print(f"BMI = {bmi:.2f}")


# =========================================================
# Function Naming Best Practices
# =========================================================

"""
Good Function Names
-------------------

✔ calculate_salary()
✔ find_maximum()
✔ load_dataset()
✔ preprocess_data()
✔ train_model()
✔ evaluate_model()

Avoid:

✘ f()
✘ abc()
✘ test1()
✘ xyz()

Choose descriptive names that explain what the
function does.
"""


# =========================================================
# AI Engineering Example
# =========================================================

def normalize_scores(scores):
    """
    Normalize a list of scores to the range 0–1.
    """
    minimum = min(scores)
    maximum = max(scores)

    return [
        (score - minimum) / (maximum - minimum)
        for score in scores
    ]


print("\nAI Example")

scores = [50, 65, 80, 95]

print(normalize_scores(scores))


# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Functions make code reusable.
✔ Functions improve readability.
✔ Functions reduce duplication.
✔ Functions can accept parameters.
✔ Functions can return values.
✔ Good naming improves maintainability.
✔ Functions are heavily used in AI and Machine Learning.
""")
