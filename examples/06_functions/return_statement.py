"""
=========================================================
Python Return Statement
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : return_statement.py

Description
-----------
The return statement is used to send a value back from a
function to the caller.

Instead of printing values directly, functions should
usually return data so it can be reused elsewhere.

Topics Covered
--------------
✔ Returning a single value
✔ Returning multiple values
✔ Returning lists
✔ Returning dictionaries
✔ Returning None
✔ Early return
✔ Nested function calls
✔ Recursive return
✔ Real-world examples
✔ AI Engineering example
✔ Best practices
"""

print("=" * 60)
print("RETURN STATEMENT")
print("=" * 60)

# =====================================================
# Example 1
# Returning a Single Value
# =====================================================

print("\nExample 1")


def square(number):
    """Return the square of a number."""
    return number ** 2


result = square(5)

print("Square:", result)

# =====================================================
# Example 2
# Returning Addition
# =====================================================

print("\nExample 2")


def add(a, b):
    return a + b


print(add(10, 20))

# =====================================================
# Example 3
# Returning Multiple Values
# =====================================================

print("\nExample 3")


def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division


add_result, sub_result, mul_result, div_result = calculate(20, 5)

print("Addition       :", add_result)
print("Subtraction    :", sub_result)
print("Multiplication :", mul_result)
print("Division       :", div_result)

# =====================================================
# Example 4
# Returning a List
# =====================================================

print("\nExample 4")


def even_numbers(limit):
    numbers = []

    for number in range(limit + 1):

        if number % 2 == 0:
            numbers.append(number)

    return numbers


print(even_numbers(20))

# =====================================================
# Example 5
# Returning a Dictionary
# =====================================================

print("\nExample 5")


def student():
    return {
        "name": "Dhruvi",
        "age": 20,
        "course": "AI Engineering"
    }


print(student())

# =====================================================
# Example 6
# Returning Boolean
# =====================================================

print("\nExample 6")


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


print(is_prime(17))
print(is_prime(20))

# =====================================================
# Example 7
# Returning None
# =====================================================

print("\nExample 7")


def hello():
    print("Hello Python")


value = hello()

print("Returned Value:", value)

# =====================================================
# Example 8
# Early Return
# =====================================================

print("\nExample 8")


def check_age(age):

    if age < 18:
        return "Minor"

    return "Adult"


print(check_age(16))
print(check_age(25))

# =====================================================
# Example 9
# Returning a Tuple
# =====================================================

print("\nExample 9")


def rectangle(length, width):

    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter


area, perimeter = rectangle(10, 5)

print("Area      :", area)
print("Perimeter :", perimeter)

# =====================================================
# Example 10
# Returning a Function
# =====================================================

print("\nExample 10")


def outer():

    def inner():
        return "Hello from Inner Function"

    return inner


message = outer()

print(message())

# =====================================================
# Example 11
# Recursive Return
# =====================================================

print("\nExample 11")


def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))

# =====================================================
# Example 12
# Real World Example
# BMI Calculator
# =====================================================

print("\nExample 12")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


bmi = calculate_bmi(65, 1.72)

print(f"BMI = {bmi:.2f}")

# =====================================================
# Example 13
# Shopping Cart
# =====================================================

print("\nExample 13")


def total_price(prices):
    return sum(prices)


cart = [1200, 350, 599, 249]

print("Total =", total_price(cart))

# =====================================================
# Example 14
# AI Engineering Example
# =====================================================

print("\nExample 14")


def normalize(data):

    minimum = min(data)
    maximum = max(data)

    normalized = []

    for value in data:
        normalized.append(
            (value - minimum) / (maximum - minimum)
        )

    return normalized


dataset = [25, 50, 75, 100]

print(normalize(dataset))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Printing instead of returning

def add(a, b):
    print(a + b)

Better:

def add(a, b):
    return a + b
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Return values instead of print()

✔ Keep return types consistent

✔ Use early return for cleaner logic

✔ Return meaningful objects

✔ Use type hints

✔ Write proper docstrings
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Return sends data back to the caller.

✔ A function can return:
    • Integer
    • Float
    • String
    • Boolean
    • List
    • Tuple
    • Dictionary
    • Another Function

✔ Every function returns something.

✔ If no return statement is used,
  Python automatically returns None.

✔ Returning values makes code reusable,
  testable and cleaner.
""")
