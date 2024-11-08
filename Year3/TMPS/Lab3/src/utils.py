from Labs.Year3.TMPS.Lab3.src.builders.weather_report_builder import WeatherReportBuilder
from Labs.Year3.TMPS.Lab3.src.builders.weather_report_director import WeatherReportDirector


def choose_format():
    print("Choose the format of the weather report:")
    print("1. JSON")
    print("2. XML")
    choice = input("Enter your choice: ")

    # Mapping of choices to format types
    format_mapping = {
        "1": "json",
        "2": "xml"
    }

    while choice not in format_mapping:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")

    return format_mapping[choice]  # Return the format string (e.g., "json" or "xml")


def choose_report_type():
    print("Choose the type of the weather report:")
    print("1. Basic")
    print("2. Standard")
    print("3. Advanced")
    choice = int(input("Enter your choice: "))
    while choice != 1 and choice != 2 and choice != 3:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
    return choice


def generate_report(weather_data, report_type):
    director = WeatherReportDirector()
    director.builder = WeatherReportBuilder()
    if report_type == 1:
        return director.create_basic_report(weather_data)
    elif report_type == 2:
        return director.create_standard_report(weather_data)
    elif report_type == 3:
        return director.create_advanced_report(weather_data)
    else:
        return None
