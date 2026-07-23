# Interview Questions

## 1. What is the difference between `if`, `elif`, and `else`?

- `if` checks the first condition.
- `elif` checks additional conditions if previous ones are false.
- `else` executes when none of the previous conditions are true.

---

## 2. What is a nested `if` statement?

An `if` statement inside another `if` statement.

---

## 3. What is the ternary operator?

A one-line conditional expression.

Example:

```python
result = "Pass" if marks >= 35 else "Fail"
```

---

## 4. What is `match-case`?

A structural pattern matching feature introduced in Python 3.10 that provides a clean alternative to long `if-elif` chains for matching values.

---

## 5. When should you avoid nested `if` statements?

When they become deeply nested and reduce readability. Consider using helper functions, guard clauses, or `match-case` where appropriate.
