"""
=========================================
Python For Loop
=========================================

Author : Dhruvi Raval
Repository : Python for AI Engineering

A for loop is used to iterate over a sequence
such as a list, tuple, string, or range.
"""

# -----------------------------------------
# Basic Example
# -----------------------------------------

print("Basic For Loop")

for i in range(5):
    print(i)

# -----------------------------------------
# Iterate through a list
# -----------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("\nFruits:")

for fruit in fruits:
    print(fruit)

# -----------------------------------------
# Iterate through a string
# -----------------------------------------

print("\nCharacters")

for letter in "Python":
    print(letter)

# -----------------------------------------
# Sum of numbers
# -----------------------------------------

total = 0

for number in range(1, 6):
    total += number

print("\nSum =", total)

# -----------------------------------------
# Even Numbers
# -----------------------------------------

print("\nEven Numbers")

for i in range(2, 11, 2):
    print(i)

# -----------------------------------------
# Multiplication Table
# -----------------------------------------

num = 5

print(f"\nMultiplication Table of {num}")

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
