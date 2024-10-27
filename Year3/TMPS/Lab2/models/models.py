from dataclasses import dataclass
from datetime import datetime
import xml.etree.ElementTree as ET


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

    @classmethod
    def from_xml(cls, data: str) -> 'Location':
        root = ET.fromstring(data)
        return cls(
            name=root.find('location/name').text,
            region=root.find('location/region').text,
            country=root.find('location/country').text,
            lat=float(root.find('location/lat').text),
            lon=float(root.find('location/lon').text),
            tz_id=root.find('location/tz_id').text,
            localtime_epoch=int(root.find('location/localtime_epoch').text),
            localtime=datetime.strptime(root.find('location/localtime').text, '%Y-%m-%d %H:%M')
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

    @classmethod
    def from_xml(cls, data: str) -> 'Astronomy':
        root = ET.fromstring(data)
        astro = root.find('astronomy/astro')
        return cls(
            sunrise=astro.find('sunrise').text,
            sunset=astro.find('sunset').text,
            moonrise=astro.find('moonrise').text,
            moonset=astro.find('moonset').text,
            moon_phase=astro.find('moon_phase').text,
            moon_illumination=astro.find('moon_illumination').text,
            is_moon_up=bool(astro.find('is_moon_up').text),
            is_sun_up=bool(astro.find('is_sun_up').text)
        )

@dataclass
class WeatherData:
    location: Location
    astronomy: Astronomy
