"""
=========================================================
Python Property Decorator (@property)
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : property_decorator.py

Description
-----------
The @property decorator allows us to access methods like
attributes. It provides controlled access to private data
without changing the way users interact with objects.

Properties make code cleaner, safer, and easier to maintain.

Topics Covered
--------------
✔ What is @property?
✔ Getter
✔ Setter
✔ Deleter
✔ Read-only Properties
✔ Validation
✔ Encapsulation with Properties
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("PROPERTY DECORATOR (@property)")
print("=" * 60)

# =====================================================
# Example 1 - Basic Property
# =====================================================

print("\nExample 1 - Basic Property")


class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Dhruvi")

print(student.name)

# =====================================================
# Example 2 - Getter and Setter
# =====================================================

print("\nExample 2 - Getter & Setter")


class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):

        if amount < 0:
            print("Salary cannot be negative.")
            return

        self._salary = amount


employee = Employee(50000)

print(employee.salary)

employee.salary = 65000

print(employee.salary)

# =====================================================
# Example 3 - Validation
# =====================================================

print("\nExample 3 - Validation")


class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            print("Invalid Age")
            return

        self._age = value


person = Person(20)

print(person.age)

person.age = 25

print(person.age)

person.age = -10

# =====================================================
# Example 4 - Read-Only Property
# =====================================================

print("\nExample 4 - Read-Only Property")


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


circle = Circle(5)

print(circle.area)

# =====================================================
# Example 5 - Property Deleter
# =====================================================

print("\nExample 5 - Property Deleter")


class Product:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting Product Name")
        del self._name


product = Product("Laptop")

print(product.name)

del product.name

# =====================================================
# Example 6 - Temperature Converter
# =====================================================

print("\nExample 6 - Temperature")


class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


temperature = Temperature(30)

print(temperature.fahrenheit)

# =====================================================
# Example 7 - Bank Account
# =====================================================

print("\nExample 7 - Bank Account")


class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")


account = BankAccount(10000)

print(account.balance)

account.balance = 15000

print(account.balance)

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class AIModel:

    def __init__(self, accuracy):
        self._accuracy = accuracy

    @property
    def accuracy(self):
        return f"{self._accuracy}%"

    @accuracy.setter
    def accuracy(self, value):

        if 0 <= value <= 100:
            self._accuracy = value
        else:
            print("Accuracy must be between 0 and 100.")


model = AIModel(98.75)

print(model.accuracy)

model.accuracy = 99.20

print(model.accuracy)

# =====================================================
# Example 9 - Student Result
# =====================================================

print("\nExample 9 - Student Result")


class Result:

    def __init__(self, marks):
        self._marks = marks

    @property
    def grade(self):

        if self._marks >= 90:
            return "A"

        if self._marks >= 75:
            return "B"

        if self._marks >= 60:
            return "C"

        return "Fail"


student = Result(88)

print(student.grade)

# =====================================================
# Example 10 - Full Name Property
# =====================================================

print("\nExample 10 - Full Name")


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


user = User("Dhruvi", "Raval")

print(user.full_name)

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting @property decorator.

❌ Using property when a normal method
would be sufficient.

❌ Skipping validation in setters.

❌ Modifying private variables directly.

❌ Returning incorrect data types.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use properties for controlled access.

✔ Validate data inside setters.

✔ Use read-only properties for calculated values.

✔ Keep property methods simple.

✔ Use meaningful property names.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is @property?

A. It converts a method into a read-only attribute.

Q. Why use @property?

A. To provide controlled access to object data.

Q. Which decorators are related to @property?

• @property
• @property.setter
• @property.deleter

Q. Can a property perform validation?

A. Yes, using the setter.

Q. What is a read-only property?

A. A property that has only a getter.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ @property lets methods behave like attributes.

✔ Properties improve encapsulation.

✔ Getters return values safely.

✔ Setters validate and update data.

✔ Deleters remove managed attributes.

✔ Properties are widely used in professional
Python libraries such as Django, FastAPI,
TensorFlow, and PyTorch.
""")
