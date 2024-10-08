from functools import reduce


def change_to_mdl_currency(cars):
    """Change the price of the cars from EUR to MDL using Map."""
    def update_price(car):
        updated_car = car.copy()
        updated_car["price"] = float(car.get("price", 0)) * 20.5
        return updated_car

    cars_price_mdl = list(map(update_price, cars))

    return cars_price_mdl


def filter_cars_by_make(cars, make):
    filtered_cars = list(filter(lambda car: car.get("Marcă").lower() == make.lower(), cars))
    return filtered_cars


def count_cars_by_fuel(cars, car_type):
    """Using filter reduce to count cars by fuel type."""
    filtered_cars = list(filter(lambda car: car.get("Tip combustibil").lower() == car_type.lower(), cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count


def count_cars_by_maximum_price(cars, price, ascending=True):
    """Using filter reduce to count cars by price and ascending."""
    if ascending:
        filtered_cars = list(filter(lambda car: car.get("price") >= price, cars))
    else:
        filtered_cars = list(filter(lambda car: car.get("price") < price, cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count


def count_cars_by_year(cars, year):
    """Using filter reduce to count cars by year."""
    filtered_cars = list(filter(lambda car: car.get("Anul fabricației") == year, cars))
    count = reduce(lambda x, y: x + 1, filtered_cars, 0)
    return count
