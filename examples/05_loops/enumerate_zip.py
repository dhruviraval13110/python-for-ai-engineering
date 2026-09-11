"""
enumerate()
zip()
"""

fruits = ["Apple", "Banana", "Mango"]

print("Enumerate")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

names = ["Alice", "Bob", "Charlie"]

marks = [90, 85, 95]

print("\nZip")

for name, mark in zip(names, marks):
    print(name, mark)
