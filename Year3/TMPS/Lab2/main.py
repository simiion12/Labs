import requests
from anyio import sleep

from config import API_KEY
from Labs.Year3.TMPS.Lab2.cache.cache_manager import *
from Labs.Year3.TMPS.Lab2.parsers.parser_factory import WeatherParserFactory
from Labs.Year3.TMPS.Lab2.builders.weather_report_builder import WeatherReportBuilder, WeatherReportDirector

import time
url = f"http://api.weatherapi.com/v1/astronomy.json"

q = 'Paris'
dt = '2024-10-25'
params = {'key': API_KEY, 'q': q, 'dt': dt}

cache = WeatherDataCache()
cache.set_ttl(minutes=15)
cache.set_max_size(100)

key = generate_weather_cache_key(q, dt)
response = requests.get(url, params=params)
data = response.text

weather_data = WeatherParserFactory.get_parser('json').parse(data)
builder = WeatherReportBuilder(weather_data)
basic_report = WeatherReportDirector.create_basic_report(builder)
print("Basic Report:")
print(basic_report)

print(data)

# print("First request:")
# if cache.get(key):
#     print("Retrieved from cache:", cache.get(key))
# else:
#     response = requests.get(url, params=params)
#     data = response.text
#     parsed_data = WeatherParserFactory.get_parser('xml').parse(data)
#     cache.set(key, parsed_data)
#     print("Retrieved from API:", parsed_data)
# time.sleep(10)
# print("\nSecond request:")
# if cache.get(key):
#     print("Retrieved from cache:", cache.get(key))
# else:
#     response = requests.get(url, params=params)
#     data = response.text
#     parsed_data = WeatherParserFactory.get_parser('xml').parse(data)
#     cache.set(key, parsed_data)
#     print("Retrieved from API:", parsed_data)
# time.sleep(10)
#
# print("\nThird request:")
# if cache.get(key):
#     print("Retrieved from cache:", cache.get(key))
# else:
#     response = requests.get(url, params=params)
#     data = response.text
#     parsed_data = WeatherParserFactory.get_parser('xml').parse(data)
#     cache.set(key, parsed_data)
#     print("Retrieved from API:", parsed_data)