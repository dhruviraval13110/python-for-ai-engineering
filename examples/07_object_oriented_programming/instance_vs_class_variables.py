"""
=========================================================
Python Instance Variables vs Class Variables
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : instance_vs_class_variables.py

Description
-----------
Python classes can contain two types of variables:

1. Instance Variables
2. Class Variables

Understanding the difference between them is essential
for writing efficient and reusable Object-Oriented code.

Topics Covered
--------------
✔ Instance Variables
✔ Class Variables
✔ Differences
✔ Updating Variables
✔ Shared vs Individual Data
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("INSTANCE VARIABLES VS CLASS VARIABLES")
print("=" * 60)

# =====================================================
# Example 1 - Instance Variables
# =====================================================

print("\nExample 1 - Instance Variables")


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Dhruvi", 95)
student2 = Student("Rahul", 88)

print(student1.name, "-", student1.marks)
print(student2.name, "-", student2.marks)

# =====================================================
# Example 2 - Class Variable
# =====================================================

print("\nExample 2 - Class Variable")


class College:

    college_name = "ABC Engineering College"

    def __init__(self, student_name):
        self.student_name = student_name


student1 = College("Dhruvi")
student2 = College("Priya")

print(student1.college_name)
print(student2.college_name)

# =====================================================
# Example 3 - Updating Instance Variable
# =====================================================

print("\nExample 3 - Updating Instance Variable")


class Car:

    def __init__(self, brand):
        self.brand = brand


car = Car("Tesla")

print("Before:", car.brand)

car.brand = "BMW"

print("After :", car.brand)

# =====================================================
# Example 4 - Updating Class Variable
# =====================================================

print("\nExample 4 - Updating Class Variable")


class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Dhruvi")
employee2 = Employee("Rahul")

print(employee1.company)
print(employee2.company)

Employee.company = "Microsoft"

print(employee1.company)
print(employee2.company)

# =====================================================
# Example 5 - Instance Variable Overrides Class Variable
# =====================================================

print("\nExample 5 - Override Class Variable")


class Laptop:

    brand = "HP"


laptop = Laptop()

print("Before:", laptop.brand)

laptop.brand = "Dell"

print("After :", laptop.brand)

print("Class :", Laptop.brand)

# =====================================================
# Example 6 - Counting Objects
# =====================================================

print("\nExample 6 - Object Counter")


class Student:

    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1


Student("A")
Student("B")
Student("C")

print(Student.total_students)

# =====================================================
# Example 7 - Bank Example
# =====================================================

print("\nExample 7 - Bank")


class BankAccount:

    bank_name = "State Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


account1 = BankAccount("Dhruvi", 25000)
account2 = BankAccount("Priya", 40000)

print(account1.bank_name)
print(account2.bank_name)

print(account1.holder, account1.balance)
print(account2.holder, account2.balance)

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class AIModel:

    framework = "TensorFlow"

    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy


model1 = AIModel("Image Classifier", 98.5)
model2 = AIModel("Spam Detector", 97.2)

print(model1.framework)
print(model2.framework)

print(model1.model_name)
print(model2.model_name)

# =====================================================
# Example 9 - __dict__
# =====================================================

print("\nExample 9 - __dict__")


print(model1.__dict__)

print(AIModel.__dict__.keys())

# =====================================================
# Example 10 - Memory Demonstration
# =====================================================

print("\nExample 10 - Shared Class Variable")


class Company:

    company_name = "OpenAI"

    def __init__(self, employee):
        self.employee = employee


emp1 = Company("Dhruvi")
emp2 = Company("Rahul")

print(emp1.company_name)
print(emp2.company_name)

Company.company_name = "NexxFlow"

print(emp1.company_name)
print(emp2.company_name)

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Using class variables for personal data.

❌ Storing shared data as instance variables.

❌ Confusing self.variable with Class.variable.

❌ Updating class variables through instances unintentionally.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use instance variables for object-specific data.

✔ Use class variables for shared data.

✔ Modify shared values using the class name.

✔ Keep naming meaningful.

✔ Avoid unnecessary class variables.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is an instance variable?

A. A variable unique to each object.

Q. What is a class variable?

A. A variable shared by all objects of a class.

Q. Where are instance variables stored?

A. Inside each object.

Q. Where are class variables stored?

A. Inside the class.

Q. Which is used for shared data?

A. Class variables.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Instance variables belong to individual objects.

✔ Class variables are shared by all objects.

✔ Use self.variable for instance data.

✔ Use Class.variable for shared data.

✔ Choosing the correct variable type makes
your OOP code cleaner and more efficient.
""")
