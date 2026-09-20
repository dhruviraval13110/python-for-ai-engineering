"""
=========================================================
Python *args and **kwargs
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : args_kwargs.py

Description
-----------
*args and **kwargs allow functions to accept a variable
number of arguments.

*args collects extra positional arguments into a tuple,
while **kwargs collects extra keyword arguments into a
dictionary.

Topics Covered
--------------
✔ *args
✔ **kwargs
✔ Packing Arguments
✔ Unpacking Arguments
✔ Combining *args and **kwargs
✔ Argument Unpacking
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("*ARGS AND **KWARGS")
print("=" * 60)

# =====================================================
# Example 1 - *args
# =====================================================

print("\nExample 1 - *args")


def add_numbers(*numbers):
    """Return the sum of all numbers."""
    return sum(numbers)


print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))

# =====================================================
# Example 2 - Iterating over *args
# =====================================================

print("\nExample 2 - Iterating *args")


def display_names(*names):
    for name in names:
        print(name)


display_names("Dhruvi", "Rahul", "Amit")

# =====================================================
# Example 3 - **kwargs
# =====================================================

print("\nExample 3 - **kwargs")


def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


student_info(
    name="Dhruvi",
    age=20,
    course="AI Engineering"
)

# =====================================================
# Example 4 - Combining Parameters
# =====================================================

print("\nExample 4 - Mixed Parameters")


def employee(name, salary, *skills):
    print("Name   :", name)
    print("Salary :", salary)
    print("Skills :", skills)


employee(
    "Dhruvi",
    50000,
    "Python",
    "SQL",
    "Machine Learning"
)

# =====================================================
# Example 5 - *args and **kwargs Together
# =====================================================

print("\nExample 5")


def demo(*args, **kwargs):
    print("Args   :", args)
    print("Kwargs :", kwargs)


demo(
    10,
    20,
    30,
    city="Ahmedabad",
    country="India"
)

# =====================================================
# Example 6 - Packing Arguments
# =====================================================

print("\nExample 6 - Packing")


def numbers(*values):
    print(values)


numbers(1, 2, 3, 4, 5)

# =====================================================
# Example 7 - Unpacking List
# =====================================================

print("\nExample 7 - Unpacking List")


def multiply(a, b, c):
    return a * b * c


values = [2, 3, 4]

print(multiply(*values))

# =====================================================
# Example 8 - Unpacking Dictionary
# =====================================================

print("\nExample 8 - Unpacking Dictionary")


def profile(name, age):
    print(name, age)


person = {
    "name": "Dhruvi",
    "age": 20
}

profile(**person)

# =====================================================
# Example 9 - Shopping Cart
# =====================================================

print("\nExample 9 - Shopping Cart")


def total_bill(*prices):
    return sum(prices)


print(total_bill(150, 250, 400, 99))

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - AI Model")


def train_model(model_name, **config):
    print("Model:", model_name)

    for key, value in config.items():
        print(f"{key}: {value}")


train_model(
    "Random Forest",
    epochs=20,
    learning_rate=0.01,
    batch_size=32
)

# =====================================================
# Example 11 - Keyword Settings
# =====================================================

print("\nExample 11")


def settings(**options):
    for key, value in options.items():
        print(key, "=", value)


settings(
    theme="Dark",
    language="English",
    notifications=True
)

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting * before args

❌ Forgetting ** before kwargs

❌ Using kwargs before args

❌ Passing duplicate keyword arguments
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use *args for variable positional arguments.

✔ Use **kwargs for optional keyword arguments.

✔ Prefer meaningful parameter names.

✔ Keep function signatures readable.

✔ Use unpacking to simplify function calls.
""")

# =====================================================
# Interview Notes
# =====================================================

print("\nInterview Questions")

print("""
Q. What is *args?

A. It collects multiple positional
arguments into a tuple.

Q. What is **kwargs?

A. It collects keyword arguments into
a dictionary.

Q. Difference between packing and unpacking?

Packing:
    def func(*args)

Unpacking:
    func(*list_values)

Dictionary unpacking:
    func(**dictionary)
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ *args stores positional arguments.

✔ **kwargs stores keyword arguments.

✔ Use * to unpack lists and tuples.

✔ Use ** to unpack dictionaries.

✔ *args and **kwargs make functions
flexible and reusable.
""")
