from abc import ABC, abstractmethod
from typing import Dict, Any

class WeatherObserver(ABC):
    @abstractmethod
    def update(self, weather_data: Dict[str, Any]) -> None:
        pass
