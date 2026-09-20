# Python Interview Bank — Questions, Answers, Follow-ups, and Coding Drills

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

## 1. What is Python?

Explain Python as a high-level programming language, distinguish language specification from implementation, and mention why readability and a rich standard library contribute to adoption.

### Mental model

Think of **What is Python?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is Python? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is Python? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is Python??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is Python? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is Python??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is Python? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 2. Why is Python considered interpreted?

Explain the practical meaning rather than saying simply that Python is interpreted. CPython compiles source to bytecode and executes it on a virtual machine. Alternative implementations can use different execution strategies.

### Mental model

Think of **Why is Python considered interpreted?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Why is Python considered interpreted? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Why is Python considered interpreted? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Why is Python considered interpreted??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Why is Python considered interpreted? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Why is Python considered interpreted??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Why is Python considered interpreted? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 3. What is the difference between == and is?

== compares equality according to the objects comparison behavior; is checks object identity. Use is for singleton identity checks such as None.

### Mental model

Think of **What is the difference between == and is?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is the difference between == and is? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is the difference between == and is? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is the difference between == and is??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is the difference between == and is? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is the difference between == and is??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is the difference between == and is? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 4. What are mutable and immutable objects?

Explain that mutability concerns whether an object can change in place. Give list versus tuple/string examples and connect this to aliasing and function arguments.

### Mental model

Think of **What are mutable and immutable objects?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What are mutable and immutable objects? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What are mutable and immutable objects? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What are mutable and immutable objects??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What are mutable and immutable objects? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What are mutable and immutable objects??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What are mutable and immutable objects? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 5. Why is a mutable default argument dangerous?

Default expressions are evaluated once when the function is defined. A mutable default therefore persists across calls. Use None and allocate inside the function.

### Mental model

Think of **Why is a mutable default argument dangerous?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Why is a mutable default argument dangerous? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Why is a mutable default argument dangerous? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Why is a mutable default argument dangerous??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Why is a mutable default argument dangerous? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Why is a mutable default argument dangerous??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Why is a mutable default argument dangerous? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 6. List vs tuple?

Compare mutability, intended semantics, memory considerations, hashability of tuples when their elements are hashable, and API communication.

### Mental model

Think of **List vs tuple?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is List vs tuple? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use List vs tuple? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving List vs tuple??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when List vs tuple? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving List vs tuple??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could List vs tuple? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 7. List vs set?

Compare ordering, duplicates, membership performance, indexing, and use cases.

### Mental model

Think of **List vs set?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is List vs set? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use List vs set? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving List vs set??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when List vs set? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving List vs set??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could List vs set? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 8. Dictionary internals?

Explain hashing, buckets conceptually, hash/equality contract, average-case lookup, collision handling at a high level, and why mutable keys are not allowed.

### Mental model

Think of **Dictionary internals?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Dictionary internals? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Dictionary internals? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Dictionary internals??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Dictionary internals? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Dictionary internals??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Dictionary internals? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 9. What is LEGB?

Local, Enclosing, Global, Builtins. Explain name lookup and how closures interact with enclosing scope.

### Mental model

Think of **What is LEGB?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is LEGB? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is LEGB? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is LEGB??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is LEGB? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is LEGB??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is LEGB? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 10. What is a closure?

A nested function retaining access to variables from an enclosing scope after the outer function returns.

### Mental model

Think of **What is a closure?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is a closure? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is a closure? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is a closure??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is a closure? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is a closure??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is a closure? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 11. What is a decorator?

A callable that transforms or wraps another callable. Explain wrappers, functools.wraps, and practical uses.

### Mental model

Think of **What is a decorator?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is a decorator? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is a decorator? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is a decorator??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is a decorator? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is a decorator??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is a decorator? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 12. Iterator vs iterable?

An iterable can produce an iterator; an iterator maintains iteration state and implements __next__. iter(obj) obtains an iterator, and next(iterator) advances it.

### Mental model

Think of **Iterator vs iterable?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Iterator vs iterable? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Iterator vs iterable? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Iterator vs iterable??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Iterator vs iterable? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Iterator vs iterable??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Iterator vs iterable? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 13. Generator?

A generator function uses yield to produce values lazily. Explain memory benefits, one-pass behavior, and when a list is simpler.

### Mental model

Think of **Generator?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Generator? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Generator? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Generator??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Generator? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Generator??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Generator? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 14. Shallow vs deep copy?

Shallow copying duplicates the outer container while nested references remain shared; deep copying recursively duplicates supported nested objects.

### Mental model

Think of **Shallow vs deep copy?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Shallow vs deep copy? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Shallow vs deep copy? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Shallow vs deep copy??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Shallow vs deep copy? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Shallow vs deep copy??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Shallow vs deep copy? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 15. What is exception handling?

Explain try, except, else, finally, raising exceptions, specificity, and why exceptions should not hide programming bugs.

### Mental model

Think of **What is exception handling?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is exception handling? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is exception handling? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is exception handling??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is exception handling? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is exception handling??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is exception handling? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 16. Why use context managers?

They make setup/cleanup deterministic and readable. Explain the with protocol and __enter__/__exit__ at a high level.

### Mental model

Think of **Why use context managers?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Why use context managers? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Why use context managers? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Why use context managers??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Why use context managers? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Why use context managers??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Why use context managers? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 17. What is a virtual environment?

An isolated environment for project dependencies and executables, reducing conflicts between projects.

### Mental model

Think of **What is a virtual environment?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is a virtual environment? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is a virtual environment? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is a virtual environment??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is a virtual environment? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is a virtual environment??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is a virtual environment? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 18. What is OOP?

Explain objects, state, behavior, encapsulation, polymorphism, inheritance, composition, and when OOP is or is not useful.

### Mental model

Think of **What is OOP?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is OOP? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is OOP? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is OOP??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is OOP? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is OOP??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is OOP? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 19. Inheritance vs composition?

Inheritance expresses an is-a relationship and substitution; composition assembles behavior and often provides looser coupling.

### Mental model

Think of **Inheritance vs composition?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Inheritance vs composition? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Inheritance vs composition? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Inheritance vs composition??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Inheritance vs composition? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Inheritance vs composition??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Inheritance vs composition? appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 20. What is duck typing?

Code relies on supported behavior rather than an objects nominal class. If an object provides the needed interface, it can be used.

### Mental model

Think of **What is duck typing?** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is What is duck typing? and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use What is duck typing? in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving What is duck typing??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when What is duck typing? is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving What is duck typing??

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could What is duck typing? appear in an AI/ML project?

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
