"""
=========================================================
Python Instance Methods
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : instance_methods.py

Description
-----------
Instance methods are the most common type of methods in
Python classes. They operate on object-specific data and
can access or modify instance variables using the 'self'
parameter.

Every instance method automatically receives the current
object as its first argument.

Topics Covered
--------------
✔ What are Instance Methods?
✔ self Parameter
✔ Accessing Instance Variables
✔ Modifying Instance Variables
✔ Calling Instance Methods
✔ Multiple Objects
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("INSTANCE METHODS")
print("=" * 60)

# =====================================================
# Example 1 - Basic Instance Method
# =====================================================

print("\nExample 1 - Basic Instance Method")


class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Student Name: {self.name}")


student = Student("Dhruvi")
student.display()

# =====================================================
# Example 2 - Multiple Instance Variables
# =====================================================

print("\nExample 2 - Multiple Instance Variables")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name   : {self.name}")
        print(f"Salary : ₹{self.salary}")


employee = Employee("Rahul", 55000)
employee.show_details()

# =====================================================
# Example 3 - Modifying Instance Variables
# =====================================================

print("\nExample 3 - Updating Object Data")


class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient Balance")
            return

        self.balance -= amount

    def show_balance(self):
        print(f"Balance: ₹{self.balance}")


account = BankAccount("Dhruvi", 10000)

account.deposit(5000)
account.withdraw(2000)

account.show_balance()

# =====================================================
# Example 4 - Multiple Objects
# =====================================================

print("\nExample 4 - Multiple Objects")


class Car:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(self.brand)


car1 = Car("Tesla")
car2 = Car("BMW")

car1.display()
car2.display()

# =====================================================
# Example 5 - Calculator Class
# =====================================================

print("\nExample 5 - Calculator")


class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(10, 20))
print(calc.multiply(5, 6))

# =====================================================
# Example 6 - Student Result
# =====================================================

print("\nExample 6 - Student Result")


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


student = Result("Priya", 88)

print(student.grade())

# =====================================================
# Example 7 - Shopping Cart
# =====================================================

print("\nExample 7 - Shopping Cart")


class ShoppingCart:

    def __init__(self):
        self.total = 0

    def add_item(self, price):
        self.total += price

    def checkout(self):
        print(f"Total Bill: ₹{self.total}")


cart = ShoppingCart()

cart.add_item(1200)
cart.add_item(599)
cart.add_item(250)

cart.checkout()

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class AIModel:

    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy

    def predict(self):
        print(f"{self.model_name} is making predictions...")

    def evaluate(self):
        print(f"Accuracy: {self.accuracy}%")

    def show_info(self):
        print(f"Model: {self.model_name}")


model = AIModel("Image Classifier", 98.75)

model.show_info()
model.predict()
model.evaluate()

# =====================================================
# Example 9 - Changing Object State
# =====================================================

print("\nExample 9 - Change Object State")


class Fan:

    def __init__(self):
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def show_status(self):
        print(self.status)


fan = Fan()

fan.show_status()

fan.turn_on()

fan.show_status()

# =====================================================
# Example 10 - self Represents Current Object
# =====================================================

print("\nExample 10 - self Keyword")


class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


person1 = Person("Dhruvi")
person2 = Person("Rahul")

person1.introduce()
person2.introduce()

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting the self parameter.

❌ Calling instance methods without creating an object.

❌ Forgetting to use self.variable.

❌ Using class variables instead of instance variables.

❌ Writing one method that performs too many tasks.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Always use self as the first parameter.

✔ Keep methods focused on one task.

✔ Use meaningful method names.

✔ Modify object data using self.

✔ Create reusable methods.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is an instance method?

A. A method that works with object-specific
data and uses self.

Q. What is self?

A. self refers to the current object.

Q. Can instance methods modify object data?

A. Yes.

Q. How do we call an instance method?

A. Through an object.

Example:

student.display()
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Instance methods belong to objects.

✔ They use self to access object data.

✔ They can read and modify instance variables.

✔ Every object has its own data but shares
the same methods.

✔ Instance methods are the most commonly
used methods in Python OOP.
""")
