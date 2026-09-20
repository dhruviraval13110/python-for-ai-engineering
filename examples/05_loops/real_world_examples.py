"""
Real World Loop Examples
"""

# Shopping Cart

prices = [100,250,300,450]

total = 0

for price in prices:
    total += price

print("Total =", total)

# Attendance

students = ["A","P","A","A","P"]

present = 0

for status in students:

    if status == "A":
        present += 1

print("Present =", present)

# Find Maximum

numbers = [45,78,12,95,63]

largest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

print("Largest =", largest)
