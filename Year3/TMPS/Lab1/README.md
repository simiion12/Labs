# SOLID Principles Laboratory Work - Lab1

This project demonstrates the implementation of two SOLID principles: the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP) in a simple shape area calculation system.

## Overview

The project consists of a single Python file (`lab1.py`) that implements classes for different shapes (Circle and Rectangle) and an AreaCalculator class that can compute the total area of multiple shapes.

### Implemented SOLID Principles

1. **Single Responsibility Principle (SRP)**
   - Each class in this project has a single, well-defined responsibility:
     - `Circle`: Represents a circle and calculates its area.
     - `Rectangle`: Represents a rectangle and calculates its area.
     - `AreaCalculator`: Calculates the total area of multiple shapes.

2. **Open-Closed Principle (OCP)**
   - The project is designed to be open for extension but closed for modification:
     - `Shape`: An abstract base class that defines the interface for all shapes.
     - New shapes can be added by creating new classes that inherit from `Shape` without modifying existing code.

## File Structure

The entire implementation is contained in a single file:

```
lab1.py
```

## How to Use

1. Ensure you have Python installed on your system.
2. Save the code in a file named `lab1.py`.
3. Run the file using Python:
   ```
   python lab1.py
   ```
4. The script will calculate and print the total area of the example shapes.

## Extending the Project

To add a new shape:

1. Create a new class that inherits from `Shape`.
2. Implement the `calculate_area()` method for the new shape.
3. Use the new shape with the existing `AreaCalculator` without modifying its code.

Example:
```python
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
```

## Requirements

- Python 3.6+
- No external libraries are required.
