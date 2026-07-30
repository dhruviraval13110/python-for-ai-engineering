# Object-Oriented Programming (OOP) Interview Questions

## Author
**Dhruvi Raval**

## Repository
**Python for AI Engineering**

## Module
**07 - Object-Oriented Programming**

---

# Beginner Level

### Q1. What is Object-Oriented Programming (OOP)?

**Answer:**
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects. Objects contain both data (attributes) and behavior (methods). OOP makes software reusable, modular, maintainable, and scalable.

---

### Q2. What are the four pillars of OOP?

**Answer:**

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

### Q3. What is a Class?

**Answer:**

A class is a blueprint or template used to create objects.

Example:

```python
class Student:
    pass
```

---

### Q4. What is an Object?

**Answer:**

An object is an instance of a class.

```python
student = Student()
```

---

### Q5. What is a Constructor?

**Answer:**

A constructor is a special method that automatically executes when an object is created.

```python
def __init__(self):
    pass
```

---

### Q6. What is self?

**Answer:**

`self` refers to the current object of a class.

---

### Q7. Difference between Class and Object?

| Class | Object |
|--------|---------|
| Blueprint | Real instance |
| Doesn't occupy runtime memory | Occupies memory |
| Used to create objects | Created from class |

---

### Q8. What are Instance Variables?

**Answer:**

Variables unique to each object.

```python
self.name
```

---

### Q9. What are Class Variables?

**Answer:**

Variables shared among all objects.

```python
class Student:
    school = "ABC School"
```

---

### Q10. What are Instance Methods?

**Answer:**

Methods that work with instance variables.

---

# Intermediate Level

### Q11. What is Encapsulation?

**Answer:**

Encapsulation means hiding internal data and providing controlled access through methods or properties.

---

### Q12. Public, Protected, and Private Members?

| Type | Syntax |
|------|--------|
| Public | name |
| Protected | _name |
| Private | __name |

---

### Q13. What is Inheritance?

**Answer:**

Inheritance allows one class to acquire properties and methods of another class.

---

### Q14. Types of Inheritance?

**Answer:**

- Single
- Multilevel
- Multiple
- Hierarchical

---

### Q15. What is Method Overriding?

**Answer:**

Redefining a parent class method inside a child class.

---

### Q16. What is super()?

**Answer:**

Used to access parent class methods and constructors.

---

### Q17. What is Polymorphism?

**Answer:**

One interface with multiple implementations.

---

### Q18. What is Duck Typing?

**Answer:**

"If it walks like a duck and quacks like a duck, it's a duck."

Python checks behavior instead of object type.

---

### Q19. What is Abstraction?

**Answer:**

Hiding implementation details while exposing only essential functionality.

---

### Q20. Which module provides abstraction?

**Answer:**

```python
abc
```

---

# Advanced Level

### Q21. What is an Abstract Class?

**Answer:**

A class that contains one or more abstract methods.

---

### Q22. Can we create an object of an abstract class?

**Answer:**

No.

---

### Q23. What is @abstractmethod?

**Answer:**

Decorator used to declare abstract methods.

---

### Q24. What are Magic Methods?

**Answer:**

Special methods beginning and ending with double underscores.

Example:

```python
__init__()
__str__()
__len__()
__add__()
```

---

### Q25. Difference between __str__() and __repr__()?

| __str__() | __repr__() |
|------------|-------------|
| User-friendly | Developer-friendly |

---

### Q26. What is Operator Overloading?

**Answer:**

Changing the behavior of operators using magic methods.

---

### Q27. What is @property?

**Answer:**

Converts a method into an attribute-like interface.

---

### Q28. Why use @property?

**Answer:**

- Validation
- Encapsulation
- Cleaner syntax

---

### Q29. What is a Setter?

**Answer:**

Used to update a property's value.

---

### Q30. What is a Deleter?

**Answer:**

Used to delete a property.

---

# Expert Level

### Q31. What is Composition?

**Answer:**

A strong HAS-A relationship where one object owns another.

Example:

Car HAS-A Engine

---

### Q32. What is Aggregation?

**Answer:**

A weak HAS-A relationship where objects are independent.

Example:

Department HAS-A Teacher

---

### Q33. Difference between Composition and Aggregation?

| Composition | Aggregation |
|-------------|-------------|
| Strong relationship | Weak relationship |
| Dependent objects | Independent objects |
| Owner creates object | Object passed from outside |

---

### Q34. What are Dataclasses?

**Answer:**

Classes that automatically generate methods like:

- __init__()
- __repr__()
- __eq__()

using:

```python
@dataclass
```

---

### Q35. Why use field(default_factory=list)?

**Answer:**

To safely create mutable default values.

---

### Q36. What is frozen=True?

**Answer:**

Creates immutable dataclass objects.

---

### Q37. What are SOLID Principles?

**Answer:**

- S – Single Responsibility Principle
- O – Open/Closed Principle
- L – Liskov Substitution Principle
- I – Interface Segregation Principle
- D – Dependency Inversion Principle

---

### Q38. Why prefer Composition over Inheritance?

**Answer:**

Because it provides loose coupling, flexibility, and better maintainability.

---

### Q39. Where is OOP used?

**Answer:**

- AI & Machine Learning
- Web Development
- Banking
- ERP Systems
- Hospital Management
- Robotics
- Game Development
- Mobile Apps
- Cloud Computing

---

### Q40. What are the benefits of OOP?

**Answer:**

- Code Reusability
- Modularity
- Maintainability
- Scalability
- Security
- Flexibility
- Easier Testing
- Better Organization

---

# Coding Interview Questions

### Q41.

Create a Student class with attributes and methods.

---

### Q42.

Create a BankAccount class using encapsulation.

---

### Q43.

Implement inheritance using Animal and Dog.

---

### Q44.

Demonstrate method overriding.

---

### Q45.

Create an abstract class Shape.

---

### Q46.

Implement polymorphism using Vehicle classes.

---

### Q47.

Use @property for salary validation.

---

### Q48.

Create a dataclass Employee.

---

### Q49.

Build a Library Management System using OOP.

---

### Q50.

Explain the difference between:

- Class vs Object
- Inheritance vs Composition
- Composition vs Aggregation
- Encapsulation vs Abstraction
- Method Overloading vs Method Overriding
- __str__() vs __repr__()

---

# Quick Revision

## OOP Pillars

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## Relationships

- IS-A → Inheritance
- HAS-A (Strong) → Composition
- HAS-A (Weak) → Aggregation

---

## Important Decorators

```python
@property
@classmethod
@staticmethod
@abstractmethod
@dataclass
```

---

## Important Magic Methods

```python
__init__()
__str__()
__repr__()
__len__()
__add__()
__eq__()
__lt__()
__call__()
```

---

# Module Summary

After completing this module, you should be able to:

- Design classes and objects
- Use constructors effectively
- Apply encapsulation for data protection
- Implement inheritance and polymorphism
- Create abstract classes
- Work with magic methods
- Use properties for controlled access
- Understand composition and aggregation
- Build dataclasses for clean data models
- Develop real-world OOP applications
- Follow professional OOP best practices

**🎉 Congratulations! You have successfully completed Module 07 – Object-Oriented Programming.**
