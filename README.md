# Scientific Calculator in Python

## Overview

This project is a simple command-line scientific calculator built using Python. It provides a variety of basic and advanced mathematical operations, including arithmetic, trigonometry, logarithms, and mathematical constants.

The calculator runs in the terminal and uses Python’s built-in `math` library for scientific computations.

## Features

The calculator supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division (with zero division handling)
- Power (exponentiation)
- Square root (with validation for negative numbers)
- Natural logarithm (with validation for non-positive numbers)
- Sine (input in degrees)
- Cosine (input in degrees)
- Tangent (input in degrees)
- Exponential function
- Mathematical constants:
  - Pi (π)
  - Euler’s number (e)

## How It Works

1. The program displays a menu with available operations.
2. The user selects an operation by entering a number from 1 to 13.
3. Depending on the selection:
   - One or two numeric inputs are requested.
4. The program performs the calculation using the corresponding function.
5. The result is displayed in the terminal.

## Requirements

- Python 3.x
- No external dependencies (only the built-in `math` module)

## Error Handling

The program includes basic error handling for:

- Division by zero  
- Square root of negative numbers  
- Logarithm of non-positive numbers  
- Invalid menu options  

## Notes

- Trigonometric functions use degrees instead of radians.  
- The program runs once per execution and exits after showing the result.
