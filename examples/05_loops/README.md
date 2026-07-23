# 🔁 Python Loops

> Learn how to automate repetitive tasks using Python loops with clear explanations, practical examples, and interview questions.

---

## 📖 Overview

Loops allow you to execute a block of code multiple times without writing the same code repeatedly. They are one of the most important programming concepts and are widely used in data processing, automation, AI, and machine learning.

Python provides two main types of loops:

- **for loop** → Iterate over a sequence (list, tuple, string, range, etc.)
- **while loop** → Execute code while a condition is `True`

---

# 📂 Folder Structure

```text
05_loops/
│
├── README.md
├── for_loop.py
├── while_loop.py
├── break_continue_pass.py
├── nested_loops.py
├── range_function.py
├── enumerate_zip.py
├── list_comprehension.py
├── real_world_examples.py
├── exercises.py
└── interview_questions.md
```

---

# 📚 Topics Covered

| File | Description |
|------|-------------|
| `for_loop.py` | Learn how to iterate over sequences using `for` loops |
| `while_loop.py` | Learn condition-based iteration using `while` loops |
| `break_continue_pass.py` | Control loop execution with `break`, `continue`, and `pass` |
| `nested_loops.py` | Understand loops inside other loops |
| `range_function.py` | Master the `range()` function |
| `enumerate_zip.py` | Iterate with indexes and multiple sequences |
| `list_comprehension.py` | Write concise and efficient loops |
| `real_world_examples.py` | Practical examples using loops |
| `exercises.py` | Practice problems |
| `interview_questions.md` | Common Python interview questions |

---

# 🔁 The `for` Loop

A `for` loop is used to iterate over a sequence.

### Example

```python
for i in range(5):
    print(i)
```

**Output**

```text
0
1
2
3
4
```

### Common Uses

- Iterating through lists
- Processing strings
- Reading files
- Data analysis
- Machine Learning datasets

---

# 🔄 The `while` Loop

A `while` loop executes as long as a condition remains `True`.

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# ⛔ Loop Control Statements

## break

Stops the loop immediately.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

## continue

Skips the current iteration.

```python
for i in range(6):

    if i % 2 == 0:
        continue

    print(i)
```

---

## pass

Acts as a placeholder.

```python
for i in range(5):

    if i == 2:
        pass

    print(i)
```

---

# 📏 range()

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

### Example

```python
for i in range(2, 11, 2):
    print(i)
```

Output

```text
2
4
6
8
10
```

---

# 🔢 enumerate()

Adds an index while iterating.

```python
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output

```text
0 Apple
1 Banana
2 Mango
```

---

# 🔗 zip()

Iterate over multiple sequences simultaneously.

```python
names = ["Alice", "Bob"]

marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output

```text
Alice 90
Bob 85
```

---

# 🧠 List Comprehension

A shorter way to create lists.

```python
numbers = [1,2,3,4,5]

squares = [num**2 for num in numbers]
```

Output

```text
[1, 4, 9, 16, 25]
```

---

# 💼 Real-World Applications

Loops are commonly used for:

- 📊 Data Analysis
- 🤖 Machine Learning
- 📁 File Processing
- 🌐 Web Scraping
- 📈 Automation
- 🎮 Game Development
- 🛒 Shopping Cart Calculations
- 📋 Attendance Systems
- 📦 Inventory Management
- 📧 Email Automation

---

# 📝 Practice Exercises

Try solving these problems:

- Print numbers from 1 to 100
- Print even numbers
- Print odd numbers
- Find factorial
- Generate Fibonacci series
- Reverse a number
- Check palindrome
- Print multiplication tables
- Print star patterns
- Find prime numbers

---

# 💼 Interview Questions

Some common interview topics include:

- Difference between `for` and `while`
- Explain `range()`
- Difference between `break` and `continue`
- What does `pass` do?
- What is `enumerate()`?
- What is `zip()`?
- What is list comprehension?
- When should you use nested loops?
- How can you avoid infinite loops?

See **`interview_questions.md`** for more questions.

---

# 🚀 Best Practices

✅ Use `for` loops when iterating over collections.

✅ Use `while` loops when the number of iterations is unknown.

✅ Prefer `enumerate()` over manual indexing.

✅ Use list comprehensions for simple transformations.

✅ Avoid deeply nested loops whenever possible.

---

# 📚 Next Module

➡️ **06 - Functions**

You'll learn:

- Function definition
- Parameters & arguments
- Return values
- Lambda functions
- Variable scope
- Recursion
- `*args` & `**kwargs`
- Docstrings
- Type hints
- Best practices

---

## 📌 Learning Outcome

After completing this module, you will be able to:

- Write efficient `for` and `while` loops.
- Control loop execution using `break`, `continue`, and `pass`.
- Work with `range()`, `enumerate()`, and `zip()`.
- Use list comprehensions for cleaner code.
- Apply loops to real-world programming problems.
- Solve common coding interview questions involving loops.

---

⭐ **If you found this module helpful, consider giving this repository a star on GitHub!**
