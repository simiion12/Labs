from dataclasses import dataclass
from datetime import datetime
from Year3.TMPS.Lab4.src.models.models import Astronomy


@dataclass
class BaseWeatherReport:
    location_name: str
    country: str
    temperature_c: float
    humidity: int
    pressure_mb: float
    condition: str
    wind_mph: float
    feels_like_c: float
    precipitation_mm: float
    cloud_coverage: int


    def __str__(self) -> str:
        return f"""
Weather Report for {self.location_name}, {self.country}
Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Current Conditions:
  Temperature: {self.temperature_c}°C (Feels like: {self.feels_like_c}°C)
  Humidity: {self.humidity}%
  Pressure: {self.pressure_mb} mb
  Condition: {self.condition}
  Wind: {self.wind_mph} mph
  Precipitation: {self.precipitation_mm} mm
  Cloud Coverage: {self.cloud_coverage}%
"""


@dataclass
class StandardWeatherReport(BaseWeatherReport):
    region: str
    lat: float
    lon: float
    tz_id: str
    max_temp_c: float
    min_temp_c: float
    avg_temp_c: float
    max_wind_mph: float
    avg_humidity: int
    chance_of_rain: str
    chance_of_snow: str

    def __str__(self) -> str:
        base_report = super().__str__()
        return f"""{base_report}
Additional Information:
  Location: {self.region} ({self.lat}, {self.lon})
  Time Zone: {self.tz_id}

Daily Statistics:
  Temperature Range: {self.min_temp_c}°C to {self.max_temp_c}°C
  Average Temperature: {self.avg_temp_c}°C
  Maximum Wind: {self.max_wind_mph} mph
  Average Humidity: {self.avg_humidity}%
  Precipitation Chance: Rain {self.chance_of_rain}, Snow {self.chance_of_snow}
"""


@dataclass
class AdvancedWeatherReport(StandardWeatherReport):
    astronomy: Astronomy
    windchill_c: float
    heatindex_c: float
    visibility_km: float

    def __str__(self) -> str:
        standard_report = super().__str__()
        return f"""{standard_report}
Astronomical Data:
  Sunrise: {self.astronomy.sunrise}
  Sunset: {self.astronomy.sunset}
  Moonrise: {self.astronomy.moonrise}
  Moonset: {self.astronomy.moonset}
  Moon Phase: {self.astronomy.moon_phase}
  Moon Illumination: {self.astronomy.moon_illumination}
  Moon Status: {"Up" if self.astronomy.is_moon_up else "Down"}
  Sun Status: {"Up" if self.astronomy.is_sun_up else "Down"}

Detailed Conditions:
  Wind Chill: {self.windchill_c}°C
  Heat Index: {self.heatindex_c}°C
  Visibility: {self.visibility_km} km
"""