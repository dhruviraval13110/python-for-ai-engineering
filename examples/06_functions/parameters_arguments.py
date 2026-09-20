"""
=========================================================
Python Parameters & Arguments
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : parameters_arguments.py

Description
-----------
This file explains different types of function parameters
and arguments in Python with practical examples.

Topics Covered
--------------
✔ Positional Arguments
✔ Keyword Arguments
✔ Default Parameters
✔ *args
✔ **kwargs
✔ Positional-only Parameters
✔ Keyword-only Parameters
✔ Argument Unpacking
✔ Practical Examples
✔ AI Engineering Examples
"""

print("=" * 60)
print("PARAMETERS & ARGUMENTS")
print("=" * 60)

# =====================================================
# 1. Positional Arguments
# =====================================================

print("\n1. Positional Arguments")


def introduce(name, age):
    """Display basic information."""
    print(f"Name : {name}")
    print(f"Age  : {age}")


introduce("Dhruvi", 20)

# Order matters:
# introduce(20, "Dhruvi")  # Wrong order


# =====================================================
# 2. Keyword Arguments
# =====================================================

print("\n2. Keyword Arguments")


def employee(name, department, salary):
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Salary     : ₹{salary}")


employee(
    salary=50000,
    department="AI",
    name="Dhruvi"
)

# Order doesn't matter when keywords are used.


# =====================================================
# 3. Default Parameters
# =====================================================

print("\n3. Default Parameters")


def greet(name, country="India"):
    print(f"{name} lives in {country}.")


greet("Dhruvi")
greet("John", "Canada")


# =====================================================
# 4. Multiple Default Parameters
# =====================================================

print("\n4. Multiple Default Parameters")


def create_account(username, active=True, role="User"):
    print(username)
    print(active)
    print(role)


create_account("dhruvi")
create_account("admin", True, "Administrator")


# =====================================================
# 5. Positional + Keyword Together
# =====================================================

print("\n5. Mixed Arguments")


def student(name, age, course):
    print(name)
    print(age)
    print(course)


student("Dhruvi", course="AI", age=20)


# =====================================================
# 6. *args
# =====================================================

print("\n6. *args")


def add_numbers(*numbers):
    """
    Accept any number of positional arguments.
    """
    total = sum(numbers)
    return total


print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(5, 10, 15, 20, 25))


# =====================================================
# 7. **kwargs
# =====================================================

print("\n7. **kwargs")


def profile(**details):
    """
    Accept any number of keyword arguments.
    """
    for key, value in details.items():
        print(f"{key} : {value}")


profile(
    name="Dhruvi",
    age=20,
    course="AI Engineering",
    city="Ahmedabad"
)


# =====================================================
# 8. Combining Parameters
# =====================================================

print("\n8. Combining Everything")


def company(name, *skills, city="Ahmedabad", **extra):
    print("Name :", name)

    print("\nSkills")
    for skill in skills:
        print("-", skill)

    print("\nCity :", city)

    print("\nExtra Information")

    for key, value in extra.items():
        print(key, ":", value)


company(
    "Dhruvi",
    "Python",
    "Machine Learning",
    "Git",
    city="Gandhinagar",
    experience="Fresher",
    internship=True
)


# =====================================================
# 9. Positional-only Parameters
# =====================================================

print("\n9. Positional-only Parameters")


def divide(a, b, /):
    return a / b


print(divide(20, 5))

# divide(a=20, b=5)
# This would raise an error.


# =====================================================
# 10. Keyword-only Parameters
# =====================================================

print("\n10. Keyword-only Parameters")


def create_user(name, *, role="Student"):
    print(name)
    print(role)


create_user("Dhruvi", role="Developer")

# create_user("Dhruvi", "Developer")
# Not allowed.


# =====================================================
# 11. Argument Unpacking
# =====================================================

print("\n11. Argument Unpacking")

numbers = (5, 10)

print(divide(*numbers))

student_info = {
    "name": "Dhruvi",
    "age": 20,
    "course": "AI"
}

student(**student_info)


# =====================================================
# 12. Real World Example
# =====================================================

print("\n12. Shopping Cart")


def shopping_cart(customer, *items):
    print(f"Customer : {customer}")

    print("Purchased Items:")

    for item in items:
        print("-", item)


shopping_cart(
    "Dhruvi",
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
)


# =====================================================
# 13. AI Engineering Example
# =====================================================

print("\n13. AI Example")


def train_model(
    dataset,
    epochs=10,
    learning_rate=0.001,
    optimizer="Adam"
):
    print("Dataset       :", dataset)
    print("Epochs        :", epochs)
    print("Learning Rate :", learning_rate)
    print("Optimizer     :", optimizer)


train_model(
    "MNIST",
    epochs=20,
    learning_rate=0.0005
)


# =====================================================
# 14. Common Mistakes
# =====================================================

print("\n14. Common Mistakes")

print("""
❌ Wrong argument order

❌ Missing required arguments

❌ Duplicate keyword arguments

❌ Mutable default values

Example (Avoid):

def add_item(item, items=[]):
    items.append(item)
    return items

Use:

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
""")


# =====================================================
# 15. Best Practices
# =====================================================

print("\n15. Best Practices")

print("""
✔ Use meaningful parameter names.

✔ Keep functions short.

✔ Prefer keyword arguments
   for many parameters.

✔ Avoid mutable default values.

✔ Use type hints.

✔ Document parameters.

✔ Return values instead of printing
   whenever possible.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Positional Arguments
✔ Keyword Arguments
✔ Default Parameters
✔ *args
✔ **kwargs
✔ Positional-only Parameters
✔ Keyword-only Parameters
✔ Argument Unpacking
✔ AI Engineering Examples
✔ Best Practices
""")
