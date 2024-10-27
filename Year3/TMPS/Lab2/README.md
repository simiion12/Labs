# Weather Forecasting System - Creational Design Patterns

## Objectives

1. **Study and Understand Creational Design Patterns**  
   Learn and apply various creational design patterns (Singleton, Builder, Factory Method) to handle object creation effectively in an object-oriented programming context.

2. **Define Domain and Main Classes**  
   Select a domain, define essential models and classes, and identify suitable instantiation mechanisms using creational design patterns.

3. **Implement Creational Patterns in a Sample Project**  
   Implement at least three creational design patterns to demonstrate object instantiation and management in the selected domain.

---

## Theory

In software engineering, **Creational Design Patterns** provide solutions to manage object creation, making the process more flexible and efficient. Without patterns, object instantiation can lead to increased complexity and potential design issues. Creational patterns introduce standard ways to create objects, often by controlling, hiding, or optimizing the process.

### Common Creational Patterns
- **Singleton**: Ensures only one instance of a class is created, with global access to that instance.
- **Builder**: Constructs complex objects by piecing together parts step-by-step.
- **Factory Method**: Provides an interface for creating objects and allows subclasses to alter the type of object that will be created.

---

## Project Overview: Weather Forecasting System

### Description

This project implements a **Weather Forecasting System** designed to collect, process, and forecast weather data for various regions using three creational design patterns. The system fetches weather data from an API, caches it to improve efficiency, and generates customized reports based on user preferences.

### Implemented Creational Patterns

1. **Factory Method**: Instantiates different types of weather data parsers (`JSONParser`, `XMLParser`) based on the chosen format, allowing flexibility in data handling.
2. **Singleton**: Manages a single instance of the `WeatherDataCache` class, which stores frequently accessed weather data to reduce redundant API calls.
3. **Builder**: Constructs flexible and customizable weather reports with sections for temperature, humidity, and forecast, based on user-selected report type.

---

## Main Project Tasks

1. **Choose Programming Language and IDE**  
   Implemented in Python without external frameworks, using standard libraries to demonstrate pattern implementation.

2. **Domain Selection and Class Definition**  
   - **Domain**: Weather Forecasting System.
   - **Classes/Entities**:
     - `WeatherDataCache`: Manages caching of weather data.
     - `WeatherReportDirector` and `WeatherReportBuilder`: Implements the Builder pattern to construct customizable weather reports.
     - `WeatherParserFactory`: Uses the Factory Method pattern to select the appropriate parser for the chosen data format.

3. **Creational Design Pattern Implementation**  
   The project demonstrates the use of Singleton, Builder, and Factory Method patterns to achieve efficient object management and reusability.

---

## Code Overview
The project is organized into several modules, each responsible for a different aspect of the weather forecasting system. Below is an overview of the key modules and files:

```
Lab2
└───src
│   └───builders
│   │   │   __init__.py
│   │   │   weather_report_builder.py
│   │   │   weather_report_director.py
│   └───cache
│   │   │   __init__.py
│   │   │   cache_manager.py
│   └───models
│   │   │   __init__.py
│   │   │   models.py
│   │   │    weather_report_models.py
│   └───parsers
│   │   │   __init__.py
│   │   │   parsers_factory.py
│   │   │   parsers.py
│   │   __init__.py
│   │   config.py
│   │   main.py
│   │   utils.py
│ 
│   README.md
│   __init__.py    
│   .gitignore
│   .env
│   requirements.txt        
```


### Module Descriptions

- **`builders`**: Implements the Builder pattern to construct weather reports. `weather_report_builder.py` defines the Builder logic, and `weather_report_director.py` controls the assembly of the report components.
- **`cache`**: Contains `cache_manager.py`, which implements the Singleton pattern to store weather data and minimize redundant API calls.
- **`models`**: Defines the data models used throughout the system. `weather_report_models.py` includes specific models related to weather report data.
- **`parsers`**: Contains the Factory Method implementation for creating parsers. `parser_factory.py` decides which parser to use based on the requested data format, while `parsers.py` includes different parser implementations (e.g., JSONParser, XMLParser).
- **`config.py`**: Stores configuration details, including API URL and keys.
- **`main.py`**: The main entry point for the application. Handles user input, retrieves weather data, and generates reports.
- **`utils.py`**: Provides utility functions that assist in user input handling and report generation.

---

## Summary

This laboratory work demonstrates the use of creational design patterns to structure and manage a Weather Forecasting System. By implementing Singleton, Builder, and Factory Method patterns, the project achieves:

- **Reduced Redundancy**: Singleton pattern ensures a single cache instance, reducing redundant API calls.
- **Flexible Report Generation**: Builder pattern allows the creation of customizable weather reports.
- **Data Flexibility**: Factory Method pattern enables seamless parsing of data in various formats.

This approach enhances the system’s maintainability, scalability, and efficiency, providing a robust architecture for future extensions or modifications.
