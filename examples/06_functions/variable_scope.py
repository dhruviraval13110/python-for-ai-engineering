"""
=========================================================
Python Variable Scope
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : variable_scope.py

Description
-----------
Variable scope determines where a variable can be accessed
within a Python program.

Topics Covered
--------------
✔ Local Variables
✔ Global Variables
✔ global Keyword
✔ nonlocal Keyword
✔ LEGB Rule
✔ Variable Shadowing
✔ Best Practices
✔ Real-world Examples
✔ AI Engineering Example
"""

print("=" * 60)
print("VARIABLE SCOPE")
print("=" * 60)

# =====================================================
# Example 1
# Local Variable
# =====================================================

print("\nExample 1 - Local Variable")


def student():
    name = "Dhruvi"
    print("Inside Function:", name)


student()

# print(name)  # NameError


# =====================================================
# Example 2
# Global Variable
# =====================================================

print("\nExample 2 - Global Variable")

language = "Python"


def show_language():
    print("Programming Language:", language)


show_language()
print(language)


# =====================================================
# Example 3
# Local and Global Variable
# =====================================================

print("\nExample 3 - Local vs Global")

city = "Ahmedabad"


def location():
    city = "Gandhinagar"
    print("Inside Function :", city)


location()

print("Outside Function:", city)


# =====================================================
# Example 4
# global Keyword
# =====================================================

print("\nExample 4 - global Keyword")

counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()

print("Counter:", counter)


# =====================================================
# Example 5
# Variable Shadowing
# =====================================================

print("\nExample 5 - Variable Shadowing")

number = 100


def demo():
    number = 50
    print("Inside:", number)


demo()

print("Outside:", number)


# =====================================================
# Example 6
# Nested Functions
# =====================================================

print("\nExample 6 - Nested Functions")


def outer():

    message = "Outer Function"

    def inner():
        print(message)

    inner()


outer()


# =====================================================
# Example 7
# nonlocal Keyword
# =====================================================

print("\nExample 7 - nonlocal")


def counter_function():

    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()
    increment()
    increment()


counter_function()


# =====================================================
# Example 8
# LEGB Rule
# =====================================================

print("\nExample 8 - LEGB Rule")

text = "Global"


def first():

    text = "Enclosing"

    def second():

        text = "Local"

        print(text)

    second()


first()

print(text)

"""
LEGB

L -> Local
E -> Enclosing
G -> Global
B -> Built-in
"""


# =====================================================
# Example 9
# Built-in Scope
# =====================================================

print("\nExample 9 - Built-in")

numbers = [10, 20, 30]

print(max(numbers))
print(min(numbers))
print(sum(numbers))


# =====================================================
# Example 10
# AI Engineering Example
# =====================================================

print("\nExample 10 - AI Example")

MODEL_NAME = "Random Forest"


def train_model():

    epochs = 10

    print("Model :", MODEL_NAME)
    print("Epochs:", epochs)


train_model()


# =====================================================
# Example 11
# Real World Example
# =====================================================

print("\nExample 11 - Bank Balance")

balance = 5000


def deposit(amount):
    global balance
    balance += amount


deposit(2000)

print("Balance:", balance)


# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Modifying a global variable without
using the global keyword.

❌ Creating too many global variables.

❌ Using globals everywhere.

❌ Forgetting variable scope.
""")


# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Prefer local variables.

✔ Minimize global variables.

✔ Use constants for global settings.

✔ Pass values as parameters.

✔ Return values instead of modifying globals.

✔ Keep functions independent.
""")


# =====================================================
# Interview Notes
# =====================================================

print("\nInterview Notes")

print("""
Q. What is variable scope?

A. Scope determines where a variable
can be accessed.

Q. Difference between local and global?

A. Local variables exist only inside
the function.

Global variables can be accessed
throughout the program.

Q. What is LEGB?

L -> Local
E -> Enclosing
G -> Global
B -> Built-in
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Local variables exist only inside functions.

✔ Global variables can be accessed anywhere.

✔ global modifies global variables.

✔ nonlocal modifies enclosing variables.

✔ Python follows the LEGB lookup rule.

✔ Prefer local variables whenever possible.
""")
