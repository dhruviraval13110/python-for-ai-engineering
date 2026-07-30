"""
=========================================================
Python Inheritance
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : inheritance.py

Description
-----------
Inheritance is one of the four fundamental pillars of
Object-Oriented Programming (OOP).

Inheritance allows a new class (Child Class) to inherit
attributes and methods from an existing class (Parent Class).

It promotes code reusability, reduces duplication,
and helps build scalable applications.

Topics Covered
--------------
✔ What is Inheritance?
✔ Parent Class
✔ Child Class
✔ Single Inheritance
✔ Multilevel Inheritance
✔ Multiple Inheritance
✔ Hierarchical Inheritance
✔ super() Function
✔ Method Overriding
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("INHERITANCE")
print("=" * 60)

# =====================================================
# Example 1 - Basic Inheritance
# =====================================================

print("\nExample 1 - Basic Inheritance")


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()

# =====================================================
# Example 2 - Parent and Child Methods
# =====================================================

print("\nExample 2 - Parent & Child Methods")


class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car is Driving")


car = Car()

car.start()
car.drive()

# =====================================================
# Example 3 - Using super()
# =====================================================

print("\nExample 3 - super()")


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll_no):

        super().__init__(name)

        self.roll_no = roll_no


student = Student("Dhruvi", 101)

print(student.name)
print(student.roll_no)

# =====================================================
# Example 4 - Method Overriding
# =====================================================

print("\nExample 4 - Method Overriding")


class Bird:

    def sound(self):
        print("Bird makes a sound")


class Sparrow(Bird):

    def sound(self):
        print("Sparrow Chirps")


bird = Sparrow()

bird.sound()

# =====================================================
# Example 5 - Multilevel Inheritance
# =====================================================

print("\nExample 5 - Multilevel Inheritance")


class LivingThing:

    def breathe(self):
        print("Breathing...")


class Animal(LivingThing):

    def walk(self):
        print("Walking...")


class Dog(Animal):

    def bark(self):
        print("Barking...")


dog = Dog()

dog.breathe()
dog.walk()
dog.bark()

# =====================================================
# Example 6 - Multiple Inheritance
# =====================================================

print("\nExample 6 - Multiple Inheritance")


class Camera:

    def capture(self):
        print("Taking Photo")


class Phone:

    def call(self):
        print("Calling...")


class SmartPhone(Camera, Phone):
    pass


phone = SmartPhone()

phone.capture()
phone.call()

# =====================================================
# Example 7 - Hierarchical Inheritance
# =====================================================

print("\nExample 7 - Hierarchical Inheritance")


class Employee:

    def company(self):
        print("OpenAI")


class Developer(Employee):

    def code(self):
        print("Writing Code")


class Designer(Employee):

    def design(self):
        print("Designing UI")


developer = Developer()
designer = Designer()

developer.company()
developer.code()

designer.company()
designer.design()

# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Engineering")


class AIModel:

    def train(self):
        print("Training Model...")


class ImageClassifier(AIModel):

    def predict(self):
        print("Predicting Images...")


classifier = ImageClassifier()

classifier.train()
classifier.predict()

# =====================================================
# Example 9 - isinstance() and issubclass()
# =====================================================

print("\nExample 9 - isinstance() & issubclass()")


print(isinstance(classifier, ImageClassifier))
print(isinstance(classifier, AIModel))

print(issubclass(ImageClassifier, AIModel))

# =====================================================
# Example 10 - Employee Management
# =====================================================

print("\nExample 10 - Employee Management")


class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Manager(Employee):

    def manage(self):
        print("Managing Team")


manager = Manager("Rahul")

manager.show()
manager.manage()

# =====================================================
# Types of Inheritance
# =====================================================

print("\nTypes of Inheritance")

print("""
1. Single Inheritance

Parent
   │
 Child

----------------------------

2. Multilevel Inheritance

Grandparent
      │
 Parent
      │
 Child

----------------------------

3. Multiple Inheritance

Parent A -----
              \
               Child
              /
Parent B -----

----------------------------

4. Hierarchical Inheritance

       Parent
      /     \
 Child1   Child2
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting to call super().

❌ Rewriting parent code unnecessarily.

❌ Deep inheritance chains.

❌ Confusing inheritance with composition.

❌ Overusing inheritance.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use inheritance for "IS-A" relationships.

✔ Reuse parent class functionality.

✔ Keep inheritance hierarchies simple.

✔ Use super() to initialize parent classes.

✔ Override methods only when necessary.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is inheritance?

A. It allows one class to inherit
properties and methods from another class.

Q. What are the different types
of inheritance?

• Single
• Multilevel
• Multiple
• Hierarchical

Q. What does super() do?

A. It calls methods or constructors
of the parent class.

Q. What is method overriding?

A. Redefining a parent class method
inside the child class.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Inheritance promotes code reuse.

✔ Child classes inherit from parent classes.

✔ super() accesses parent functionality.

✔ Python supports Single, Multilevel,
Multiple, and Hierarchical inheritance.

✔ Inheritance is widely used in AI,
web development, automation,
and enterprise software.
""")
