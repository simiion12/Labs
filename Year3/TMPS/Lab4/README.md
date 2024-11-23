# Behavioral Design Patterns

## Author: Cuzmin Simion

----

## Objectives:

1. Study and understand the Behavioral Design Patterns.
2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
3. Implement some additional functionalities using behavioral design patterns.

## Used Design Patterns:

1. **Observer**

    **Observer** is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
    
    ![image](https://refactoring.guru/images/patterns/diagrams/observer/example.png)

2. **Strategy**

    **Strategy** is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
    
    ![image](https://refactoring.guru/images/patterns/diagrams/strategy/structure.png)



## Implementation

Building upon the existing Weather System that used creational patterns (Singleton, Factory, and Builder) together with three another structural patterns (Decorator, Composite, Facade),  I've implemented two behavioral patterns to enhance the system's functionality and organization:

1. **Observer Pattern** (`Weather Alert System`)

Implements a real-time weather monitoring system that automatically notifies about dangerous weather conditions. This pattern allows weather stations to notify observers about changes in weather conditions without being tightly coupled to the alert system.

```python
class AlertSystem(WeatherObserver):
    def update(self, weather_data: Dict[str, Any]) -> None:
        self._check_temperature(weather_data)
        self._check_wind(weather_data)
        self._check_precipitation(weather_data)

    def _check_temperature(self, data: Dict[str, Any]) -> None:
        temp = data.get('temperature_c')
        if temp > 5:
            self._log_alert(f"🔥 EXTREME HEAT WARNING: {temp}°C in {data['location']}")
        elif temp > -10:
            self._log_alert(f"❄️ EXTREME COLD WARNING: {temp}°C in {data['location']}")

    def _check_wind(self, data: Dict[str, Any]) -> None:
        wind = data.get('wind_mph', 0)
        if wind > 50:
            self._log_alert(f"💨 HIGH WIND ADVISORY: {wind} mph in {data['location']}")

    def _check_precipitation(self, data: Dict[str, Any]) -> None:
        precip = data.get('precipitation_mm', 0)
        if precip > 50:
            self._log_alert(f"🌧️ HEAVY RAIN ALERT: {precip}mm in {data['location']}")

    def _log_alert(self, message: str) -> None:
        print(f"\n[ALERT] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(message)

```

2. **Strategy Pattern** (Weather Calculation Methods)

    Provides different algorithms for calculating weather statistics, allowing regions to use different calculation methods based on their needs. This pattern separates various calculation algorithms from the main business logic.

```python

class AverageCalculationStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        temps = [data['temperature'] for data in weather_data]
        humidity = [data['humidity'] for data in weather_data]
        pressure = [data['pressure'] for data in weather_data]

        return {
            'avg_temperature': sum(temps) / len(temps),
            'avg_humidity': sum(humidity) / len(humidity),
            'avg_pressure': sum(pressure) / len(pressure),
            'station_count': len(weather_data)
        }


class WeightedAverageStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        # More weight to recent readings
        weights = [0.5, 0.3, 0.2]  # Weights for last 3 readings
        temps = [data['temperature'] for data in weather_data[-3:]]
        humidity = [data['humidity'] for data in weather_data[-3:]]
        pressure = [data['pressure'] for data in weather_data[-3:]]
        return {
            'avg_temperature': sum(t * w for t, w in zip(temps, weights)),
            'avg_humidity': sum(h * w for h, w in zip(humidity, weights)),
            'avg_pressure': sum(p * w for p, w in zip(pressure, weights)),
            'station_count': len(weather_data)
        }


class MedianCalculationStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        def median(values):
            sorted_values = sorted(values)
            mid = len(sorted_values) // 2
            return sorted_values[mid]

        temps = [data['temperature'] for data in weather_data]
        humidity = [data['humidity'] for data in weather_data]
        pressure = [data['pressure'] for data in weather_data]

        return {
            'avg_temperature': median(temps),
            'avg_humidity': median(humidity),
            'avg_pressure': median(pressure),
            'station_count': len(weather_data)
        }

```

## Project Structure

```
Lab3
└───src
│   └───builders
│   │   │   __init__.py
│   │   │   weather_report_builder.py
│   │   │   weather_report_director.py
│   └───cache
│   │   │   __init__.py
│   │   │   cache_manager.py
│   └───facade
│   │   │   __init__.py
│   │   │   weather_facade.py
│   └───interfaces
│   │   │   __init__.py
│   │   │   calculation_strategy.py
│   │   │   weather_component.py
│   │   │   weather_observer.py
│   │   │   weather_service.py
│   └───components
│   │   │   __init__.py
│   │   │   region_monitor.py
│   │   │   weather_component.py
│   │   │   weather_station.py
│   └───decorators
│   │   │   __init__.py
│   │   │   decorators.py
│   └───observers
│   │   │   __init__.py
│   │   │   weather_observers.py
│   └───strategies
│   │   │   __init__.py
│   │   │   calculation_strategy.py
│   └───models
│   │   │   __init__.py
│   │   │   models.py
│   │   │   weather_report_models.py
│   └───parsers
│   │   │   __init__.py
│   │   │   parsers_factory.py
│   │   │   parsers.py
│   │   __init__.py
│   │   config.py
│   │   main.py
│ 
│   README.md
│   __init__.py    
│   .gitignore
│   .env
│   requirements.txt        
```

## Conclusion

The implementation of behavioral patterns has significantly improved the Weather System:
1. **Observer Pattern Benefits:**
   - Real-time weather monitoring
   - Automatic alert generation
   - Loosely coupled components
   - Easy to add new types of notifications

2. **Strategy Pattern Benefits:**
   - Flexible calculation methods
   - Easy to add new algorithms
   - Runtime strategy switching
   - Clean separation of algorithms


The combination of behavioral patterns with the existing creational and structural patterns has created a robust, flexible, and maintainable weather monitoring system.
