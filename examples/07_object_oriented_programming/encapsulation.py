"""
=========================================================
Python Encapsulation
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : encapsulation.py

Description
-----------
Encapsulation is one of the four fundamental pillars of
Object-Oriented Programming (OOP).

It refers to bundling data (attributes) and methods
(functions) into a single unit (class) while controlling
access to the internal data.

Python supports encapsulation using public, protected,
and private members.

Topics Covered
--------------
✔ What is Encapsulation?
✔ Public Members
✔ Protected Members
✔ Private Members
✔ Name Mangling
✔ Getter & Setter Methods
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("ENCAPSULATION")
print("=" * 60)

# =====================================================
# Example 1 - Public Members
# =====================================================

print("\nExample 1 - Public Members")


class Student:

    def __init__(self, name):
        self.name = name


student = Student("Dhruvi")

print(student.name)

# =====================================================
# Example 2 - Protected Members
# =====================================================

print("\nExample 2 - Protected Members")


class Employee:

    def __init__(self, salary):
        self._salary = salary


employee = Employee(50000)

print(employee._salary)

# =====================================================
# Example 3 - Private Members
# =====================================================

print("\nExample 3 - Private Members")


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(25000)

# print(account.__balance)   # Error

print("Private data cannot be accessed directly.")

# =====================================================
# Example 4 - Getter Method
# =====================================================

print("\nExample 4 - Getter Method")


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(40000)

print(account.get_balance())

# =====================================================
# Example 5 - Setter Method
# =====================================================

print("\nExample 5 - Setter Method")


class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.deposit(15000)

print(account.get_balance())

# =====================================================
# Example 6 - Name Mangling
# =====================================================

print("\nExample 6 - Name Mangling")


class Demo:

    def __init__(self):
        self.__secret = "Python"


demo = Demo()

print(demo._Demo__secret)

# =====================================================
# Example 7 - Student Marks
# =====================================================

print("\nExample 7 - Student Marks")


class Result:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


result = Result(95)

print(result.get_marks())

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class AIModel:

    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.__accuracy = accuracy

    def show_accuracy(self):
        print(f"Accuracy: {self.__accuracy}%")


model = AIModel("Image Classifier", 98.75)

print(model.model_name)

model.show_accuracy()

# =====================================================
# Example 9 - Password Protection
# =====================================================

print("\nExample 9 - Password Protection")


class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def verify_password(self, password):
        return self.__password == password


user = User("dhruvi", "Python@123")

print(user.verify_password("Python@123"))
print(user.verify_password("abc123"))

# =====================================================
# Example 10 - Salary Update
# =====================================================

print("\nExample 10 - Salary Update")


class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def increase_salary(self, amount):

        if amount > 0:
            self.__salary += amount

    def show_salary(self):
        print(f"Salary: ₹{self.__salary}")


employee = Employee(60000)

employee.increase_salary(5000)

employee.show_salary()

# =====================================================
# Public vs Protected vs Private
# =====================================================

print("\nPublic vs Protected vs Private")

print("""
Public
------
name

Accessible everywhere.

Protected
---------
_name

Should only be accessed inside the class
or subclasses (by convention).

Private
-------
__name

Cannot be accessed directly from outside
the class due to name mangling.
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Accessing private variables directly.

❌ Confusing protected with private.

❌ Making every variable private.

❌ Ignoring getter/setter methods.

❌ Breaking encapsulation by exposing
sensitive data.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Keep sensitive data private.

✔ Use getter and setter methods.

✔ Use public members for general access.

✔ Use protected members for inheritance.

✔ Validate data before modifying it.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is encapsulation?

A. Encapsulation is the process of combining
data and methods into one class while
restricting direct access to sensitive data.

Q. What are the three access levels?

• Public
• Protected
• Private

Q. What is name mangling?

A. Python changes the name of private
variables internally to prevent direct access.

Q. Why is encapsulation important?

A. It improves security, maintainability,
and data integrity.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Encapsulation protects object data.

✔ Public members are accessible everywhere.

✔ Protected members use a single underscore (_).

✔ Private members use a double underscore (__).

✔ Getter and setter methods provide controlled
access to private data.

✔ Encapsulation improves security, reliability,
and maintainability of Python applications.
""")
