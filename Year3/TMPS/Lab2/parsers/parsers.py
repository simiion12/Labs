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
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON data: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error parsing weather data: {str(e)}")


class XmlWeatherDataParser(WeatherDataParser):
    def parse(self, data: str) -> WeatherData:
        try:
            location = Location.from_xml(data)
            astronomy = Astronomy.from_xml(data)
            return WeatherData(location=location, astronomy=astronomy)
        except Exception as e:
            raise ValueError(f"Error parsing weather data: {str(e)}")
