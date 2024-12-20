# Structural Design Patterns

## Author: Cuzmin Simion

----

## Objectives:

1. Study and understand the Structural Design Patterns
2. Extend the previous laboratory work by adding structural design patterns
3. Keep the same theme - Weather System - and add additional functionalities using structural patterns

## Used Design Patterns:

1. **Decorator Pattern**

    **Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
    
    ![Decorator Pattern](https://refactoring.guru/images/patterns/diagrams/decorator/structure.png)

2. **Composite Pattern**

    **Composite** is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.
    
    ![image](https://github.com/user-attachments/assets/ede26d6b-49b6-46f9-a0f1-84a156f9b8e1)

3. **Facade Pattern**

    **Facade** is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.
    
    ![Facade Pattern](https://refactoring.guru/images/patterns/diagrams/facade/structure.png)

## Implementation

Building upon the existing Weather System that used creational patterns (Singleton, Factory, and Builder), I've implemented three structural patterns to enhance the system's functionality and organization:

1. **Decorator Pattern** (`AlertDecorator`)

    Used to dynamically add weather alerts to weather reports based on conditions. The decorator wraps the weather report object and adds alert functionality without modifying the original report structure. This decorator enhances weather reports by analyzing temperature and wind conditions to generate appropriate weather alerts. It seamlessly combines these alerts with the original report while maintaining the original report's interface. The enhancement process is transparent to the client, allowing for dynamic addition of alert functionality without disrupting the existing report structure.

```python
class AlertDecorator:
    def __init__(self, weather_report):
        self._weather_report = weather_report

    def get_data(self):
        alerts = self._generate_weather_alerts(self._weather_report)
        return self._combine_report_and_alerts(self._weather_report, alerts)

    def _generate_weather_alerts(self, data):
        alerts = []
        if data.temperature_c > 35:
            alerts.append("Extreme heat warning!")
        if data.wind_mph > 50:
            alerts.append("High wind advisory!")
        return alerts

    def _combine_report_and_alerts(self, weather_report, alerts):
        alerts_str = "\n".join(alerts) if alerts else "No active weather alerts."
        return f"""
{alerts_str}

{weather_report}
"""
```

2. **Composite Pattern** (Weather Monitoring Hierarchy)

    Implemented a tree structure for weather monitoring where individual weather stations can be grouped into regions. Both individual stations and regions share a common interface through the `WeatherComponent` abstract class. This pattern enables a seamless hierarchical organization of weather stations while ensuring uniform treatment of both individual stations and entire regions. It automatically handles the calculation of regional statistics across all stations and makes it straightforward to add new monitoring points to any level of the hierarchy. The flexibility of this structure allows the system to grow organically while maintaining consistent behavior across all components.

```python
# Base Component
class WeatherComponent(ABC):
    @abstractmethod
    def get_report(self, date: str) -> str:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass

# Leaf
class WeatherStation(WeatherComponent):
    def __init__(self, location: str, weather_service: WeatherService):
        self.location = location
        self.weather_service = weather_service

    def get_report(self, date: str) -> str:
        return self.weather_service.get_weather_report(self.location, date)

    def get_name(self) -> str:
        return self.location

    def add_component(self, component: 'WeatherComponent') -> None:
        raise NotImplementedError("Weather stations cannot have sub-components")

    def remove_component(self, component: 'WeatherComponent') -> None:
        raise NotImplementedError("Weather stations cannot have sub-components")

    def get_components(self) -> List['WeatherComponent']:
        return []

# Composite
class RegionMonitor(WeatherComponent):
    def __init__(self, name: str):
        self.name = name
        self.components: List[WeatherComponent] = []

    def get_name(self) -> str:
        return self.name

    def add_component(self, component: WeatherComponent) -> None:
        self.components.append(component)

    def remove_component(self, component: WeatherComponent) -> None:
        self.components.remove(component)

    def get_components(self) -> List[WeatherComponent]:
        return self.components

    def get_report(self, date: str) -> str:
        if not self.components:
            return f"No stations in region {self.name}"

        # Collect and aggregate component reports
        reports = []
        stats = self._calculate_statistics(date)

        report = f"""
Regional Weather Report for {self.name}
Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Summary Statistics:
{self._format_statistics(stats)}

Individual Station Reports:
{'-' * 50}
"""
```

3. **Facade Pattern** (`WeatherSystemFacade`)

    Provides a simplified interface to the complex weather system, handling the interaction between various components like cache, parsers, report builders, and the composite structure.The facade handles all complex operations including cache checking and updates, data parsing and formatting, report generation with decorations, and comprehensive region and station management. This centralized control point streamlines the interaction between different system components while hiding their complexity from the client.

```python
class WeatherSystemFacade(WeatherService):
    def __init__(self):
        self.cache = WeatherDataCache()
        self.parser_factory = WeatherParserFactory()
        self.report_builder = WeatherReportBuilder()
        self.regions: Dict[str, RegionMonitor] = {}

        self.cache.set_ttl(minutes=15)
        self.cache.set_max_size(100)

    def get_weather_report(self, location: str, date: str) -> str:
        try:
            format = self._get_format()
            # Get from cache or fetch new data
            weather_data = self._get_weather_data(location, date, format)

            # Generate report
            report_type = self._get_report_type()
            report = self._generate_report(weather_data, report_type)
            report_with_alerts = AlertDecorator(report).get_data()
            return str(report_with_alerts)
        except Exception as e:
            return f"Error getting weather report: {str(e)}"

    def add_region(self, region_name: str) -> None:
        if region_name not in self.regions:
            self.regions[region_name] = RegionMonitor(region_name)

    def add_station_to_region(self, region_name: str, station_location: str) -> None:
        if region_name not in self.regions:
            self.add_region(region_name)

        station = WeatherStation(station_location, self)
        self.regions[region_name].add_component(station)

    def get_region_report(self, region_name: str, date: str) -> str:
        format = self._get_format()
        region = self.regions.get(region_name)
        if not region:
            return f"Region {region_name} not found"
        return region.get_report(date)

    def _get_weather_data(self, location: str, date: str, format: str) -> Dict:
        params = {'key': API_KEY, 'q': location, 'dt': date}
        url = URL + f".{format}"
        response = requests.get(url, params=params)
        key = generate_weather_cache_key(location, date)
        if self.cache.get(key) is None:
            weather_data = WeatherParserFactory.get_parser(format).parse(response.text)
            self._set_cache(key, weather_data)
            return weather_data
        else:
            return self._get_cache(key)
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
│   └───components
│   │   │   __init__.py
│   │   │   region_monitor.py
│   │   │   weather_component.py
│   │   │   weather_station.py
│   └───decorators
│   │   │   __init__.py
│   │   │   decorators.py
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

## Conclusion

The implementation of structural patterns has significantly improved the Weather System:

1. **Decorator Pattern** (AlertDecorator):
   - Allows dynamic addition of weather alerts
   - Maintains single responsibility principle
   - Easy to add new types of alerts

2. **Composite Pattern** (Weather Monitoring Hierarchy):
   - Creates a flexible structure for organizing weather stations
   - Enables hierarchical data aggregation
   - Provides uniform treatment of individual stations and groups

3. **Facade Pattern** (WeatherSystemFacade):
   - Simplifies client interaction with the system
   - Encapsulates complex operations
   - Provides a clean, high-level interface

These patterns work together with the previously implemented creational patterns to create a robust, maintainable, and extensible weather monitoring system. The structural patterns have particularly improved the system's organization and made it easier to add new features while maintaining clean code principles.
