"""
=========================================================
Python Polymorphism
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : polymorphism.py

Description
-----------
Polymorphism is one of the four fundamental pillars of
Object-Oriented Programming (OOP).

The word "Polymorphism" means "Many Forms."

It allows different classes to have methods with the
same name but different implementations. This enables
the same interface to perform different actions depending
on the object being used.

Topics Covered
--------------
✔ What is Polymorphism?
✔ Method Overriding
✔ Duck Typing
✔ Built-in Polymorphism
✔ Operator Overloading
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("POLYMORPHISM")
print("=" * 60)

# =====================================================
# Example 1 - Basic Polymorphism
# =====================================================

print("\nExample 1 - Basic Polymorphism")


class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


class Cat(Animal):

    def speak(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# =====================================================
# Example 2 - Same Method Different Objects
# =====================================================

print("\nExample 2 - Same Method")


class Car:

    def move(self):
        print("Car drives on the road")


class Airplane:

    def move(self):
        print("Airplane flies in the sky")


vehicles = [Car(), Airplane()]

for vehicle in vehicles:
    vehicle.move()

# =====================================================
# Example 3 - Duck Typing
# =====================================================

print("\nExample 3 - Duck Typing")


class Bird:

    def fly(self):
        print("Bird is flying")


class Airplane:

    def fly(self):
        print("Airplane is flying")


def start_flying(obj):
    obj.fly()


start_flying(Bird())
start_flying(Airplane())

# =====================================================
# Example 4 - Built-in Polymorphism
# =====================================================

print("\nExample 4 - Built-in Functions")


print(len("Python"))

print(len([10, 20, 30, 40]))

print(len({"a": 1, "b": 2}))

# =====================================================
# Example 5 - Operator Overloading
# =====================================================

print("\nExample 5 - Operator Overloading")


print(10 + 20)

print("Python " + "Programming")

print([1, 2] + [3, 4])

# =====================================================
# Example 6 - Employee Example
# =====================================================

print("\nExample 6 - Employee")


class Employee:

    def work(self):
        print("Employee works")


class Developer(Employee):

    def work(self):
        print("Developer writes code")


class Designer(Employee):

    def work(self):
        print("Designer creates UI")


employees = [Developer(), Designer()]

for employee in employees:
    employee.work()

# =====================================================
# Example 7 - AI Engineering Example
# =====================================================

print("\nExample 7 - AI Engineering")


class AIModel:

    def predict(self):
        print("Generic Prediction")


class ImageClassifier(AIModel):

    def predict(self):
        print("Predicting Image")


class SpamDetector(AIModel):

    def predict(self):
        print("Detecting Spam")


models = [
    ImageClassifier(),
    SpamDetector()
]

for model in models:
    model.predict()

# =====================================================
# Example 8 - Payment System
# =====================================================

print("\nExample 8 - Payment System")


class Payment:

    def pay(self):
        print("Processing Payment")


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


payments = [CreditCard(), UPI()]

for payment in payments:
    payment.pay()

# =====================================================
# Example 9 - Function Polymorphism
# =====================================================

print("\nExample 9 - Function Polymorphism")


def show_details(item):
    item.display()


class Student:

    def display(self):
        print("Student Details")


class Teacher:

    def display(self):
        print("Teacher Details")


show_details(Student())
show_details(Teacher())

# =====================================================
# Example 10 - Shape Example
# =====================================================

print("\nExample 10 - Shapes")


class Shape:

    def area(self):
        print("Area")


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")


class Circle(Shape):

    def area(self):
        print("Circle Area")


for shape in [Rectangle(), Circle()]:
    shape.area()

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Confusing inheritance with polymorphism.

❌ Forgetting to override methods.

❌ Using if-else instead of polymorphism.

❌ Creating unnecessary duplicate code.

❌ Ignoring the parent class interface.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Design common interfaces.

✔ Override only when behavior changes.

✔ Use polymorphism instead of long if-else chains.

✔ Write reusable code.

✔ Follow the Open/Closed Principle.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is polymorphism?

A. Polymorphism allows one interface
to represent many different forms.

Q. What is method overriding?

A. Redefining a parent class method
inside a child class.

Q. What is Duck Typing?

A. If an object behaves like the expected
type, Python accepts it regardless of its class.

Q. Give a real-life example of polymorphism.

A. Different payment methods
(Credit Card, UPI, Net Banking)
all use the same pay() method.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Polymorphism means "Many Forms."

✔ Different objects can use the same method
name with different behavior.

✔ Method overriding is the most common form
of polymorphism.

✔ Duck typing is a powerful Python feature.

✔ Polymorphism makes code flexible,
reusable, and easier to maintain.
""")
