"""
=========================================================
Python Recursion
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 06 - Functions
File        : recursion.py

Description
-----------
Recursion is a programming technique where a function
calls itself to solve a smaller version of the same problem.

Every recursive function must have:
1. Base Case
2. Recursive Case

Topics Covered
--------------
✔ What is Recursion?
✔ Base Case
✔ Recursive Case
✔ Factorial
✔ Fibonacci
✔ Sum of Numbers
✔ Reverse String
✔ Palindrome Check
✔ Binary Search
✔ Real-world Example
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("RECURSION")
print("=" * 60)

# =====================================================
# Example 1 - Basic Recursion
# =====================================================

print("\nExample 1 - Countdown")


def countdown(number):
    """Print numbers from n to 1."""

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)

# =====================================================
# Example 2 - Factorial
# =====================================================

print("\nExample 2 - Factorial")


def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("5! =", factorial(5))

# =====================================================
# Example 3 - Fibonacci
# =====================================================

print("\nExample 3 - Fibonacci")


def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for i in range(8):
    print(fibonacci(i), end=" ")

print()

# =====================================================
# Example 4 - Sum of Numbers
# =====================================================

print("\nExample 4 - Sum of Numbers")


def total(number):

    if number == 1:
        return 1

    return number + total(number - 1)


print(total(10))

# =====================================================
# Example 5 - Power Function
# =====================================================

print("\nExample 5 - Power")


def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 5))

# =====================================================
# Example 6 - Reverse String
# =====================================================

print("\nExample 6 - Reverse String")


def reverse(text):

    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]


print(reverse("Python"))

# =====================================================
# Example 7 - Palindrome Check
# =====================================================

print("\nExample 7 - Palindrome")


def palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])


print(palindrome("madam"))
print(palindrome("python"))

# =====================================================
# Example 8 - Binary Search
# =====================================================

print("\nExample 8 - Binary Search")


def binary_search(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)

    return binary_search(arr, target, mid + 1, right)


numbers = [5, 10, 15, 20, 25, 30, 35]

index = binary_search(numbers, 25, 0, len(numbers) - 1)

print("Index:", index)

# =====================================================
# Example 9 - Count Digits
# =====================================================

print("\nExample 9 - Count Digits")


def count_digits(number):

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)


print(count_digits(987654))

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - AI Search Tree")


def search_tree(depth):

    if depth == 0:
        return

    print("Searching Depth:", depth)

    search_tree(depth - 1)


search_tree(4)

# =====================================================
# Example 11 - Real World Example
# Folder Structure
# =====================================================

print("\nExample 11")

print("""
Project/
│
├── app.py
├── utils/
│   ├── helper.py
│   └── data.py
└── models/

Recursive algorithms are commonly used
to traverse folders and subfolders.
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Forgetting the base case.

❌ Infinite recursion.

❌ Changing recursive variables incorrectly.

❌ Using recursion when iteration is simpler.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Always define a base case.

✔ Reduce the problem size each call.

✔ Avoid unnecessary recursion.

✔ Prefer iteration for very large loops.

✔ Keep recursive functions simple.
""")

# =====================================================
# Interview Notes
# =====================================================

print("\nInterview Questions")

print("""
Q. What is recursion?

A. A function calling itself.

Q. Why is a base case necessary?

A. To stop infinite recursion.

Q. Which problems commonly use recursion?

• Factorial
• Fibonacci
• Binary Search
• Tree Traversal
• DFS
• Backtracking
• Merge Sort
• Quick Sort
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Recursion is when a function calls itself.

✔ Every recursive function has:
   • Base Case
   • Recursive Case

✔ Common applications:
   • Trees
   • Graphs
   • Search Algorithms
   • Divide and Conquer
   • Dynamic Programming

✔ Recursion makes some algorithms cleaner
but should be used carefully because deep
recursion can lead to stack overflow.
""")
