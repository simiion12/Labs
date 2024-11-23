from abc import ABC, abstractmethod
from typing import List, Dict, Any
from Year3.TMPS.Lab4.src.interfaces.weather_observer import WeatherObserver


class WeatherComponent(ABC):
    def __init__(self):
        self.observers: List[WeatherObserver] = []

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

    def attach_observer(self, observer: WeatherObserver) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def detach_observer(self, observer: WeatherObserver) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, weather_data: Dict[str, Any]) -> None:
        # Add location to weather data before notifying
        weather_data['location'] = self.get_name()
        for observer in self.observers:
            observer.update(weather_data)