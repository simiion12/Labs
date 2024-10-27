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
        astro = root.find('forecast/forecastday/astro')
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
class Current:
    temp_c: float
    wind_mph: float
    pressure_mb: float
    precip_mm: float
    humidity: int
    cloud: int
    feelslike_c: float
    windchill_c: float
    heatindex_c: float

    @classmethod
    def from_dict(cls, data: dict) -> 'Current':
        return cls(
            temp_c=data['temp_c'],
            wind_mph=data['wind_mph'],
            pressure_mb=data['pressure_mb'],
            precip_mm=data['precip_mm'],
            humidity=data['humidity'],
            cloud=data['cloud'],
            feelslike_c=data['feelslike_c'],
            windchill_c=data['windchill_c'],
            heatindex_c=data['heatindex_c']
        )

    @classmethod
    def from_xml(cls, data: str) -> 'Current':
        root = ET.fromstring(data)
        current = root.find('current')
        return cls(
            temp_c=float(current.find('temp_c').text),
            wind_mph=float(current.find('wind_mph').text),
            pressure_mb=float(current.find('pressure_mb').text),
            precip_mm=float(current.find('precip_mm').text),
            humidity=int(current.find('humidity').text),
            cloud=int(current.find('cloud').text),
            feelslike_c=float(current.find('feelslike_c').text),
            windchill_c=float(current.find('windchill_c').text),
            heatindex_c=float(current.find('heatindex_c').text)
        )


@dataclass
class Day:
    maxtemp_c: float
    mintemp_c: float
    avgtemp_c: float
    maxwind_mph: float
    totalprecip_mm: float
    avgvis_km: float
    avghumidity: int
    daily_chance_of_rain: str
    daily_chance_of_snow: str
    condition: str

    @classmethod
    def from_dict(cls, data: dict) -> 'Day':
        day_data = data['day']
        return cls(
            maxtemp_c=day_data['maxtemp_c'],
            mintemp_c=day_data['mintemp_c'],
            avgtemp_c=day_data['avgtemp_c'],
            maxwind_mph=day_data['maxwind_mph'],
            totalprecip_mm=day_data['totalprecip_mm'],
            avgvis_km=day_data['avgvis_km'],
            avghumidity=day_data['avghumidity'],
            daily_chance_of_rain=day_data['daily_chance_of_rain'],
            daily_chance_of_snow=day_data['daily_chance_of_snow'],
            condition=day_data['condition']['text'],
        )

    @classmethod
    def from_xml(cls, data: str) -> 'Day':
        root = ET.fromstring(data)
        day = root.find('forecast/forecastday/day')
        return cls(
            maxtemp_c=float(day.find('maxtemp_c').text),
            mintemp_c=float(day.find('mintemp_c').text),
            avgtemp_c=float(day.find('avgtemp_c').text),
            maxwind_mph=float(day.find('maxwind_mph').text),
            totalprecip_mm=float(day.find('totalprecip_mm').text),
            avgvis_km=float(day.find('avgvis_km').text),
            avghumidity=int(day.find('avghumidity').text),
            daily_chance_of_rain=day.find('daily_chance_of_rain').text,
            daily_chance_of_snow=day.find('daily_chance_of_snow').text,
            condition=day.find('condition/text').text
        )


@dataclass
class WeatherData:
    location: Location
    current: Current
    day: Day
    astronomy: Astronomy
