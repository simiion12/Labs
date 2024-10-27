import requests

from Labs.Year3.TMPS.Lab2.src.utils import choose_format, choose_report_type, generate_report
from Labs.Year3.TMPS.Lab2.src.config import API_KEY, URL
from Labs.Year3.TMPS.Lab2.src.parsers.parser_factory import WeatherParserFactory
from Labs.Year3.TMPS.Lab2.src.cache.cache_manager import WeatherDataCache, generate_weather_cache_key


def main():
    print("Weather Report Builder")
    print("1. Enter the location, date and format to get the weather report")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 2:
        if choice == 1:
            location = input("Enter the location: ")
            date = input("Enter the date (yyyy-mm-dd): ")
            format = choose_format()
            params = {'key': API_KEY, 'q': location, 'dt': date}
            url = URL + f".{format}"
            response = requests.get(url, params=params)

            cache = WeatherDataCache()
            cache.set_ttl(minutes=15)
            cache.set_max_size(100)
            key = generate_weather_cache_key(location, date)
            if cache.get(key) is None:
                weather_data = WeatherParserFactory.get_parser(format).parse(response.text)
                cache.set(key, weather_data)
                report_type = choose_report_type()
                report = generate_report(weather_data, report_type)
                print(report)
            else:
                weather_data = cache.get(key)
                report_type = choose_report_type()
                report = generate_report(weather_data, report_type)
                print(report)
        else:
            print("Invalid choice. Please try again.")

        print("1. Enter the location, date and format to get the weather report")
        print("2. Exit")

    print("Exiting program.")

if __name__ == '__main__':
    main()
