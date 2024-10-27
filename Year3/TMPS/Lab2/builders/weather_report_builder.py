from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from Labs.Year3.TMPS.Lab2.models.models import Location, Astronomy, WeatherData


# Data Classes for different weather components
@dataclass
class Temperature:
    current: float
    feels_like: float
    min: float
    max: float
    unit: str = "°C"


@dataclass
class Humidity:
    value: int
    comfort_level: str  # "Dry", "Comfortable", "Humid"


@dataclass
class Precipitation:
    probability: int
    type: str  # "Rain", "Snow", "None"
    intensity: str  # "Light", "Moderate", "Heavy"
    amount: float
    unit: str = "mm"


@dataclass
class DailyForecast:
    date: datetime
    temperature: Temperature
    humidity: Humidity
    precipitation: Precipitation
    conditions: str  # "Sunny", "Cloudy", "Rainy", etc.


@dataclass
class WeatherReport:
    location: Location
    astronomy: Astronomy
    current_temperature: Optional[Temperature] = None
    current_humidity: Optional[Humidity] = None
    current_precipitation: Optional[Precipitation] = None
    forecast: Optional[List[DailyForecast]] = None
    report_time: datetime = datetime.now()

    def __str__(self) -> str:
        report = f"\nWeather Report for {self.location.name}, {self.location.country}\n"
        report += f"Generated at: {self.report_time.strftime('%Y-%m-%d %H:%M')}\n"
        report += f"\nAstronomy Data:\n"
        report += f"  Sunrise: {self.astronomy.sunrise}\n"
        report += f"  Sunset: {self.astronomy.sunset}\n"

        if self.current_temperature:
            report += f"\nCurrent Temperature:\n"
            report += f"  Current: {self.current_temperature.current}{self.current_temperature.unit}\n"
            report += f"  Feels Like: {self.current_temperature.feels_like}{self.current_temperature.unit}\n"
            report += f"  Min: {self.current_temperature.min}{self.current_temperature.unit}\n"
            report += f"  Max: {self.current_temperature.max}{self.current_temperature.unit}\n"

        if self.current_humidity:
            report += f"\nCurrent Humidity:\n"
            report += f"  Value: {self.current_humidity.value}%\n"
            report += f"  Comfort Level: {self.current_humidity.comfort_level}\n"

        if self.current_precipitation:
            report += f"\nPrecipitation:\n"
            report += f"  Probability: {self.current_precipitation.probability}%\n"
            report += f"  Type: {self.current_precipitation.type}\n"
            report += f"  Intensity: {self.current_precipitation.intensity}\n"
            report += f"  Amount: {self.current_precipitation.amount}{self.current_precipitation.unit}\n"

        if self.forecast:
            report += f"\nForecast:\n"
            for day in self.forecast:
                report += f"\n  Date: {day.date.strftime('%Y-%m-%d')}\n"
                report += f"  Conditions: {day.conditions}\n"
                report += f"  Temperature: {day.temperature.max}/{day.temperature.min}{day.temperature.unit}\n"
                report += f"  Humidity: {day.humidity.value}%\n"
                report += f"  Precipitation: {day.precipitation.probability}% chance of {day.precipitation.type}\n"

        return report


# Abstract Builder
class WeatherReportBuilder:
    def __init__(self, weather_data: WeatherData):
        self._weather_report = WeatherReport(location=weather_data.location, astronomy=weather_data.astronomy)

    def add_temperature(self, current: float, feels_like: float, min_temp: float, max_temp: float,
                        unit: str = "°C") -> 'WeatherReportBuilder':
        self._weather_report.current_temperature = Temperature(
            current=current,
            feels_like=feels_like,
            min=min_temp,
            max=max_temp,
            unit=unit
        )
        return self

    def add_humidity(self, value: int) -> 'WeatherReportBuilder':
        comfort_level = "Comfortable"
        if value < 30:
            comfort_level = "Dry"
        elif value > 70:
            comfort_level = "Humid"

        self._weather_report.current_humidity = Humidity(
            value=value,
            comfort_level=comfort_level
        )
        return self

    def add_precipitation(self, probability: int, type_: str, intensity: str, amount: float,
                          unit: str = "mm") -> 'WeatherReportBuilder':
        self._weather_report.current_precipitation = Precipitation(
            probability=probability,
            type=type_,
            intensity=intensity,
            amount=amount,
            unit=unit
        )
        return self

    def add_forecast_day(self, date: datetime, temp_max: float, temp_min: float,
                         humidity: int, precip_prob: int, precip_type: str,
                         conditions: str) -> 'WeatherReportBuilder':
        if self._weather_report.forecast is None:
            self._weather_report.forecast = []

        forecast_day = DailyForecast(
            date=date,
            temperature=Temperature(
                current=(temp_max + temp_min) / 2,
                feels_like=(temp_max + temp_min) / 2,
                min=temp_min,
                max=temp_max,
                unit="°C"
            ),
            humidity=Humidity(
                value=humidity,
                comfort_level="Comfortable" if 30 <= humidity <= 70 else ("Dry" if humidity < 30 else "Humid")
            ),
            precipitation=Precipitation(
                probability=precip_prob,
                type=precip_type,
                intensity="Light" if precip_prob < 30 else ("Moderate" if precip_prob < 70 else "Heavy"),
                amount=0.0 if precip_prob == 0 else (1.0 if precip_prob < 30 else (5.0 if precip_prob < 70 else 10.0)),
                unit="mm"
            ),
            conditions=conditions
        )

        self._weather_report.forecast.append(forecast_day)
        return self

    def build(self) -> WeatherReport:
        return self._weather_report


# Director class to demonstrate different report configurations
class WeatherReportDirector:
    @staticmethod
    def create_basic_report(builder: WeatherReportBuilder) -> WeatherReport:
        return builder.build()

    @staticmethod
    def create_standard_report(builder: WeatherReportBuilder,
                               temp: float, feels_like: float, min_temp: float, max_temp: float,
                               humidity: int) -> WeatherReport:
        return builder \
            .add_temperature(temp, feels_like, min_temp, max_temp) \
            .add_humidity(humidity) \
            .build()

    @staticmethod
    def create_full_report(builder: WeatherReportBuilder,
                           temp: float, feels_like: float, min_temp: float, max_temp: float,
                           humidity: int,
                           precip_prob: int, precip_type: str, precip_intensity: str,
                           precip_amount: float) -> WeatherReport:
        return builder \
            .add_temperature(temp, feels_like, min_temp, max_temp) \
            .add_humidity(humidity) \
            .add_precipitation(precip_prob, precip_type, precip_intensity, precip_amount) \
            .build()
