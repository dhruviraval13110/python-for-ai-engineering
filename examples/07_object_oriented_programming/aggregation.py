"""
=========================================================
Python Aggregation
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : aggregation.py

Description
-----------
Aggregation is an Object-Oriented Programming (OOP)
relationship where one class uses another class, but
both classes can exist independently.

It represents a weak "HAS-A" relationship.

Unlike Composition, if the owner object is destroyed,
the contained object can still exist.

Topics Covered
--------------
✔ What is Aggregation?
✔ Weak HAS-A Relationship
✔ Independent Objects
✔ Aggregation vs Composition
✔ Real-world Examples
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("AGGREGATION")
print("=" * 60)

# =====================================================
# Example 1 - Basic Aggregation
# =====================================================

print("\nExample 1 - Basic Aggregation")


class Teacher:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Teacher: {self.name}")


class Department:

    def __init__(self, teacher):
        self.teacher = teacher

    def show(self):
        self.teacher.display()


teacher = Teacher("Dhruvi")
department = Department(teacher)

department.show()

# =====================================================
# Example 2 - Student and College
# =====================================================

print("\nExample 2 - Student & College")


class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Student: {self.name}")


class College:

    def __init__(self, student):
        self.student = student

    def show_student(self):
        self.student.display()


student = Student("Rahul")
college = College(student)

college.show_student()

# =====================================================
# Example 3 - Employee and Company
# =====================================================

print("\nExample 3 - Employee & Company")


class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")


class Company:

    def __init__(self, employee):
        self.employee = employee

    def start_work(self):
        self.employee.work()


employee = Employee("Amit")
company = Company(employee)

company.start_work()

# =====================================================
# Example 4 - Customer and Bank
# =====================================================

print("\nExample 4 - Customer & Bank")


class Customer:

    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Customer: {self.name}")


class Bank:

    def __init__(self, customer):
        self.customer = customer

    def show_customer(self):
        self.customer.details()


customer = Customer("Priya")
bank = Bank(customer)

bank.show_customer()

# =====================================================
# Example 5 - Doctor and Hospital
# =====================================================

print("\nExample 5 - Doctor & Hospital")


class Doctor:

    def __init__(self, name):
        self.name = name

    def consult(self):
        print(f"Dr. {self.name} is consulting.")


class Hospital:

    def __init__(self, doctor):
        self.doctor = doctor

    def start(self):
        self.doctor.consult()


doctor = Doctor("Sharma")
hospital = Hospital(doctor)

hospital.start()

# =====================================================
# Example 6 - AI Engineering Example
# =====================================================

print("\nExample 6 - AI Engineering")


class Dataset:

    def __init__(self, name):
        self.name = name

    def load(self):
        print(f"Loading Dataset: {self.name}")


class ModelTrainer:

    def __init__(self, dataset):
        self.dataset = dataset

    def train(self):
        self.dataset.load()
        print("Training AI Model...")


dataset = Dataset("ImageNet")
trainer = ModelTrainer(dataset)

trainer.train()

# =====================================================
# Example 7 - Team and Player
# =====================================================

print("\nExample 7 - Team & Player")


class Player:

    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing.")


class Team:

    def __init__(self, player):
        self.player = player

    def start_match(self):
        self.player.play()


player = Player("Virat")

team = Team(player)

team.start_match()

# =====================================================
# Example 8 - Laptop and Mouse
# =====================================================

print("\nExample 8 - Laptop & Mouse")


class Mouse:

    def click(self):
        print("Mouse Clicked")


class Laptop:

    def __init__(self, mouse):
        self.mouse = mouse

    def use(self):
        self.mouse.click()
        print("Laptop in Use")


mouse = Mouse()

laptop = Laptop(mouse)

laptop.use()

# =====================================================
# Example 9 - Book and Library
# =====================================================

print("\nExample 9 - Book & Library")


class Book:

    def __init__(self, title):
        self.title = title

    def show(self):
        print(self.title)


class Library:

    def __init__(self, book):
        self.book = book

    def display_book(self):
        self.book.show()


book = Book("Python for AI Engineering")

library = Library(book)

library.display_book()

# =====================================================
# Example 10 - Independent Objects
# =====================================================

print("\nExample 10 - Independent Objects")

teacher = Teacher("Anjali")

department = Department(teacher)

department.show()

print("\nDeleting Department...")

del department

print("Teacher still exists:")

teacher.display()

# =====================================================
# Aggregation vs Composition
# =====================================================

print("\nAggregation vs Composition")

print("""
Aggregation
-----------
Weak HAS-A Relationship

Objects are independent.

Example:
University HAS-A Professor

-------------------------------

Composition
-----------
Strong HAS-A Relationship

Objects depend on each other.

Example:
Car HAS-A Engine
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Confusing Aggregation with Composition.

❌ Creating objects inside the owner class.

❌ Using Aggregation for dependent objects.

❌ Ignoring object independence.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use Aggregation for reusable objects.

✔ Pass objects through constructors.

✔ Keep classes loosely coupled.

✔ Promote code reusability.

✔ Design flexible systems.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is Aggregation?

A. Aggregation is a weak HAS-A relationship
where objects can exist independently.

Q. Difference between Composition and Aggregation?

Composition:
Objects depend on each other.

Aggregation:
Objects are independent.

Q. Give real-life examples.

• College HAS-A Student
• Hospital HAS-A Doctor
• Company HAS-A Employee

Q. Which relationship is weaker?

A. Aggregation.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Aggregation represents a weak HAS-A relationship.

✔ Objects are independent.

✔ Aggregation promotes loose coupling.

✔ It improves flexibility and reusability.

✔ It is widely used in enterprise software,
AI systems, ERP applications, and web development.
""")
