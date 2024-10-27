from typing import Dict, Any
from Labs.Year3.TMPS.Lab2.models.models import Location, Current, Day
from Labs.Year3.TMPS.Lab2.models.weather_report_models import *


class WeatherReportBuilder:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._report_data: Dict[str, Any] = {}

    def set_location_data(self, location: Location) -> 'WeatherReportBuilder':
        """Set basic location data"""
        self._report_data.update({
            'location_name': location.name,
            'country': location.country
        })
        return self

    def set_standard_location_data(self, location: Location) -> 'WeatherReportBuilder':
        """Set extended location data"""
        self.set_location_data(location)
        self._report_data.update({
            'region': location.region,
            'lat': location.lat,
            'lon': location.lon,
            'tz_id': location.tz_id
        })
        return self

    def set_current_conditions(self, current: Current) -> 'WeatherReportBuilder':
        """Set basic current conditions"""
        self._report_data.update({
            'temperature_c': current.temp_c,
            'humidity': current.humidity,
            'pressure_mb': current.pressure_mb,
            'wind_mph': current.wind_mph,
            'feels_like_c': current.feelslike_c,
            'precipitation_mm': current.precip_mm,
            'cloud_coverage': current.cloud
        })
        return self

    def set_advanced_conditions(self, current: Current) -> 'WeatherReportBuilder':
        """Set advanced current conditions"""
        self.set_current_conditions(current)
        self._report_data.update({
            'windchill_c': current.windchill_c,
            'heatindex_c': current.heatindex_c
        })
        return self

    def set_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set basic day data"""
        self._report_data['condition'] = day.condition
        return self

    def set_standard_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set extended day data"""
        self.set_day_data(day)
        self._report_data.update({
            'max_temp_c': day.maxtemp_c,
            'min_temp_c': day.mintemp_c,
            'avg_temp_c': day.avgtemp_c,
            'max_wind_mph': day.maxwind_mph,
            'avg_humidity': day.avghumidity,
            'chance_of_rain': day.daily_chance_of_rain,
            'chance_of_snow': day.daily_chance_of_snow
        })
        return self

    def set_advanced_day_data(self, day: Day) -> 'WeatherReportBuilder':
        """Set advanced day data"""
        self.set_standard_day_data(day)
        self._report_data['visibility_km'] = day.avgvis_km
        return self

    def set_astronomy_data(self, astronomy: Astronomy) -> 'WeatherReportBuilder':
        """Set astronomy data"""
        self._report_data['astronomy'] = astronomy
        return self

    def build_basic(self) -> BaseWeatherReport:
        """Build basic weather report"""
        report = BaseWeatherReport(**self._report_data)
        self.reset()
        return report

    def build_standard(self) -> StandardWeatherReport:
        """Build standard weather report"""
        report = StandardWeatherReport(**self._report_data)
        self.reset()
        return report

    def build_advanced(self) -> AdvancedWeatherReport:
        """Build advanced weather report"""
        report = AdvancedWeatherReport(**self._report_data)
        self.reset()
        return report
