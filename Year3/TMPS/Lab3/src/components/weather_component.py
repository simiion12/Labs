from abc import ABC, abstractmethod
from typing import Optional, List


class WeatherComponent(ABC):
    @abstractmethod
    def get_report(self, date: str) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def add_component(self, component: 'WeatherComponent') -> None:
        pass

    @abstractmethod
    def remove_component(self, component: 'WeatherComponent') -> None:
        pass

    @abstractmethod
    def get_components(self) -> List['WeatherComponent']:
        pass