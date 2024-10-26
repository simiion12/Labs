from dataclasses import dataclass
from datetime import datetime



@dataclass
class Location:
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime:datetime

    @classmethod
    def from_dict(cls, data: dict) -> 'Location':
        return cls(
            name=data['name'],
            region=data['region'],
            country=data['country'],
            lat=data['lat'],
            lon=data['lon'],
            tz_id=data['tz_id'],
            localtime_epoch=data['localtime_epoch'],
            localtime=datetime.strptime(data['localtime'], '%Y-%m-%d %H:%M')
        )

@dataclass
class Astronomy:
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moon_phase: str
    moon_illumination: str
    is_moon_up: bool
    is_sun_up: bool

    @classmethod
    def from_dict(cls, data: dict) -> 'Astronomy':
        astro_data = data['astro']
        return cls(
            sunrise=astro_data['sunrise'],
            sunset=astro_data['sunset'],
            moonrise=astro_data['moonrise'],
            moonset=astro_data['moonset'],
            moon_phase=astro_data['moon_phase'],
            moon_illumination=astro_data['moon_illumination'],
            is_moon_up=bool(astro_data['is_moon_up']),
            is_sun_up=bool(astro_data['is_sun_up'])
        )

@dataclass
class WeatherData:
    location: Location
    astronomy: Astronomy
