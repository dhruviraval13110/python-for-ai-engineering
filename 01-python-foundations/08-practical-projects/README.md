# Foundation Projects — Build, Debug, Test, and Explain

> **Course rule:** Do not memorize this chapter. Type every example, run it, deliberately break it, inspect the error, fix it, and explain the behavior in your own words.

## How to study this chapter
1. Read the mental model.
2. Type the examples instead of copy-pasting them.
3. Predict the output before running the code.
4. Run the code.
5. Change one thing and predict again.
6. Write the exercises without looking at the solution.
7. Explain the interview questions aloud.
8. Complete the mastery checklist only after you can reproduce the ideas.


---

## 1. Project 1: CLI Expense Manager

Build a command-line application that stores expenses, validates input, calculates totals, filters by category, persists data to JSON, and includes unit tests. The purpose is to combine functions, collections, files, errors, and CLI design.

### Mental model

Think of **Project 1: CLI Expense Manager** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

### Basic example

```python
# Predict the output before running this.
value = 10
result = value * 2
print(result)
```

### Production example

```python
def process_value(value: int) -> int:
    """Transform a value while keeping the contract explicit."""
    if not isinstance(value, int):
        raise TypeError('value must be an integer')
    return value * 2

print(process_value(10))
```

### Common mistakes
- Memorizing syntax without understanding the object or control-flow model.
- Ignoring boundary cases.
- Catching every exception and hiding the actual bug.
- Writing clever one-liners when a readable block would be easier to maintain.
- Skipping tests because the example is small.

### AI/ML connection
In AI/ML code, this concept appears in data validation, preprocessing, feature engineering, model-serving code, experiment tooling, and automation. A strong Python engineer understands the behavior of the language before relying on a library abstraction.

### Practice drills
1. Rebuild the example from memory.
2. Add an invalid input.
3. Decide what exception should be raised.
4. Write one unit test for normal input and one for a boundary or failure case.
5. Explain why your implementation is readable.

### Interview questions for this topic

**Q:** What is Project 1: CLI Expense Manager and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Project 1: CLI Expense Manager in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Project 1: CLI Expense Manager?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Project 1: CLI Expense Manager is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Project 1: CLI Expense Manager?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Project 1: CLI Expense Manager appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 2. Project 2: Student Grade Analyzer

Load student records from CSV, validate rows, calculate statistics, identify missing data, generate a report, and test edge cases. This bridges pure Python with data analysis.

### Mental model

Think of **Project 2: Student Grade Analyzer** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

### Basic example

```python
# Predict the output before running this.
value = 10
result = value * 2
print(result)
```

### Production example

```python
def process_value(value: int) -> int:
    """Transform a value while keeping the contract explicit."""
    if not isinstance(value, int):
        raise TypeError('value must be an integer')
    return value * 2

print(process_value(10))
```

### Common mistakes
- Memorizing syntax without understanding the object or control-flow model.
- Ignoring boundary cases.
- Catching every exception and hiding the actual bug.
- Writing clever one-liners when a readable block would be easier to maintain.
- Skipping tests because the example is small.

### AI/ML connection
In AI/ML code, this concept appears in data validation, preprocessing, feature engineering, model-serving code, experiment tooling, and automation. A strong Python engineer understands the behavior of the language before relying on a library abstraction.

### Practice drills
1. Rebuild the example from memory.
2. Add an invalid input.
3. Decide what exception should be raised.
4. Write one unit test for normal input and one for a boundary or failure case.
5. Explain why your implementation is readable.

### Interview questions for this topic

**Q:** What is Project 2: Student Grade Analyzer and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Project 2: Student Grade Analyzer in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Project 2: Student Grade Analyzer?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Project 2: Student Grade Analyzer is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Project 2: Student Grade Analyzer?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Project 2: Student Grade Analyzer appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 3. Project 3: Log Analyzer

Read application logs, parse structured fields, count error types, detect repeated failures, and produce a summary. This introduces strings, files, dictionaries, regular expressions, and operational thinking.

### Mental model

Think of **Project 3: Log Analyzer** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

### Basic example

```python
# Predict the output before running this.
value = 10
result = value * 2
print(result)
```

### Production example

```python
def process_value(value: int) -> int:
    """Transform a value while keeping the contract explicit."""
    if not isinstance(value, int):
        raise TypeError('value must be an integer')
    return value * 2

print(process_value(10))
```

### Common mistakes
- Memorizing syntax without understanding the object or control-flow model.
- Ignoring boundary cases.
- Catching every exception and hiding the actual bug.
- Writing clever one-liners when a readable block would be easier to maintain.
- Skipping tests because the example is small.

