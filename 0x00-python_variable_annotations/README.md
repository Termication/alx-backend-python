# Python Type Annotations

This guide covers the fundamentals of using type annotations in Python 3, including specifying function signatures, variable types, and the concept of duck typing. It also explains how to validate your code using the mypy static type checker.
Table of Contents

    Type Annotations in Python 3
    Using Type Annotations for Function Signatures and Variables
    Duck Typing in Python
    Validating Code with Mypy

# Type Annotations in Python 3

Type annotations allow you to explicitly state the expected data types of variables, function parameters, and return values. This helps improve code readability and maintainability. Type annotations do not affect the runtime behavior of your code but can be used for static type checking.
Example of Type Annotations

```python

# Specifying types for variables
name: str = "Alice"
age: int = 30
is_active: bool = True
```
### Using Type Annotations for Function Signatures and Variables

Type annotations can be used to specify the data types for function arguments and return values, which helps clarify the expected inputs and outputs of the function.
Function Signature Example

```python

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(x: int, y: int) -> int:
    return x + y

    name: str specifies that the name parameter must be a string.
    -> str indicates that the function will return a string.
```
## Complex Data Types

You can also use annotations for more complex data structures like lists, tuples, dictionaries, and custom classes.

```python

from typing import List, Dict

def process_data(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data), "count": len(data)}
```
## Duck Typing in Python

Duck typing is a concept that focuses on the behavior of an object rather than its type. In Python, an object's suitability is determined by the methods and properties it implements, rather than the class it is derived from.
#### Example of Duck Typing

```python

class Bird:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_it_quack(thing):
    thing.quack()

bird = Bird()
dog = Dog()

make_it_quack(bird)  # Outputs: Quack!
make_it_quack(dog)   # Outputs: Woof!
```
In this example, both Bird and Dog have a quack method, so they can be used interchangeably in the make_it_quack function, regardless of their actual types.
## Validating Code with Mypy

mypy is a static type checker for Python that helps catch type errors in your code based on your annotations. It ensures that your code follows the specified types, making it more robust and reliable.
#### Installing Mypy

##### To install mypy, use the following command:

```bash

pip install mypy
```
#### Validating Your Code

Run mypy on your Python files to check for type inconsistencies:

```bash

mypy your_script.py
```
#### Example

Given the following code in example.py:

```python

def add(x: int, y: int) -> int:
    return x + y

result = add(5, "10")  # Error: Argument 2 to "add" has incompatible type "str"; expected "int"
```
Running mypy example.py will produce an error indicating that the second argument passed to add is not of the expected type.
## Summary

This guide provides a comprehensive overview of type annotations in Python, the use of duck typing, and how to validate your code using mypy. Understanding these concepts will help you write more readable, maintainable, and error-free Python code.
