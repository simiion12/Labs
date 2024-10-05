from abc import ABC, abstractmethod
import math

# Single Responsibility Principle (SRP)
# Each class has a single responsibility: calculating the area of a specific shape


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Open-Closed Principle (OCP)
# The AreaCalculator is open for extension (new shapes) but closed for modification


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class AreaCalculator:
    def calculate_total_area(self, shapes):
        return sum(shape.calculate_area() for shape in shapes)


circle = Circle(5)
rectangle = Rectangle(4, 6)

calculator = AreaCalculator()
total_area = calculator.calculate_total_area([circle, rectangle])

print(f"Total area: {total_area}")
