from web_utils import read_json
from functools import reduce


def count_cars_by_fuel(file_path, car_type):
    """Using filter reduce to count cars by fuel type."""
    cars = read_json(file_path)
    filtered_cars = list(filter(lambda car: car.get("Tip combustibil").lower() == car_type.lower(), cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count


def count_cars_by_maximum_price(file_path, price):
    """Using filter reduce to count cars by price."""
    cars = read_json(file_path)
    filtered_cars = list(filter(lambda car: car.get("price") < price, cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count


def count_cars_by_minimum_price(file_path, price):
    """Using filter reduce to count cars by price."""
    cars = read_json(file_path)
    filtered_cars = list(filter(lambda car: car.get("price") > price, cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count



