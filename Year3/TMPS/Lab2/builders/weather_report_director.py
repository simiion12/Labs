from Labs.Year3.TMPS.Lab2.builders.weather_report_builder import WeatherReportBuilder
from Labs.Year3.TMPS.Lab2.models.models import WeatherData
from Labs.Year3.TMPS.Lab2.models.weather_report_models import BaseWeatherReport, StandardWeatherReport, \
    AdvancedWeatherReport


class WeatherReportDirector:
    def __init__(self):
        self._builder = WeatherReportBuilder()

    def create_basic_report(self, weather_data: WeatherData) -> BaseWeatherReport:
        try:
            self._builder.reset()
            self._builder.set_location_data(weather_data.location)
            self._builder.set_current_conditions(weather_data.current)
            self._builder.set_day_data(weather_data.day)
            return self._builder.build_basic()

        except Exception as e:
            print(f"Error during report creation: {str(e)}")
            raise

    def create_standard_report(self, weather_data: WeatherData) -> StandardWeatherReport:
        try:
            self._builder.reset()
            self._builder.set_standard_location_data(weather_data.location)
            self._builder.set_current_conditions(weather_data.current)
            self._builder.set_standard_day_data(weather_data.day)
            return self._builder.build_standard()
        except Exception as e:
            print(f"Error during standard report creation: {str(e)}")
            raise

    def create_advanced_report(self, weather_data: WeatherData) -> AdvancedWeatherReport:
        try:
            self._builder.reset()
            self._builder.set_standard_location_data(weather_data.location)
            self._builder.set_advanced_conditions(weather_data.current)
            self._builder.set_advanced_day_data(weather_data.day)
            self._builder.set_astronomy_data(weather_data.astronomy)
            return self._builder.build_advanced()
        except Exception as e:
            print(f"Error during advanced report creation: {str(e)}")
            raise
