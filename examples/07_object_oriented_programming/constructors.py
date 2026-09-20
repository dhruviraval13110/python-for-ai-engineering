"""
=========================================================
Python Constructors (__init__)
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : constructors.py

Description
-----------
A constructor is a special method in Python that is
automatically called whenever an object is created.

The constructor is used to initialize object attributes
with default or user-provided values.

In Python, the constructor is written using the
__init__() method.

Topics Covered
--------------
✔ What is a Constructor?
✔ __init__ Method
✔ Initializing Objects
✔ Default Parameters
✔ Multiple Attributes
✔ Multiple Objects
✔ Constructor with Methods
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("PYTHON CONSTRUCTORS (__init__)")
print("=" * 60)

# =====================================================
# Example 1 - Simple Constructor
# =====================================================

print("\nExample 1 - Simple Constructor")


class Student:

    def __init__(self):
        print("Student object created!")


student = Student()

# =====================================================
# Example 2 - Constructor with Parameters
# =====================================================

print("\nExample 2 - Constructor with Parameters")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Dhruvi", 20)

print(student.name)
print(student.age)

# =====================================================
# Example 3 - Multiple Objects
# =====================================================

print("\nExample 3 - Multiple Objects")


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

print(car1.brand, "-", car1.model)
print(car2.brand, "-", car2.model)

# =====================================================
# Example 4 - Default Parameter Values
# =====================================================

print("\nExample 4 - Default Parameters")


class Employee:

    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary


employee1 = Employee("Rahul")
employee2 = Employee("Priya", 60000)

print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)

# =====================================================
# Example 5 - Constructor with Methods
# =====================================================

print("\nExample 5 - Constructor + Methods")


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(5)

print(circle.area())

# =====================================================
# Example 6 - Bank Account
# =====================================================

print("\nExample 6 - Bank Account")


class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print(f"{self.holder} : ₹{self.balance}")


account = BankAccount("Dhruvi", 10000)

account.deposit(5000)

account.display()

# =====================================================
# Example 7 - AI Engineering Example
# =====================================================

print("\nExample 7 - AI Model")


class AIModel:

    def __init__(self, model_name, framework, accuracy):
        self.model_name = model_name
        self.framework = framework
        self.accuracy = accuracy

    def show_info(self):
        print(f"Model     : {self.model_name}")
        print(f"Framework : {self.framework}")
        print(f"Accuracy  : {self.accuracy}%")


model = AIModel(
    "Image Classifier",
    "TensorFlow",
    98.75
)

model.show_info()

# =====================================================
# Example 8 - Product Example
# =====================================================

print("\nExample 8 - Product")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)


product = Product("Laptop", 75000)

print(product.discount_price(10))

# =====================================================
# Example 9 - Student Result
# =====================================================

print("\nExample 9 - Student Result")


class Result:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A"

        if self.marks >= 75:
            return "B"

        if self.marks >= 60:
            return "C"

        return "Fail"


student = Result("Rahul", 82)

print(student.grade())

# =====================================================
# Example 10 - Constructor is Called Automatically
# =====================================================

print("\nExample 10 - Automatic Constructor")


class Demo:

    def __init__(self):
        print("__init__ executed automatically.")


demo = Demo()

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting self.

❌ Misspelling __init__.

❌ Not initializing required attributes.

❌ Using global variables instead of object attributes.

❌ Writing too much logic inside the constructor.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Initialize all required attributes.

✔ Keep constructors simple.

✔ Use meaningful parameter names.

✔ Avoid complex calculations inside __init__().

✔ Store data using self.attribute.

✔ Use methods for additional operations.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a constructor?

A. A special method that automatically runs
when an object is created.

Q. What is the constructor name in Python?

A. __init__()

Q. Is __init__ called manually?

A. No. Python automatically calls it
during object creation.

Q. Why do we use constructors?

A. To initialize object attributes.

Q. Can constructors have parameters?

A. Yes.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Constructors initialize objects.

✔ __init__() runs automatically.

✔ self refers to the current object.

✔ Constructors can accept parameters.

✔ Constructors make object creation
clean, organized, and reusable.
""")
