from abc import ABC, abstractmethod
from typing import Dict, List

class WeatherCalculationStrategy(ABC):
    @abstractmethod
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        pass
