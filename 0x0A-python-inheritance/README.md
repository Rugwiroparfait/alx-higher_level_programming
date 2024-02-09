# Project 0x0A - Python Inheritance

## Description
This project explores the concept of inheritance in Python, focusing on Object-Oriented Programming (OOP) principles. The tasks involve writing Python scripts to create classes, inherit from base classes, override methods, and validate attributes.

## Project Details
- **Author:** Guillaume
- **Weight:** 1
- **Start Date:** February 5, 2024, 6:00 AM
- **Deadline:** February 8, 2024, 6:00 AM
- **Auto QA Review:** An auto review will be launched at the deadline
- **Mandatory Tasks Completion:**
  - Auto QA review: 0.0/170 mandatory & 0.0/21 optional
  - Altogether: 0.0%
  - Mandatory: 0.0%
  - Optional: 0.0%

## Learning Objectives
By the end of this project, participants are expected to understand the following concepts:
- Python programming advantages
- Superclass, base class, and parent class
- Subclass
- Listing all attributes and methods of a class or instance
- Adding new attributes to an instance
- Inheriting classes from others
- Defining classes with multiple base classes
- Default class inheritance
- Method or attribute overriding
- Inherited attributes and methods available to subclasses
- Purpose of inheritance
- Usage of `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Resources
Participants are encouraged to read or watch the following resources:
- Inheritance
- Multiple inheritance
- Inheritance in Python
- Learn to Program 10: Inheritance Magic Methods

## Requirements
### Python Scripts
- **Allowed Editors:** vi, vim, emacs
- **Interpreter:** Python 3 (version 3.8.5)
- **File Endings:** All files should end with a new line
- **Shebang:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A README.md file, at the root of the project folder, is mandatory
- **Coding Style:** Code should follow PEP 8 guidelines (using `pycodestyle` version 2.8.*)
- **Execution Permission:** All files must be executable
- **File Length:** The length of files will be tested using `wc`

### Python Test Cases
- **Allowed Editors:** vi, vim, emacs
- **File Endings:** All test files should end with a new line
- **Folder Structure:** All test files should be inside a folder named `tests`
- **File Type:** All test files should be text files with extension `.txt`
- **Execution:** All tests should be executed using the command `python3 -m doctest ./tests/*`
- **Documentation:** All modules, classes, and functions should have documentation
- **Documentation Format:** A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method
- **Collaboration:** Collaboration on test cases is encouraged

## Documentation
- Do not use the words `import` or `from` inside comments, as the checker may interpret it as attempting to import modules

## Tasks
Participants are required to complete several tasks, each focusing on different aspects of inheritance in Python. Each task has specific requirements and objectives.

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.

### 1. My List
Write a class `MyList` that inherits from `list` with a method `print_sorted()` to print the list in ascending order.

### 2. Exact Same Class
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

### 3. Same Class or Inherit From
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

### 4. Only Sub Class Of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

### 5. Geometry Module
Write an empty class `BaseGeometry`.

### 6. Improve Geometry
Write a class `BaseGeometry` with a method `area()` that raises an Exception with the message "area() is not implemented".

### 7. Integer Validator
Write a class `BaseGeometry` with a method `integer_validator()` to validate integer values.

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` with instantiation, validation, and area calculation.

### 9. Full Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` with instantiation, validation, area calculation, and string representation.

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` with instantiation, validation, and area calculation.

### 11. Square #2
Write a class `Square` that inherits from `Rectangle` with instantiation, validation, area calculation, and string representation.

## Conclusion
This project provides practical exercises to enhance understanding and proficiency in Python inheritance, promoting good coding practices and adherence to guidelines.
