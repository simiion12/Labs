from typing import Dict
from ..cache.cache_manager import WeatherDataCache, generate_weather_cache_key
from ..parsers.parser_factory import WeatherParserFactory
from ..builders.weather_report_builder import WeatherReportBuilder
from ..builders.weather_report_director import WeatherReportDirector
from ..components.region_monitor import RegionMonitor
from ..components.weather_station import WeatherStation
from ..interfaces.weather_service import WeatherService
from ..decorators.decorators import AlertDecorator
from ..config import API_KEY, URL
import requests


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

    def _get_report_type(self) -> str:
        print("Choose the type of the weather report:")
        print("1. Basic")
        print("2. Standard")
        print("3. Advanced")
        choice = int(input("Enter your choice: "))
        while choice != 1 and choice != 2 and choice != 3:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        return choice

    def _generate_report(self, weather_data, report_type):
        director = WeatherReportDirector()
        director.builder = WeatherReportBuilder()
        if report_type == 1:
            return director.create_basic_report(weather_data)
        elif report_type == 2:
            return director.create_standard_report(weather_data)
        elif report_type == 3:
            return director.create_advanced_report(weather_data)
        else:
            return None

    def _set_cache(self, key, weather_data):
        self.cache.set(key, weather_data)

    def _get_cache(self, key):
        return self.cache.get(key)

    def _get_format(self) -> str:
        print("Choose the format of the weather report:")
        print("1. JSON")
        print("2. XML")
        choice = input("Enter your choice: ")

        # Mapping of choices to format types
        format_mapping = {
            "1": "json",
            "2": "xml"
        }

        while choice not in format_mapping:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")

        return format_mapping[choice]
