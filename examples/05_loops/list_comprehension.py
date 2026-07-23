"""
List Comprehension
"""

numbers = [1,2,3,4,5]

squares = [num**2 for num in numbers]

print(squares)

evens = [num for num in range(20) if num % 2 == 0]

print(evens)

words = ["python","ai","ml"]

uppercase = [word.upper() for word in words]

print(uppercase)
