# Python CLI Calculator

A professional command-line calculator built using Python.  
This project demonstrates clean code structure, modular design, robust error handling, and automated testing using `pytest`.

---

## Features

- Addition, subtraction, multiplication, and division
- ASCII calculator logo
- Input validation for numbers and operators
- Graceful handling of division-by-zero errors
- Continuous calculation support
- Clean modular package structure
- Automated unit tests with pytest

---

## Project Structure

calculator/
├── calculator_pkg/
│ ├── init.py # Marks this as a Python package
│ ├── calculator.py # Main calculator logic
│ └── art.py # ASCII logo
├── tests/
│ └── test_calculator.py # Unit tests
├── pyproject.toml # Pytest configuration
├── README.md # Documentation
├── .gitignore

---

## How to Run the Calculator

1. Navigate to the project root:

```bash
cd calculator

```

python3 calculator_pkg/calculator.py

Example Usage
What is the first number?: 10
Pick an operation (+, -, \*, /): /
What is the next number?: 0
❌ Error: Cannot divide by zero

Running Tests

This project uses pytest for automated testing.

From the project root, run: pytest

Expected output:
============================== 5 passed ==============================

All tests must pass before pushing changes or creating a release.

Author

Charandeep Singh Dhingra
GitHub: https://github.com/smartcd007
