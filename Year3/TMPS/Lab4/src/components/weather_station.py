from typing import List, Dict, Any
from Year3.TMPS.Lab4.src.interfaces.weather_component import WeatherComponent
from ..interfaces.weather_service import WeatherService



class WeatherStation(WeatherComponent):
    def __init__(self, location: str, weather_service: WeatherService):
        super().__init__()  # Initialize observers list
        self.location = location
        self.weather_service = weather_service

    def get_report(self, date: str) -> str:
        report = self.weather_service.get_weather_report(self.location, date)

        # Extract weather data from report and notify observers
        weather_data = self._extract_weather_data(report)
        self.notify_observers(weather_data)

        # Format the report using current strategy
        return report


    def get_name(self) -> str:
        return self.location

    def add_component(self, component: 'WeatherComponent') -> None:
        raise NotImplementedError("Weather stations cannot have sub-components")

    def remove_component(self, component: 'WeatherComponent') -> None:
        raise NotImplementedError("Weather stations cannot have sub-components")

    def get_components(self) -> List['WeatherComponent']:
        return []

    def _extract_weather_data(self, report: str) -> Dict[str, Any]:
        """Extract numerical values from report string"""
        data = {}

        # Extract temperature
        temp_start = report.find("Temperature: ") + len("Temperature: ")
        temp_end = report.find("°C", temp_start)
        if temp_start > -1 and temp_end > -1:
            try:
                data['temperature_c'] = float(report[temp_start:temp_end])
            except ValueError:
                data['temperature_c'] = None

        # Extract wind speed
        wind_start = report.find("Wind: ") + len("Wind: ")
        wind_end = report.find(" mph", wind_start)
        if wind_start > -1 and wind_end > -1:
            try:
                data['wind_mph'] = float(report[wind_start:wind_end])
            except ValueError:
                data['wind_mph'] = None

        return data