# Object-Oriented Python — Deep OOP, Design, and Interview Mastery

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

## 1. Objects and classes

A class defines behavior and structure used to create instances. An object is a concrete instance with state and behavior. OOP is useful when domain entities have identity, state transitions, and cohesive behavior.

### Mental model

Think of **Objects and classes** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Objects and classes and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Objects and classes in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Objects and classes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Objects and classes is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Objects and classes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Objects and classes appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 2. __init__

__init__ initializes an already-created instance. It is not technically the object constructor; __new__ participates in object creation. Most application code only needs __init__.

### Mental model

Think of **__init__** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is __init__ and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use __init__ in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving __init__?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when __init__ is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving __init__?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could __init__ appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 3. Instance attributes

Instance attributes belong to a particular object. They should normally be initialized consistently so an object has a predictable state.

### Mental model

Think of **Instance attributes** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Instance attributes and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Instance attributes in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Instance attributes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Instance attributes is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Instance attributes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Instance attributes appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 4. Class attributes

Class attributes live on the class and can be shared by instances. Accidentally using a mutable class attribute for per-instance state is a common bug.

### Mental model

Think of **Class attributes** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Class attributes and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Class attributes in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Class attributes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Class attributes is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Class attributes?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Class attributes appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 5. Methods

Instance methods receive self by convention. Class methods receive cls and are useful for alternative constructors or class-level behavior. Static methods receive neither automatically and are best used when a function is logically grouped with a class but does not need instance or class state.

### Mental model

Think of **Methods** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Methods and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Methods in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Methods?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Methods is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Methods?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Methods appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 6. Encapsulation

Python relies more on conventions than strict access modifiers. A leading underscore communicates internal use. Double-underscore name mangling can reduce accidental name collisions but is not a security boundary.

### Mental model

Think of **Encapsulation** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Encapsulation and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Encapsulation in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Encapsulation?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Encapsulation is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Encapsulation?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Encapsulation appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 7. Inheritance

Inheritance allows a class to reuse and specialize another class. Prefer inheritance when there is a genuine substitutable relationship; otherwise composition is often easier to maintain.

### Mental model

Think of **Inheritance** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Inheritance and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Inheritance in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Inheritance?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Inheritance is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Inheritance?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Inheritance appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 8. Polymorphism

Polymorphism means code can operate on different objects through a shared interface or behavior. Python often achieves this through duck typing rather than explicit inheritance.

### Mental model

Think of **Polymorphism** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Polymorphism and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Polymorphism in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Polymorphism?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Polymorphism is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Polymorphism?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Polymorphism appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 9. Composition

Composition builds objects from other objects. It often keeps responsibilities smaller and makes dependencies easier to replace in tests.

### Mental model

Think of **Composition** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Composition and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Composition in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Composition?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Composition is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Composition?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Composition appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 10. Dataclasses

dataclasses generate common methods for data-focused classes. They reduce boilerplate while retaining normal Python class behavior.

### Mental model

Think of **Dataclasses** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Dataclasses and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Dataclasses in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Dataclasses?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Dataclasses is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Dataclasses?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Dataclasses appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 11. Abstract interfaces

abc can define abstract methods for explicit interfaces. Protocols from typing can provide structural typing when static analysis is desired without forcing inheritance.

### Mental model

Think of **Abstract interfaces** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Abstract interfaces and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Abstract interfaces in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Abstract interfaces?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Abstract interfaces is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Abstract interfaces?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Abstract interfaces appear in an AI/ML project?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

### Mastery checkpoint
- [ ] I can explain the concept without reading notes.
- [ ] I can write a working example from memory.
- [ ] I can debug a broken example.
- [ ] I can explain a production use case.
- [ ] I can answer the interview questions aloud.


---

## 12. Magic methods

Dunder methods such as __repr__, __eq__, __len__, and __iter__ integrate objects with Python syntax and built-ins. Implement only behavior that matches Python conventions.

### Mental model

Think of **Magic methods** as a tool with a contract. The important question is not only what syntax exists, but what guarantee the language gives you, what assumptions your code makes, and what failure modes appear when those assumptions are wrong.

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

**Q:** What is Magic methods and why does Python provide it?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** When would you use Magic methods in production?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What is a common mistake involving Magic methods?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** What happens internally or conceptually when Magic methods is used?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How would you test code involving Magic methods?

**Answer framework:** Define it precisely → show a minimal example → explain the runtime/data model → discuss trade-offs → give a production example → mention a failure mode.

**Q:** How could Magic methods appear in an AI/ML project?

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
