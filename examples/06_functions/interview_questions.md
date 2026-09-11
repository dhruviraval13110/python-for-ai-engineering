# Python Functions - Interview Questions

> A collection of beginner to advanced Python function interview questions with concise answers. These questions are commonly asked in Python, AI/ML, Data Science, and Software Development interviews.

---

# 📌 Beginner Level

## 1. What is a function in Python?

A function is a reusable block of code that performs a specific task. It helps organize code, reduce duplication, and improve readability.

---

## 2. Why do we use functions?

- Code reusability
- Better readability
- Easier debugging
- Modularity
- Easier maintenance

---

## 3. How do you define a function?

```python
def greet():
    print("Hello")
```

---

## 4. How do you call a function?

```python
greet()
```

---

## 5. What is the difference between a parameter and an argument?

| Parameter | Argument |
|-----------|----------|
| Variable in function definition | Actual value passed during function call |

Example:

```python
def greet(name):      # Parameter
    print(name)

greet("Dhruvi")       # Argument
```

---

## 6. What is the difference between `return` and `print()`?

| return | print() |
|---------|----------|
| Sends value back | Displays output |
| Reusable | Not reusable |
| Ends function | Doesn't end function |

---

## 7. What happens if a function has no return statement?

Python automatically returns **None**.

```python
def hello():
    print("Hello")

print(hello())
```

Output:

```
Hello
None
```

---

## 8. Can a function return multiple values?

Yes.

```python
def calculate(a, b):
    return a+b, a-b

x, y = calculate(10,5)
```

---

## 9. What are default parameters?

Default values are used when no argument is provided.

```python
def greet(name="Guest"):
    print(name)
```

---

## 10. What are keyword arguments?

Arguments passed using parameter names.

```python
student(name="Dhruvi", age=20)
```

---

# 📌 Intermediate Level

## 11. What is variable scope?

Scope determines where a variable can be accessed.

Types:

- Local
- Global
- Enclosing
- Built-in

(LEGB Rule)

---

## 12. What is the LEGB Rule?

Python searches variables in this order:

- Local
- Enclosing
- Global
- Built-in

---

## 13. What is the `global` keyword?

It allows modification of a global variable inside a function.

---

## 14. What is the `nonlocal` keyword?

It modifies variables from the enclosing function.

---

## 15. What are lambda functions?

Anonymous one-line functions created using the `lambda` keyword.

```python
square = lambda x: x*x
```

---

## 16. When should lambda functions be used?

For short, simple operations such as:

- map()
- filter()
- reduce()
- sorted()

---

## 17. What is recursion?

A function calling itself to solve a problem.

---

## 18. What is a base case?

The stopping condition of recursion.

Without it, recursion continues forever.

---

## 19. What is *args?

It collects multiple positional arguments into a tuple.

```python
def add(*numbers):
```

---

## 20. What is **kwargs?

It collects keyword arguments into a dictionary.

```python
def info(**data):
```

---

## 21. Difference between *args and **kwargs?

| *args | **kwargs |
|--------|-----------|
| Tuple | Dictionary |
| Positional | Keyword |

---

## 22. What is packing?

Collecting multiple values into one variable.

```python
def demo(*args):
```

---

## 23. What is unpacking?

Passing list or dictionary elements as arguments.

```python
numbers = [1,2,3]

func(*numbers)
```

---

# 📌 Advanced Level

## 24. What is a decorator?

A function that modifies another function without changing its original code.

---

## 25. Why use decorators?

- Logging
- Authentication
- Authorization
- Validation
- Performance Monitoring
- Caching

---

## 26. What does `@wraps` do?

It preserves the original function's metadata.

---

## 27. What are docstrings?

Documentation strings used to describe modules, classes, and functions.

---

## 28. How do you access a docstring?

```python
help(function)

function.__doc__
```

---

## 29. What are type hints?

Annotations that describe expected data types.

```python
def add(a:int, b:int) -> int:
```

---

## 30. Do type hints enforce data types?

No.

They improve readability and help IDEs and static analysis tools.

---

# 📌 AI Engineering Interview Questions

## 31. Why are functions important in AI?

Functions make AI code:

- Modular
- Reusable
- Testable
- Easier to debug

---

## 32. Why should preprocessing be written as functions?

Because preprocessing is reused in:

- Training
- Validation
- Testing
- Production

---

## 33. Give examples of AI functions.

- normalize()
- preprocess()
- train_model()
- predict()
- evaluate_model()
- split_dataset()

---

## 34. Why should AI functions return values instead of printing?

Returned values can be reused by the next stage of the ML pipeline.

---

## 35. Where are decorators used in AI?

- Logging
- Timing
- Model monitoring
- Performance tracking

---

# 📌 Coding Questions

Practice writing functions for:

- Factorial
- Fibonacci
- Prime Number
- Palindrome
- Armstrong Number
- Calculator
- Student Grade
- BMI Calculator
- Shopping Cart
- Bank Account
- Employee Salary
- Data Normalization
- Binary Search
- Temperature Converter

---

# 📌 Rapid Fire Questions

- What is a function?
- What is recursion?
- What is lambda?
- What is a decorator?
- What is a docstring?
- What is type hinting?
- Difference between argument and parameter?
- Difference between print() and return()?
- Difference between local and global variables?
- Difference between *args and **kwargs?
- What is LEGB?
- What is unpacking?
- Why use functions?
- Can a function return another function?
- Can Python return multiple values?

---

# 🎯 Interview Tips

✅ Write clean and readable functions.

✅ Use meaningful function names.

✅ Prefer `return` over `print()`.

✅ Add docstrings and type hints.

✅ Avoid unnecessary global variables.

✅ Keep functions focused on a single responsibility.

✅ Practice writing functions without looking at examples.

---

# 🚀 Module Completed

Congratulations! 🎉

You have completed **Module 06 – Functions**.

You now understand:

- ✅ Function Basics
- ✅ Parameters & Arguments
- ✅ Return Statements
- ✅ Variable Scope
- ✅ Lambda Functions
- ✅ Recursion
- ✅ *args & **kwargs
- ✅ Docstrings
- ✅ Type Hints
- ✅ Decorators
- ✅ Best Practices
- ✅ Real-world Applications

➡️ **Next Module:** `07_object_oriented_programming`
