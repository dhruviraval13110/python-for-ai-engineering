"""
=========================================================
Python Class Methods
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : class_methods.py

Description
-----------
Class methods are methods that operate on the class itself
instead of individual objects.

They use the @classmethod decorator and receive the class
(cls) as the first parameter instead of self.

Class methods are commonly used to modify class variables,
create alternative constructors, and perform operations
related to the class.

Topics Covered
--------------
✔ What are Class Methods?
✔ @classmethod Decorator
✔ cls Parameter
✔ Accessing Class Variables
✔ Modifying Class Variables
✔ Alternative Constructors
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("CLASS METHODS")
print("=" * 60)

# =====================================================
# Example 1 - Basic Class Method
# =====================================================

print("\nExample 1 - Basic Class Method")


class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(f"School: {cls.school}")


Student.show_school()

# =====================================================
# Example 2 - Modifying Class Variable
# =====================================================

print("\nExample 2 - Modify Class Variable")


class Company:

    company_name = "OpenAI"

    @classmethod
    def change_company(cls, name):
        cls.company_name = name


print("Before:", Company.company_name)

Company.change_company("NexxFlow")

print("After :", Company.company_name)

# =====================================================
# Example 3 - Calling Through an Object
# =====================================================

print("\nExample 3 - Calling Through an Object")


class College:

    college_name = "Government Engineering College"

    @classmethod
    def display(cls):
        print(cls.college_name)


student = College()

student.display()

# =====================================================
# Example 4 - Object Counter
# =====================================================

print("\nExample 4 - Counting Objects")


class Employee:

    total_employees = 0

    def __init__(self):
        Employee.total_employees += 1

    @classmethod
    def show_total(cls):
        print(f"Total Employees: {cls.total_employees}")


Employee()
Employee()
Employee()

Employee.show_total()

# =====================================================
# Example 5 - Alternative Constructor
# =====================================================

print("\nExample 5 - Alternative Constructor")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Dhruvi-20")

print(student.name)
print(student.age)

# =====================================================
# Example 6 - Bank Example
# =====================================================

print("\nExample 6 - Bank")


class Bank:

    bank_name = "State Bank of India"

    @classmethod
    def update_bank_name(cls, name):
        cls.bank_name = name


print(Bank.bank_name)

Bank.update_bank_name("Reserve Bank")

print(Bank.bank_name)

# =====================================================
# Example 7 - AI Engineering Example
# =====================================================

print("\nExample 7 - AI Engineering")


class AIModel:

    framework = "TensorFlow"

    def __init__(self, model_name):
        self.model_name = model_name

    @classmethod
    def change_framework(cls, framework):
        cls.framework = framework


print("Before:", AIModel.framework)

AIModel.change_framework("PyTorch")

print("After :", AIModel.framework)

# =====================================================
# Example 8 - Creating Object Using Class Method
# =====================================================

print("\nExample 8 - Create Object")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def create_default_product(cls):
        return cls("Laptop", 50000)


product = Product.create_default_product()

print(product.name)
print(product.price)

# =====================================================
# Example 9 - Access Class Variable
# =====================================================

print("\nExample 9 - Access Class Variable")


class Car:

    wheels = 4

    @classmethod
    def display(cls):
        print(cls.wheels)


Car.display()

# =====================================================
# Example 10 - Multiple Objects Share Class Variable
# =====================================================

print("\nExample 10 - Shared Data")


class Mobile:

    company = "Samsung"

    def __init__(self, model):
        self.model = model

    @classmethod
    def change_company(cls, company):
        cls.company = company


mobile1 = Mobile("Galaxy S25")
mobile2 = Mobile("Galaxy A56")

print(mobile1.company)
print(mobile2.company)

Mobile.change_company("Google")

print(mobile1.company)
print(mobile2.company)

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting @classmethod.

❌ Using self instead of cls.

❌ Modifying instance variables using cls.

❌ Confusing class methods with static methods.

❌ Using class methods when instance methods
are more appropriate.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use cls as the first parameter.

✔ Use class methods for shared data.

✔ Use alternative constructors when needed.

✔ Keep class methods focused on class-level tasks.

✔ Modify class variables using cls.variable.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a class method?

A. A method that operates on the class
instead of an object.

Q. Which decorator is used?

A. @classmethod

Q. What is the first parameter?

A. cls

Q. Can class methods modify class variables?

A. Yes.

Q. Can class methods create objects?

A. Yes, they are often used as
alternative constructors.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Class methods work with the class itself.

✔ They use the @classmethod decorator.

✔ cls refers to the class.

✔ Class methods are ideal for managing
shared class data.

✔ They are commonly used for alternative
constructors and class-level operations.
""")
