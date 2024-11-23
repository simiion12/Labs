from typing import Dict, Optional
from ..cache.cache_manager import WeatherDataCache, generate_weather_cache_key
from ..parsers.parser_factory import WeatherParserFactory
from ..builders.weather_report_builder import WeatherReportBuilder
from ..builders.weather_report_director import WeatherReportDirector
from ..components.region_monitor import RegionMonitor
from ..components.weather_station import WeatherStation
from ..interfaces.weather_service import WeatherService
from ..decorators.decorators import AlertDecorator
from ..observers.weather_observer import AlertSystem
from ..strategies.calculation_strategy import AverageCalculationStrategy, WeightedAverageStrategy, MedianCalculationStrategy
from ..config import API_KEY, URL
import requests


class WeatherSystemFacade(WeatherService):
    def __init__(self):
        super().__init__()
        self.cache = WeatherDataCache()
        self.parser_factory = WeatherParserFactory()
        self.report_builder = WeatherReportBuilder()
        self.regions: Dict[str, RegionMonitor] = {}
        self.alert_system = AlertSystem()
        self.calculation_strategies = {
            'average': AverageCalculationStrategy(),
            'weighted': WeightedAverageStrategy(),
            'median': MedianCalculationStrategy()
        }

    def set_calculation_method(self, region_name: str, method: str) -> None:
        """Set the statistical calculation method for a region"""
        if region_name in self.regions:
            if method in self.calculation_strategies:
                self.regions[region_name].set_calculation_strategy(
                    self.calculation_strategies[method]
                )
                print(f"Calculation method for {region_name} set to {method}")
            else:
                print(f"Invalid calculation method: {method}")
        else:
            print(f"Region not found: {region_name}")

    def get_station_list(self) -> list[str]:
        """Get a list of all station locations"""
        stations = []
        for region in self.regions.values():
            for component in region.get_components():
                if isinstance(component, WeatherStation):
                    stations.append(component.get_name())
        return stations

    def _get_report_format(self) -> str:
        print("\nChoose report format:")
        print("1. Text")
        print("2. HTML")
        print("3. JSON")
        choice = input("Enter your choice: ")

        format_mapping = {
            "1": "text",
            "2": "html",
            "3": "json"
        }
        return format_mapping.get(choice, "text")

    def add_alert_monitoring(self, region_name: str = None) -> None:
        """Add alert system to a specific region or all regions"""
        if region_name:
            if region_name in self.regions:
                self.regions[region_name].attach_observer(self.alert_system)
                print(f"Alert monitoring added to region: {region_name}")
            else:
                print(f"Region {region_name} not found")
        else:
            # Add to all regions
            for region in self.regions.values():
                region.attach_observer(self.alert_system)
            print("Alert monitoring added to all regions")

    def remove_alert_monitoring(self, region_name: str = None) -> None:
        """Remove alert system from a specific region or all regions"""
        if region_name:
            if region_name in self.regions:
                self.regions[region_name].detach_observer(self.alert_system)
                print(f"Alert monitoring removed from region: {region_name}")
            else:
                print(f"Region {region_name} not found")
        else:
            # Remove from all regions
            for region in self.regions.values():
                region.detach_observer(self.alert_system)
            print("Alert monitoring removed from all regions")

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

    def _find_station(self, location: str) -> Optional[WeatherStation]:
        """
        Find a weather station by its location name in any region
        Returns None if station is not found
        """
        for region in self.regions.values():
            for component in region.get_components():
                if isinstance(component, WeatherStation) and component.get_name() == location:
                    return component
        return None

    def manage_alerts(self):
        while True:
            print("\nAlert System Management")
            print("1. Enable alerts for region")
            print("2. Enable alerts for all regions")
            print("3. Disable alerts for region")
            print("4. Disable alerts for all regions")
            print("5. Back to main menu")

            choice = input("Enter choice: ")

            if choice == '1':
                region = input("Enter region name: ")
                self.add_alert_monitoring(region)
            elif choice == '2':
                self.add_alert_monitoring()
            elif choice == '3':
                region = input("Enter region name: ")
                self.remove_alert_monitoring(region)
            elif choice == '4':
                self.remove_alert_monitoring()
            elif choice == '5':
                break
            else:
                print("Invalid choice")


    def manage_calculation_methods(self):
        print("\nCalculation Method Management")
        print("1. Simple Average")
        print("2. Weighted Average (recent data weighted more)")
        print("3. Median Values")

        region = input("Enter region name: ")
        choice = input("Choose calculation method: ")

        method_mapping = {
            "1": "average",
            "2": "weighted",
            "3": "median"
        }

        if choice in method_mapping:
            self.set_calculation_method(region, method_mapping[choice])