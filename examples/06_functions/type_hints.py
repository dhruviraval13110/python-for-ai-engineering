"""
=========================================================
Python Type Hints
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : type_hints.py

Description
-----------
Type hints allow you to specify the expected data types
of variables, function parameters, and return values.

Although Python is dynamically typed, type hints improve
code readability, editor support, static analysis, and
maintainability.

Topics Covered
--------------
✔ Introduction to Type Hints
✔ Parameter Type Hints
✔ Return Type Hints
✔ Variable Type Hints
✔ Optional Types
✔ Union Types
✔ List, Tuple & Dictionary Types
✔ Any Type
✔ Type Aliases
✔ AI Engineering Example
✔ Real-world Example
✔ Best Practices
"""

from typing import Any, Optional, Union

print("=" * 60)
print("TYPE HINTS")
print("=" * 60)

# =====================================================
# Example 1 - Parameter Type Hints
# =====================================================

print("\nExample 1 - Parameter Type Hints")


def greet(name: str) -> None:
    print(f"Hello, {name}")


greet("Dhruvi")

# =====================================================
# Example 2 - Return Type Hint
# =====================================================

print("\nExample 2 - Return Type Hint")


def square(number: int) -> int:
    return number ** 2


print(square(5))

# =====================================================
# Example 3 - Multiple Parameters
# =====================================================

print("\nExample 3 - Multiple Parameters")


def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))

# =====================================================
# Example 4 - Float Type
# =====================================================

print("\nExample 4 - Float Type")


def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


print(calculate_bmi(65.0, 1.72))

# =====================================================
# Example 5 - List Type Hint
# =====================================================

print("\nExample 5 - List Type")


def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))

# =====================================================
# Example 6 - Dictionary Type Hint
# =====================================================

print("\nExample 6 - Dictionary Type")


def student() -> dict[str, str]:
    return {
        "name": "Dhruvi",
        "course": "AI Engineering"
    }


print(student())

# =====================================================
# Example 7 - Optional Type
# =====================================================

print("\nExample 7 - Optional")


def welcome(name: Optional[str]) -> str:

    if name is None:
        return "Guest"

    return name


print(welcome("Rahul"))
print(welcome(None))

# =====================================================
# Example 8 - Union Type
# =====================================================

print("\nExample 8 - Union")


def display(value: Union[int, float, str]) -> None:
    print(value)


display(100)
display(3.14)
display("Python")

# =====================================================
# Example 9 - Any Type
# =====================================================

print("\nExample 9 - Any")


def show(data: Any) -> None:
    print(data)


show(100)
show("AI")
show([1, 2, 3])

# =====================================================
# Example 10 - Tuple Type
# =====================================================

print("\nExample 10 - Tuple")


def coordinates() -> tuple[int, int]:
    return (10, 20)


print(coordinates())

# =====================================================
# Example 11 - AI Engineering Example
# =====================================================

print("\nExample 11 - AI Engineering")


def normalize(scores: list[float]) -> list[float]:

    minimum = min(scores)
    maximum = max(scores)

    return [
        (score - minimum) / (maximum - minimum)
        for score in scores
    ]


print(normalize([25.0, 50.0, 75.0, 100.0]))

# =====================================================
# Example 12 - Real-world Example
# =====================================================

print("\nExample 12 - Bank Account")


def deposit(balance: float, amount: float) -> float:
    return balance + amount


print(deposit(5000.0, 2500.0))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Thinking type hints enforce types.

❌ Forgetting return type hints.

❌ Using incorrect type annotations.

❌ Ignoring Optional when None is allowed.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Add type hints to public functions.

✔ Use meaningful return types.

✔ Use Optional for nullable values.

✔ Keep annotations consistent.

✔ Combine type hints with docstrings.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What are type hints?

A. They specify expected data types for
parameters, variables, and return values.

Q. Do type hints enforce data types?

A. No. They improve readability and help
tools like IDEs and static type checkers.

Q. Which module provides Optional, Union,
and Any?

A. typing
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Type hints improve code readability.

✔ They help IDEs detect errors early.

✔ Python remains dynamically typed.

✔ Common types:
   • int
   • float
   • str
   • bool
   • list
   • tuple
   • dict
   • Optional
   • Union
   • Any

✔ Type hints are recommended for
professional Python projects.
""")
