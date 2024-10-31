# Creational Design Patterns
## Author: Cuzmin Simion
----
## Objectives:
* Get familiar with the Creational Design Patterns;
* Choose a specific domain and define its main classes/models;
* Implement at least 3 Creational Design Patterns for the specific domain;

## Used Design Patterns:
* Singleton Pattern
* Builder Pattern
* Factory Method Pattern

## Implementation

This project implements a **Weather Forecasting System** designed to collect, process, and forecast weather data for various regions using three creational design patterns. The system fetches weather data from an API, caches it to improve efficiency, and generates customized reports based on user preferences.


Here are the key implementations:

### 1. Singleton Pattern (Cache Manager)
Used to maintain a single instance of the weather data cache throughout the application:

```python
class WeatherDataCache:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Double-checked locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_cache()
        return cls._instance
```

### 2. Factory Method Pattern (Parser Creation)
Handles the creation of different parser types based on data format:

```python
class WeatherParserFactory:
    _parsers = {
        'json': JsonWeatherDataParser,
        'xml': XmlWeatherDataParser
    }

    @staticmethod
    def get_parser(parser_type: str):
        parser = WeatherParserFactory._parsers.get(parser_type.lower())
        if not parser:
            raise ValueError(f"Invalid parser type: {parser_type}")
        return parser()

```

### 3. Builder Pattern (Weather Report Construction)
Enables step-by-step construction of weather reports with different components:

```python
class WeatherReportBuilder:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._report_data: Dict[str, Any] = {}

    def set_location_data(self, location: Location) -> 'WeatherReportBuilder':
        """Set basic location data"""
         pass

    def set_standard_location_data(self, location: Location) -> 'WeatherReportBuilder':
         """Set extended location data"""
         pass

         def set_current_conditions(self, current: Current) -> 'WeatherReportBuilder':
        """Set basic current conditions"""
         pass

    def set_advanced_conditions(self, current: Current) -> 'WeatherReportBuilder':
        """Set advanced current conditions"""
         pass

    def set_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set basic day data"""
         pass

    def set_standard_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set extended day data"""
         pass

    def set_advanced_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set advanced day data"""
         pass

    def set_astronomy_data(self, astronomy: Astronomy) -> 'WeatherReportBuilder':
        """Set astronomy data"""
         pass

    def build_basic(self) -> BaseWeatherReport:
        """Build basic weather report"""
         pass

    def build_standard(self) -> StandardWeatherReport:
        """Build standard weather report"""
         pass

    def build_advanced(self) -> AdvancedWeatherReport:
        """Build advanced weather report"""
         pass

```

## Project Structure
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


## Conclusions
The implementation of creational design patterns in this Weather Forecasting System has resulted in:
* Efficient data management through centralized caching (Singleton)
* Flexible report generation system that can be easily extended (Builder)
* Modular and maintainable parser creation mechanism (Factory Method)
* Clear separation of concerns and improved code organization

These patterns have significantly improved the system's maintainability and scalability while reducing code duplication and complexity.
