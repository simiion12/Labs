from abc import ABC, abstractmethod

class WeatherService(ABC):
    @abstractmethod
    def get_weather_report(self, location: str, date: str) -> str:
        pass