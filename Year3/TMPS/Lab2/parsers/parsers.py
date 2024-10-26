import json
from abc import ABC, abstractmethod

from Labs.Year3.TMPS.Lab2.models.models import WeatherData, Location, Astronomy


# Abstract Parser Interface
class WeatherDataParser(ABC):
    @abstractmethod
    def parse(self, data: str) -> WeatherData:
        pass


class JsonWeatherDataParser(WeatherDataParser):
    def parse(self, data: str) -> WeatherData:
        try:
            json_data = json.loads(data)
            location = Location.from_dict(json_data['location'])
            astronomy = Astronomy.from_dict(json_data['astronomy'])
            return WeatherData(location=location, astronomy=astronomy)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class XmlWeatherDataParser(WeatherDataParser):
    def parse(self, data: str) -> WeatherData:
        try:
            location = Location.from_xml(data)
            astronomy = Astronomy.from_xml(data)
            return WeatherData(location=location, astronomy=astronomy)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
