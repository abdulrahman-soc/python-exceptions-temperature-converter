# Python Exceptions & Temperature Converter

A practical Python project demonstrating exception handling, input validation, functions, and temperature conversion through a simple command-line application.

Developed as part of a Python programming learning path, with a bonus Temperature Converter feature to strengthen practical programming and error-handling skills relevant to cybersecurity automation.

---

## Overview

This project focuses on handling runtime errors safely and validating user input using Python exception handling.

It contains two components:

1. **Exception Handling Practice** — Identifying and handling a `NameError` using `try` and `except`.
2. **Temperature Converter** — Converting temperatures between Celsius and Fahrenheit while handling invalid input and unsupported units.

The Temperature Converter also includes a conversion history feature as an additional enhancement.

---

## Learning Objectives

This project demonstrates:

- Python exception handling
- `try` / `except`
- `NameError`
- `ValueError`
- `TypeError`
- Functions
- Loops
- Conditional statements
- Input validation
- User input processing
- Error recovery
- Basic application design

---

## Technologies

- Python 3
- Python Standard Library
- Git
- GitHub

---

## Project Structure

    python-exceptions-temperature-converter/
    │
    ├── README.md
    ├── exceptions.py
    └── temperature_converter.py

---

## Features

### Exception Handling

The `exceptions.py` program demonstrates how Python exceptions can be identified and handled using `try` and `except`.

The project specifically demonstrates handling:

- `NameError`

Instead of allowing the application to terminate unexpectedly, the exception is handled and an appropriate message is displayed.

---

### Temperature Converter

The `temperature_converter.py` program supports:

- Celsius to Fahrenheit conversion.
- Fahrenheit to Celsius conversion.
- Numeric input validation.
- Temperature unit validation.
- Exception handling.
- Repeated user input.
- Conversion history.

### Supported Input

    50 C
    100 F

### Example

    50.0 C = 122.00 F

    100.0 F = 37.78 C

---

## Conversion Formulas

### Celsius to Fahrenheit

    Fahrenheit = (Celsius × 9/5) + 32

### Fahrenheit to Celsius

    Celsius = (Fahrenheit - 32) × 5/9

---

## Exception Handling

The application handles different types of invalid input.

### ValueError

Occurs when the temperature value cannot be converted into a number.

Example:

    abc C

Output:

    Invalid input. Please enter a number followed by C or F.

### TypeError

Raised when an unsupported temperature unit is entered.

Example:

    25 X

Output:

    Invalid temperature unit.

---

## Conversion History

The Temperature Converter includes an additional feature that stores successful conversions during the current program session.

Enter:

    H

to display the conversion history.

Example:

    Conversion History:
    50.0 C = 122.00 F
    100.0 F = 37.78 C

This feature demonstrates practical use of lists and structured program state.

---

## Testing

The project was tested using multiple scenarios.

### Exception Handling

- Successful arithmetic operation.
- `NameError` handling.

### Temperature Conversion

- Celsius to Fahrenheit.
- Fahrenheit to Celsius.
- Decimal temperature values.
- Invalid numeric input.
- Invalid temperature unit.
- Conversion history.

### Example Test Cases

| Input | Expected Result |
|---|---|
| `50 C` | `122.00 F` |
| `100 F` | `37.78 C` |
| `100.5 F` | `38.06 C` |
| `abc C` | Invalid input message |
| `25 X` | Invalid temperature unit |
| `H` | Display conversion history |

---

## How to Run

Make sure Python 3 is installed.

### Run Exception Handling

    python exceptions.py

### Run Temperature Converter

    python temperature_converter.py

---

## Cybersecurity Relevance

Exception handling and input validation are important concepts in cybersecurity programming and automation.

Security scripts frequently process data from users, logs, APIs, files, and other external sources. Unexpected or malformed input can cause failures if it is not handled properly.

The concepts demonstrated in this project can be applied to cybersecurity tasks such as:

- Security log processing
- IOC validation
- Data parsing
- Automation scripts
- SOC tooling
- Incident data processing
- Defensive security utilities

This project provides a foundation for developing more reliable Python-based cybersecurity automation.

---

## Skills Demonstrated

- Python Programming
- Exception Handling
- Error Handling
- Input Validation
- Functions
- Loops
- Conditional Logic
- Data Processing
- Problem Solving
- Basic Automation
- Cybersecurity Programming Fundamentals

---

## Future Improvements

Potential future improvements include:

- Persistent conversion history using JSON.
- Support for additional temperature units.
- Automated unit testing.
- Logging application errors.
- Extending exception handling into cybersecurity data-processing tools.
- Building a security-focused input validation utility.

---

## Author

**Abdulrahman**

Cybersecurity-focused learner developing practical Python programming and security automation skills.

GitHub: `abdulrahman-soc`

---

## License

This project was created for educational and portfolio purposes.