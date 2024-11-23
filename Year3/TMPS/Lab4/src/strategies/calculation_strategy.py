from typing import Dict, List
from ..interfaces.calculation_strategy import WeatherCalculationStrategy


class AverageCalculationStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        temps = [data['temperature'] for data in weather_data]
        humidity = [data['humidity'] for data in weather_data]
        pressure = [data['pressure'] for data in weather_data]

        return {
            'avg_temperature': sum(temps) / len(temps),
            'avg_humidity': sum(humidity) / len(humidity),
            'avg_pressure': sum(pressure) / len(pressure),
            'station_count': len(weather_data)
        }


class WeightedAverageStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        # More weight to recent readings
        weights = [0.5, 0.3, 0.2]  # Weights for last 3 readings
        temps = [data['temperature'] for data in weather_data[-3:]]
        humidity = [data['humidity'] for data in weather_data[-3:]]
        pressure = [data['pressure'] for data in weather_data[-3:]]
        return {
            'avg_temperature': sum(t * w for t, w in zip(temps, weights)),
            'avg_humidity': sum(h * w for h, w in zip(humidity, weights)),
            'avg_pressure': sum(p * w for p, w in zip(pressure, weights)),
            'station_count': len(weather_data)
        }


class MedianCalculationStrategy(WeatherCalculationStrategy):
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        def median(values):
            sorted_values = sorted(values)
            mid = len(sorted_values) // 2
            return sorted_values[mid]

        temps = [data['temperature'] for data in weather_data]
        humidity = [data['humidity'] for data in weather_data]
        pressure = [data['pressure'] for data in weather_data]

        return {
            'avg_temperature': median(temps),
            'avg_humidity': median(humidity),
            'avg_pressure': median(pressure),
            'station_count': len(weather_data)
        }
