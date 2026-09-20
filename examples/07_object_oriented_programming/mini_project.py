"""
=========================================================
Python Mini Project - Student Management System
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 07 - Object-Oriented Programming
File        : mini_project.py

Description
-----------
This mini project demonstrates how Object-Oriented
Programming concepts work together in a real-world
application.

The project includes:
- Classes & Objects
- Constructors
- Encapsulation
- Properties
- Composition
- Lists of Objects
- CRUD Operations

Topics Covered
--------------
✔ Student Class
✔ Student Management System
✔ Add Student
✔ View Students
✔ Search Student
✔ Update Marks
✔ Delete Student
✔ OOP Project Structure
"""

print("=" * 60)
print("MINI PROJECT - STUDENT MANAGEMENT SYSTEM")
print("=" * 60)

# =====================================================
# Student Class
# =====================================================


class Student:

    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks should be between 0 and 100.")

    def display(self):

        print("-" * 50)
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Marks   : {self.__marks}")


# =====================================================
# Student Management System
# =====================================================


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    # -------------------------------------------------
    # Add Student
    # -------------------------------------------------

    def add_student(self, student):

        self.students.append(student)

        print(f"{student.name} added successfully.")

    # -------------------------------------------------
    # View Students
    # -------------------------------------------------

    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\nStudent List")

        for student in self.students:
            student.display()

    # -------------------------------------------------
    # Search Student
    # -------------------------------------------------

    def search_student(self, roll_no):

        for student in self.students:

            if student.roll_no == roll_no:

                print("\nStudent Found")

                student.display()

                return student

        print("Student not found.")
        return None

    # -------------------------------------------------
    # Update Marks
    # -------------------------------------------------

    def update_marks(self, roll_no, marks):

        student = self.search_student(roll_no)

        if student:

            student.marks = marks

            print("Marks Updated Successfully.")

    # -------------------------------------------------
    # Delete Student
    # -------------------------------------------------

    def delete_student(self, roll_no):

        for student in self.students:

            if student.roll_no == roll_no:

                self.students.remove(student)

                print("Student Deleted Successfully.")

                return

        print("Student not found.")


# =====================================================
# Creating Management System
# =====================================================

system = StudentManagementSystem()

# =====================================================
# Adding Students
# =====================================================

print("\nAdding Students")

student1 = Student(101, "Dhruvi", 21, 95)
student2 = Student(102, "Rahul", 20, 88)
student3 = Student(103, "Amit", 22, 91)

system.add_student(student1)
system.add_student(student2)
system.add_student(student3)

# =====================================================
# Viewing Students
# =====================================================

print("\nViewing Students")

system.view_students()

# =====================================================
# Searching Student
# =====================================================

print("\nSearching Student")

system.search_student(102)

# =====================================================
# Updating Marks
# =====================================================

print("\nUpdating Marks")

system.update_marks(102, 93)

# =====================================================
# Viewing Updated Data
# =====================================================

print("\nUpdated Student List")

system.view_students()

# =====================================================
# Deleting Student
# =====================================================

print("\nDeleting Student")

system.delete_student(101)

# =====================================================
# Final Student List
# =====================================================

print("\nFinal Student List")

system.view_students()

# =====================================================
# Features of This Project
# =====================================================

print("\nProject Features")

print("""
✔ Add Student

✔ View Student

✔ Search Student

✔ Update Marks

✔ Delete Student

✔ Encapsulation

✔ Property Decorator

✔ Object-Oriented Design
""")

# =====================================================
# OOP Concepts Used
# =====================================================

print("\nOOP Concepts Used")

print("""
✔ Class

✔ Object

✔ Constructor

✔ Encapsulation

✔ Property

✔ Composition

✔ List of Objects

✔ Methods
""")

# =====================================================
# Common Improvements
# =====================================================

print("\nFuture Improvements")

print("""
✔ Store data in a database

✔ Export data to CSV

✔ Import data from Excel

✔ Login System

✔ File Handling

✔ GUI using Tkinter

✔ REST API using FastAPI

✔ SQLite Integration

✔ Search by Name

✔ Sort Students
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Which OOP concepts are used in this project?

A.
• Class
• Object
• Constructor
• Encapsulation
• Property
• Composition

Q. Why is encapsulation used?

A.
To protect sensitive data like marks.

Q. How are students stored?

A.
Inside a list of Student objects.

Q. How can this project be improved?

A.
By adding database support,
authentication, and a graphical interface.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ This project combines multiple OOP concepts.

✔ It demonstrates real-world object interaction.

✔ It follows modular design principles.

✔ It can be expanded into a complete
Student Management Application.

✔ Similar architectures are used in
ERP systems, Banking Software,
Hospital Management Systems,
and AI-powered applications.
""")
