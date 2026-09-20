"""
=========================================================
Python Real-World Function Examples
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : real_world_examples.py

Description
-----------
Functions are used everywhere in software development.
This file demonstrates practical examples that resemble
real-world applications in automation, banking, e-commerce,
AI, and data processing.

Topics Covered
--------------
✔ Calculator
✔ Student Grade System
✔ BMI Calculator
✔ Bank Account
✔ Shopping Cart
✔ Password Validator
✔ Email Validator
✔ Temperature Converter
✔ AI Data Normalization
✔ Employee Salary Calculator
✔ Invoice Generator
✔ Best Practices
"""

print("=" * 60)
print("REAL-WORLD FUNCTION EXAMPLES")
print("=" * 60)

# =====================================================
# Example 1 - Calculator
# =====================================================

print("\nExample 1 - Calculator")


def calculator(a, b, operator):

    if operator == "+":
        return a + b

    if operator == "-":
        return a - b

    if operator == "*":
        return a * b

    if operator == "/":
        if b == 0:
            return "Division by zero is not allowed."
        return a / b

    return "Invalid Operator"


print(calculator(20, 10, "+"))
print(calculator(20, 10, "*"))

# =====================================================
# Example 2 - Student Grade
# =====================================================

print("\nExample 2 - Student Grade")


def calculate_grade(marks):

    if marks >= 90:
        return "A"

    if marks >= 80:
        return "B"

    if marks >= 70:
        return "C"

    if marks >= 60:
        return "D"

    return "F"


print(calculate_grade(92))
print(calculate_grade(74))

# =====================================================
# Example 3 - BMI Calculator
# =====================================================

print("\nExample 3 - BMI")


def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


print(calculate_bmi(65, 1.72))

# =====================================================
# Example 4 - Bank Account
# =====================================================

print("\nExample 4 - Bank")


def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):

    if amount > balance:
        return "Insufficient Balance"

    return balance - amount


balance = 10000

balance = deposit(balance, 2500)
balance = withdraw(balance, 3000)

print(balance)

# =====================================================
# Example 5 - Shopping Cart
# =====================================================

print("\nExample 5 - Shopping Cart")


def total_bill(*prices):
    return sum(prices)


print(total_bill(500, 999, 250, 150))

# =====================================================
# Example 6 - Password Validator
# =====================================================

print("\nExample 6 - Password")


def validate_password(password):

    if len(password) < 8:
        return False

    return True


print(validate_password("Python123"))
print(validate_password("abc"))

# =====================================================
# Example 7 - Email Validator
# =====================================================

print("\nExample 7 - Email")


def validate_email(email):
    return "@" in email and "." in email


print(validate_email("user@gmail.com"))
print(validate_email("python"))

# =====================================================
# Example 8 - Temperature Converter
# =====================================================

print("\nExample 8 - Temperature")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print(celsius_to_fahrenheit(30))

# =====================================================
# Example 9 - Employee Salary
# =====================================================

print("\nExample 9 - Employee Salary")


def calculate_salary(basic, bonus):
    return basic + bonus


print(calculate_salary(50000, 8000))

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - AI Data Normalization")


def normalize(data):

    minimum = min(data)
    maximum = max(data)

    return [
        round((value - minimum) / (maximum - minimum), 2)
        for value in data
    ]


dataset = [35, 55, 75, 95]

print(normalize(dataset))

# =====================================================
# Example 11 - Invoice Generator
# =====================================================

print("\nExample 11 - Invoice")


def generate_invoice(customer, amount):

    return f"""
----------------------------
        INVOICE
----------------------------
Customer : {customer}
Amount   : ₹{amount}
Status   : Paid
----------------------------
"""


print(generate_invoice("Dhruvi", 2499))

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Writing duplicate code.

❌ One function performing many tasks.

❌ Forgetting to validate inputs.

❌ Not handling errors.

❌ Using print instead of return.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Write reusable functions.

✔ Validate user input.

✔ Return values.

✔ Keep functions small.

✔ Use descriptive names.

✔ Add documentation.

✔ Handle exceptions gracefully.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Functions are the building blocks of
professional Python applications.

✔ They are used in banking, AI, web
development, automation, finance,
healthcare, and e-commerce.

✔ Reusable functions reduce code
duplication and improve maintainability.
""")
