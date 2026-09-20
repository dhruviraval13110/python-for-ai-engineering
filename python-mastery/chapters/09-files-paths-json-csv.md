# 09. Files, Paths, JSON, CSV

> **Goal:** pathlib, text/binary files, CSV/JSON, serialization, encodings, atomic writes, and data ingestion.

## 1. What you are learning

This chapter is designed as a working lesson, not a definition sheet. Read the explanation, run every example, modify the code, complete the exercises, and then build the mini-project. The goal is to understand **what happens, why it happens, when to use it, and what trade-offs it creates**.

## 2. Core mental model

Python programs are combinations of **objects, names, expressions, statements, functions, and modules**. When you write code, keep asking four questions:

1. What value/object exists right now?
2. What name refers to it?
3. What operation changes or consumes it?
4. What contract should the next part of the program expect?

A strong Python engineer does not memorize syntax in isolation. They can predict the state of a program, explain why an implementation behaves as it does, and choose a simpler implementation when appropriate.

## 3. Learn by execution

For every code example in this chapter:

- run it locally;
- change at least one input;
- predict the output before running it;
- inspect the error when you intentionally break it;
- rewrite the example as a reusable function;
- add a test for the behavior you care about.

## 4. Practical pattern

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExampleRecord:
    name: str
    value: float


def transform(record: ExampleRecord) -> float:
    """Apply one deterministic transformation to a record."""
    if not record.name.strip():
        raise ValueError("name must not be empty")
    return record.value * 1.10


if __name__ == "__main__":
    record = ExampleRecord(name="demo", value=100.0)
    print(transform(record))
```

Notice the engineering habits: explicit types, a small function, validation, a useful exception, an immutable data object, and an executable entry point. These habits become increasingly important as the repository moves toward data and ML systems.

## 5. What to understand deeply

### Syntax versus semantics

Syntax is the grammar Python accepts. Semantics are what that syntax means when executed. Two snippets can look similar but have different behavior because of mutability, scope, evaluation order, or the APIs they call.

### State

State is the information a program currently holds. Bugs often come from unexpected state changes. When debugging, identify the state before and after each important operation instead of guessing.

### Contracts

A function should make its expected inputs, outputs, and failure modes understandable. Type hints and docstrings help communicate the contract; tests verify important parts of it.

## 6. Common mistakes

- copying code without predicting its behavior;
- writing one huge function instead of small units;
- hiding errors with broad `except Exception`;
- using mutable global state;
- hardcoding paths and credentials;
- writing code that works once but cannot be tested;
- optimizing before measuring;
- confusing a tutorial completion with engineering competence.

## 7. AI/ML connection

Python is the orchestration layer for much of practical AI work. The same fundamentals appear in data loaders, preprocessing functions, feature engineering, training pipelines, evaluation scripts, inference services, notebooks, APIs, and automation. If the Python foundation is weak, ML code becomes difficult to debug and maintain.

## 8. Exercises

1. Recreate the example without looking at it.
2. Add input validation and a custom error message.
3. Convert the main operation into a pure function.
4. Write three tests: normal input, boundary input, invalid input.
5. Measure the function with ten thousand inputs and describe the result.
6. Explain the code aloud in under two minutes.

## 9. Interview questions

### Q1. What is the difference between syntax and semantics?
**Answer:** Syntax determines whether Python can parse a program; semantics describe what the parsed program does when executed.

### Q2. Why are small functions easier to maintain?
**Answer:** They reduce the number of responsibilities per unit, make behavior easier to test, and make failures easier to isolate.

### Q3. What makes code production-ready?
**Answer:** There is no single switch. Production readiness normally requires clear contracts, validation, tests, logging, configuration, dependency control, security practices, observability, and an operational plan appropriate to the system.

## 10. Mastery checkpoint

You are ready to move on when you can:

- explain the concept without reading notes;
- write a solution from a blank file;
- debug a deliberately broken solution;
- explain at least two trade-offs;
- write tests for important behavior;
- connect the concept to a data or AI use case.

## 11. Mini-project

Build a small command-line application that uses this chapter's concept. Store it under `python-mastery/projects/` and document the problem, design, implementation, tests, and lessons learned.
