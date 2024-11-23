from typing import List, Dict
from datetime import datetime
from Year3.TMPS.Lab4.src.interfaces.weather_component import WeatherComponent
from ..interfaces.weather_observer import WeatherObserver
from ..strategies.calculation_strategy import AverageCalculationStrategy
from ..interfaces.calculation_strategy import WeatherCalculationStrategy

class RegionMonitor(WeatherComponent):
    def __init__(self, name: str):
        super().__init__()  # Initialize observers list
        self.name = name
        self.components: List[WeatherComponent] = []
        self.calculation_strategy = AverageCalculationStrategy()

    def get_name(self) -> str:
        return self.name

    def add_component(self, component: WeatherComponent) -> None:
        self.components.append(component)
        # Share observers with components
        for observer in self.observers:
            component.attach_observer(observer)

    def attach_observer(self, observer: WeatherObserver) -> None:
        super().attach_observer(observer)
        # Propagate observer to all components
        for component in self.components:
            component.attach_observer(observer)

    def detach_observer(self, observer: WeatherObserver) -> None:
        super().detach_observer(observer)
        # Remove observer from all components
        for component in self.components:
            component.detach_observer(observer)

    def remove_component(self, component: WeatherComponent) -> None:
        self.components.remove(component)

    def get_components(self) -> List[WeatherComponent]:
        return self.components

    def get_report(self, date: str) -> str:
        if not self.components:
            return f"No stations in region {self.name}"

        # Collect and aggregate component reports
        reports = []
        stats = self._calculate_statistics(date)

        report = f"""
Regional Weather Report for {self.name}
Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Summary Statistics:
{self._format_statistics(stats)}

Individual Station Reports:
{'-' * 50}
"""
        # Add individual reports
        for component in self.components:
            reports.append(component.get_report(date))

        return report + "\n".join(reports)

    def set_calculation_strategy(self, strategy: WeatherCalculationStrategy):
        self.calculation_strategy = strategy

    def _calculate_statistics(self, date: str) -> Dict:
        if not self.components:
            return {}

        # Collect weather data from all stations
        weather_data = []
        for component in self.components:
            data = component.get_report(date)
            weather_data.append(self._extract_data(data))

        # Use strategy to calculate statistics
        return self.calculation_strategy.calculate_statistics(weather_data)

    def _extract_data(self, report: str) -> Dict:
        """Extract numerical values from report string"""
        data = {}

        # Extract temperature
        temp_start = report.find("Temperature: ") + len("Temperature: ")
        temp_end = report.find("°C", temp_start)
        if temp_start > -1 and temp_end > -1:
            try:
                data['temperature'] = float(report[temp_start:temp_end])
            except ValueError:
                data['temperature'] = None

        # Extract humidity
        humidity_start = report.find("Humidity: ") + len("Humidity: ")
        humidity_end = report.find("%", humidity_start)
        if humidity_start > -1 and humidity_end > -1:
            try:
                data['humidity'] = float(report[humidity_start:humidity_end])
            except ValueError:
                data['humidity'] = None

        # Extract pressure
        pressure_start = report.find("Pressure: ") + len("Pressure: ")
        pressure_end = report.find(" mb", pressure_start)
        if pressure_start > -1 and pressure_end > -1:
            try:
                data['pressure'] = float(report[pressure_start:pressure_end])
            except ValueError:
                data['pressure'] = None

        return data

    def _format_statistics(self, stats: Dict) -> str:
        """Format the statistics into a readable string"""
        if not stats:
            return "No statistics available"

        # Format each statistic with proper rounding
        formatted_stats = "Summary:\n"

        if stats.get('avg_temperature') is not None:
            formatted_stats += f"  Average Temperature: {stats['avg_temperature']:.1f}°C\n"

        if stats.get('avg_humidity') is not None:
            formatted_stats += f"  Average Humidity: {stats['avg_humidity']:.0f}%\n"

        if stats.get('avg_pressure') is not None:
            formatted_stats += f"  Average Pressure: {stats['avg_pressure']:.1f} mb\n"

        formatted_stats += f"  Number of Stations: {stats['station_count']}"

        return formatted_stats
