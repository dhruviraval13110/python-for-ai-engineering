"""
=========================================================
Python Lambda Functions
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : lambda_functions.py

Description
-----------
Lambda functions are small anonymous functions written
using the 'lambda' keyword.

They are useful for short operations and are commonly used
with functions like map(), filter(), sorted(), and reduce().

Topics Covered
--------------
✔ Lambda Basics
✔ Multiple Arguments
✔ Conditional Lambda
✔ map()
✔ filter()
✔ reduce()
✔ sorted() with key
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

from functools import reduce

print("=" * 60)
print("LAMBDA FUNCTIONS")
print("=" * 60)

# =====================================================
# Example 1 - Basic Lambda
# =====================================================

print("\nExample 1 - Basic Lambda")

square = lambda x: x ** 2

print(square(5))

# =====================================================
# Example 2 - Multiple Arguments
# =====================================================

print("\nExample 2 - Multiple Arguments")

add = lambda a, b: a + b

print(add(10, 20))

# =====================================================
# Example 3 - Conditional Lambda
# =====================================================

print("\nExample 3 - Conditional Lambda")

maximum = lambda a, b: a if a > b else b

print(maximum(15, 40))

# =====================================================
# Example 4 - map()
# =====================================================

print("\nExample 4 - map()")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

# =====================================================
# Example 5 - filter()
# =====================================================

print("\nExample 5 - filter()")

numbers = [10, 15, 20, 25, 30, 35]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# =====================================================
# Example 6 - reduce()
# =====================================================

print("\nExample 6 - reduce()")

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)

print(total)

# =====================================================
# Example 7 - sorted()
# =====================================================

print("\nExample 7 - sorted()")

students = [
    ("Dhruvi", 88),
    ("Rahul", 75),
    ("Amit", 95),
    ("Neha", 82)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)

# =====================================================
# Example 8 - Sorting Dictionary
# =====================================================

print("\nExample 8 - Sorting Dictionary")

employees = [
    {"name": "A", "salary": 45000},
    {"name": "B", "salary": 60000},
    {"name": "C", "salary": 52000}
]

employees = sorted(
    employees,
    key=lambda emp: emp["salary"]
)

print(employees)

# =====================================================
# Example 9 - Real World Example
# =====================================================

print("\nExample 9 - Product Discount")

prices = [500, 1200, 800, 300]

discount_prices = list(
    map(lambda price: price * 0.9, prices)
)

print(discount_prices)

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - Normalize Scores")

scores = [55, 72, 91, 65]

maximum = max(scores)

normalized = list(
    map(lambda score: round(score / maximum, 2), scores)
)

print(normalized)

# =====================================================
# Example 11 - String Operations
# =====================================================

print("\nExample 11 - String Operations")

names = ["dhruvi", "rahul", "amit"]

capitalized = list(
    map(lambda name: name.title(), names)
)

print(capitalized)

# =====================================================
# Example 12 - Filter Passing Students
# =====================================================

print("\nExample 12 - Passing Students")

marks = [35, 62, 80, 29, 91, 48]

passed = list(
    filter(lambda mark: mark >= 40, marks)
)

print(passed)

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Writing long lambda functions

❌ Using lambda where a normal function
would be easier to read.

❌ Adding multiple statements inside lambda.
(Lambda supports only one expression.)
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Keep lambda functions short.

✔ Use lambda for simple operations.

✔ Use def for complex logic.

✔ Combine lambda with map(), filter(),
sorted(), and reduce().

✔ Prefer readability over clever code.
""")

# =====================================================
# Interview Notes
# =====================================================

print("\nInterview Notes")

print("""
Q. What is a lambda function?

A. An anonymous function written using
the lambda keyword.

Q. Can lambda contain multiple statements?

A. No.

Q. When should lambda be used?

A. For short, simple functions that are
used only once.

Q. Which built-in functions commonly use lambda?

• map()
• filter()
• reduce()
• sorted()
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Lambda functions are anonymous functions.

✔ They contain only one expression.

✔ Commonly used with:
    • map()
    • filter()
    • reduce()
    • sorted()

✔ Use lambda for concise, readable code.

✔ For complex logic, prefer normal functions.
""")
