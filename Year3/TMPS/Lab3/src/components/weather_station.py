from typing import List
from .weather_component import WeatherComponent
from ..interfaces.weather_service import WeatherService


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