### AI/ML connection
In AI/ML code, this concept appears in data validation, preprocessing, feature engineering, model-serving code, experiment tooling, and automation. A strong Python engineer understands the behavior of the language before relying on a library abstraction.

### Practice drills
1. Rebuild the example from memory.
2. Add an invalid input.
3. Decide what exception should be raised.
4. Write one unit test for normal input and one for a boundary or failure case.
5. Explain why your implementation is readable.

### Interview questions for this topic

**Q:** What is Project 3: Log Analyzer and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Project 3: Log Analyzer in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Project 3: Log Analyzer?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Project 3: Log Analyzer is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Project 3: Log Analyzer?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Project 3: Log Analyzer appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 4. Project 4: Package a reusable utility library

Turn shared functions into a real Python package with pyproject.toml, tests, type hints, documentation, and a CLI entry point. The goal is to learn how code becomes reusable software rather than a collection of scripts.

### Mental model

Think of **Project 4: Package a reusable utility library** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

### Basic example

```python
# Predict the output before running this.
value = 10
result = value * 2
print(result)
```

### Production example

```python
def process_value(value: int) -> int:
    """Transform a value while keeping the contract explicit."""
    if not isinstance(value, int):
        raise TypeError('value must be an integer')
    return value * 2

print(process_value(10))
```

### Common mistakes
- Memorizing syntax without understanding the object or control-flow model.
- Ignoring boundary cases.
- Catching every exception and hiding the actual bug.
- Writing clever one-liners when a readable block would be easier to maintain.
- Skipping tests because the example is small.

### AI/ML connection
In AI/ML code, this concept appears in data validation, preprocessing, feature engineering, model-serving code, experiment tooling, and automation. A strong Python engineer understands the behavior of the language before relying on a library abstraction.

### Practice drills
1. Rebuild the example from memory.
2. Add an invalid input.
3. Decide what exception should be raised.
4. Write one unit test for normal input and one for a boundary or failure case.
5. Explain why your implementation is readable.

### Interview questions for this topic

**Q:** What is Project 4: Package a reusable utility library and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Project 4: Package a reusable utility library in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Project 4: Package a reusable utility library?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Project 4: Package a reusable utility library is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Project 4: Package a reusable utility library?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Project 4: Package a reusable utility library appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 5. Project 5: Data preprocessing pipeline

Create a deterministic preprocessing pipeline that validates input records, cleans values, transforms features, and emits a dataset ready for machine learning. Separate pure transformations from I/O.

### Mental model

Think of **Project 5: Data preprocessing pipeline** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

### Basic example

```python
# Predict the output before running this.
value = 10
result = value * 2
print(result)
```

### Production example

```python
def process_value(value: int) -> int:
    """Transform a value while keeping the contract explicit."""
    if not isinstance(value, int):
        raise TypeError('value must be an integer')
    return value * 2

print(process_value(10))
```

### Common mistakes
- Memorizing syntax without understanding the object or control-flow model.
- Ignoring boundary cases.
- Catching every exception and hiding the actual bug.
- Writing clever one-liners when a readable block would be easier to maintain.
- Skipping tests because the example is small.

### AI/ML connection
In AI/ML code, this concept appears in data validation, preprocessing, feature engineering, model-serving code, experiment tooling, and automation. A strong Python engineer understands the behavior of the language before relying on a library abstraction.

### Practice drills
1. Rebuild the example from memory.
2. Add an invalid input.
3. Decide what exception should be raised.
4. Write one unit test for normal input and one for a boundary or failure case.
5. Explain why your implementation is readable.

### Interview questions for this topic

**Q:** What is Project 5: Data preprocessing pipeline and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Project 5: Data preprocessing pipeline in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Project 5: Data preprocessing pipeline?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Project 5: Data preprocessing pipeline is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Project 5: Data preprocessing pipeline?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Project 5: Data preprocessing pipeline appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

# Final Foundation Review

## Build challenge
Create a CLI application that accepts user input, validates it, stores structured records, performs calculations, persists data to a file, handles expected errors, logs important events, and has unit tests. Do not use external frameworks. After completing it, refactor repeated logic into functions and then into a small package.

## Oral interview drill
Explain the following without notes: names versus objects; equality versus identity; mutability; scope; iteration; exception boundaries; context managers; modules versus packages; virtual environments; classes versus instances; composition versus inheritance; shallow versus deep copying; iterables versus iterators; generators; decorators; type hints; testing strategy; and why clean boundaries matter in AI/ML systems.

## Graduation standard
You are ready to move forward when you can build a small Python program from an empty directory, explain every important design decision, write tests for its behavior, diagnose failures from tracebacks, and explain why your solution is preferable to at least one plausible alternative.
