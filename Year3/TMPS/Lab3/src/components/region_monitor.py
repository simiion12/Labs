from typing import List, Dict
from datetime import datetime
from .weather_component import WeatherComponent

class RegionMonitor(WeatherComponent):
    def __init__(self, name: str):
        self.name = name
        self.components: List[WeatherComponent] = []

    def get_name(self) -> str:
        return self.name

    def add_component(self, component: WeatherComponent) -> None:
        self.components.append(component)

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

    def _calculate_statistics(self, date: str) -> Dict:
        """Calculate aggregate statistics from all stations in the region"""
        if not self.components:
            return {}

        temperatures = []
        humidities = []
        pressures = []

        # Collect data from all stations
        for component in self.components:
            # Get the report from each station
            report = component.get_report(date)

            # Extract numerical values using string parsing
            # Find temperature
            temp_start = report.find("Temperature: ") + len("Temperature: ")
            temp_end = report.find("°C", temp_start)
            if temp_start > -1 and temp_end > -1:
                try:
                    temp = float(report[temp_start:temp_end])
                    temperatures.append(temp)
                except ValueError:
                    continue

            # Find humidity
            humidity_start = report.find("Humidity: ") + len("Humidity: ")
            humidity_end = report.find("%", humidity_start)
            if humidity_start > -1 and humidity_end > -1:
                try:
                    humidity = float(report[humidity_start:humidity_end])
                    humidities.append(humidity)
                except ValueError:
                    continue

            # Find pressure
            pressure_start = report.find("Pressure: ") + len("Pressure: ")
            pressure_end = report.find(" mb", pressure_start)
            if pressure_start > -1 and pressure_end > -1:
                try:
                    pressure = float(report[pressure_start:pressure_end])
                    pressures.append(pressure)
                except ValueError:
                    continue

        # Calculate averages
        stats = {
            'avg_temperature': sum(temperatures) / len(temperatures) if temperatures else None,
            'avg_humidity': sum(humidities) / len(humidities) if humidities else None,
            'avg_pressure': sum(pressures) / len(pressures) if pressures else None,
            'station_count': len(self.components)
        }

        return stats

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
