"""
=========================================================
Python Decorators - Introduction
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : decorators_intro.py

Description
-----------
Decorators are a powerful feature in Python that allow you
to modify or extend the behavior of functions and methods
without changing their original code.

Decorators are commonly used for logging, authentication,
performance monitoring, caching, validation, and many
frameworks such as Flask, FastAPI, and Django.

Topics Covered
--------------
✔ What are Decorators?
✔ Basic Decorator
✔ @decorator Syntax
✔ Wrapper Functions
✔ Returning Values
✔ Passing Arguments
✔ Multiple Decorators
✔ functools.wraps
✔ Timing Decorator
✔ Logging Decorator
✔ AI Engineering Example
✔ Best Practices
"""

from functools import wraps
import time

print("=" * 60)
print("PYTHON DECORATORS")
print("=" * 60)

# =====================================================
# Example 1 - Function Without Decorator
# =====================================================

print("\nExample 1 - Without Decorator")


def greet():
    print("Hello, Python!")


greet()

# =====================================================
# Example 2 - Basic Decorator
# =====================================================

print("\nExample 2 - Basic Decorator")


def decorator(func):

    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper


@decorator
def welcome():
    print("Welcome to AI Engineering")


welcome()

# =====================================================
# Example 3 - Decorator with Arguments
# =====================================================

print("\nExample 3 - Decorator with Arguments")


def repeat(func):

    def wrapper(name):
        print("Executing...")
        func(name)

    return wrapper


@repeat
def hello(name):
    print(f"Hello {name}")


hello("Dhruvi")

# =====================================================
# Example 4 - Returning Values
# =====================================================

print("\nExample 4 - Returning Values")


def calculate_decorator(func):

    def wrapper(a, b):
        print("Calculating...")
        return func(a, b)

    return wrapper


@calculate_decorator
def add(a, b):
    return a + b


print(add(10, 20))

# =====================================================
# Example 5 - Using functools.wraps
# =====================================================

print("\nExample 5 - functools.wraps")


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):
    return a * b


print(multiply(5, 6))
print(multiply.__name__)

# =====================================================
# Example 6 - Timing Decorator
# =====================================================

print("\nExample 6 - Timing Decorator")


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end - start:.6f} sec")

        return result

    return wrapper


@timer
def square_numbers():

    total = 0

    for i in range(100000):
        total += i * i

    return total


print(square_numbers())

# =====================================================
# Example 7 - Logging Decorator
# =====================================================

print("\nExample 7 - Logging")


def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log
def login(username):
    print(f"{username} logged in")


login("Dhruvi")

# =====================================================
# Example 8 - Authentication Example
# =====================================================

print("\nExample 8 - Authentication")


def authenticate(func):

    @wraps(func)
    def wrapper(user):

        if user != "admin":
            print("Access Denied")
            return

        return func(user)

    return wrapper


@authenticate
def dashboard(user):
    print(f"Welcome {user}")


dashboard("admin")
dashboard("guest")

# =====================================================
# Example 9 - AI Engineering Example
# =====================================================

print("\nExample 9 - AI Engineering")


def model_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Loading AI Model...")
        result = func(*args, **kwargs)
        print("Prediction Completed")
        return result

    return wrapper


@model_logger
def predict(value):
    return value * 2


print(predict(15))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting to return wrapper.

❌ Forgetting to call func().

❌ Losing metadata without functools.wraps.

❌ Writing overly complex decorators.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use @wraps for every decorator.

✔ Keep decorators reusable.

✔ Decorators should perform one task.

✔ Use decorators for logging,
authentication, caching, and timing.

✔ Keep wrapper functions clean.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a decorator?

A. A function that modifies the behavior
of another function without changing its code.

Q. Why use functools.wraps?

A. It preserves the original function's
metadata such as __name__ and __doc__.

Q. Where are decorators commonly used?

• Logging
• Authentication
• Authorization
• Performance Monitoring
• Caching
• Validation
• Flask
• FastAPI
• Django
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Decorators modify function behavior.

✔ They improve code reusability.

✔ Use @decorator syntax for readability.

✔ functools.wraps preserves metadata.

✔ Decorators are widely used in
professional Python applications.
""")
