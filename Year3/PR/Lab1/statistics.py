from functools import reduce


class Statistics:
    def __init__(self, cars):
        self.cars = cars

    def get_statistics(self):
        """Return a dictionary with statistics about the cars."""
        if not self.cars:
            return {}
        return {
            "total_cars": len(self.cars),
            "total_price": self.get_total_price(),
            "average_price": self.get_average_price(),
            "most_expensive_car": self.get_most_expensive_car(),
            "cheapest_car": self.get_cheapest_car(),
            "average_year": self.get_average_year(),
            "cars_under_400000": self.ratio_cars_by_maximum_price(400000),
            "cars_upper_400000": self.ratio_cars_by_maximum_price(400000, False),
            "diesel_cars": self.ratio_cars_by_fuel("Diesel"),
            "petrol_cars": self.ratio_cars_by_fuel("Benzină"),
            "electric_cars": self.ratio_cars_by_fuel("Electric"),
            "hybrid_cars": self.ratio_cars_by_fuel("Hybrid"),
            "cars_under_2020": self.ratio_cars_by_year("2020"),
            "cars_upper_2020": self.ratio_cars_by_year(2020, False),
            "bmw_cars": self.ratio_cars_by_make("BMW"),
            "audi_cars": self.ratio_cars_by_make("Audi"),
            "mercedes_cars": self.ratio_cars_by_make("Mercedes"),
            "volkswagen_cars": self.ratio_cars_by_make("Volkswagen"),
            "toyota_cars": self.ratio_cars_by_make("Toyota"),
            "skoda_cars": self.ratio_cars_by_make("Skoda"),
            "tesla_cars": self.ratio_cars_by_make("Tesla"),
        }

    def get_total_price(self):
        """Calculate the total price of cars."""
        def safe_price(car):
            try:
                return float(car.get("price", 0))
            except (ValueError, TypeError):
                print(f"Error in get_total_price: {car}")
                return 0
        return int(reduce(lambda acc, car: acc + safe_price(car), self.cars, 0))

    def get_average_price(self):
        """Calculate the average price of cars."""
        try:
            total_price = self.get_total_price()
            return round(total_price / len(self.cars), 2)
        except ZeroDivisionError:
            print("Error in get_average_price: Division by zero")
            return 0

    def get_most_expensive_car(self):
        """Get the car with the highest price, handling possible invalid price values."""
        try:
            return max(self.cars, key=lambda car: float(car.get("price", 0)) if car.get("price") else 0)
        except (ValueError, TypeError):
            return None

    def get_cheapest_car(self):
        """Get the car with the lowest price, handling possible invalid price values,
         and ensuring price is above 20,000."""
        try:
            valid_cars = [car for car in self.cars if car.get("price") and float(car["price"]) > 20000]
            if not valid_cars:
                return None
            return min(valid_cars, key=lambda car: float(car["price"]))
        except (ValueError, TypeError):
            return None

    def get_average_year(self):
        """Calculate the average year of cars."""
        years = []
        for car in self.cars:
            try:
                year = int(car.get("Anul fabricației", 2018))
                years.append(year)
            except (ValueError, TypeError):
                continue
        if not years:
            return 0
        return round(sum(years) / len(years), 0)

    def ratio_cars_by_make(self, make):
        """Count cars where the make is contained in the 'Marcă' field."""
        def safe_filter(car):
            try:
                return make.lower() in car.get("Marcă", "").lower()
            except (ValueError, TypeError):
                return False
        filtered_cars = filter(safe_filter, self.cars)
        count = reduce(lambda acc, _: acc + 1, filtered_cars, 0)
        return round(count/len(self.cars), 2)

    def ratio_cars_by_fuel(self, fuel_type):
        """Count cars where the fuel type is contained in the 'Tip combustibil' field."""
        def safe_filter(car):
            try:
                return fuel_type.lower() in car.get("Tip combustibil", "").lower()
            except (ValueError, TypeError):
                return False
        filtered_cars = filter(safe_filter, self.cars)
        count = reduce(lambda acc, _: acc + 1, filtered_cars, 0)
        return round(count/len(self.cars), 2)

    def ratio_cars_by_maximum_price(self, price, ascending=True):
        """Using filter reduce to count cars by price and ascending."""
        def safe_filter(car):
            try:
                return float(car.get("price", 0)) >= float(price) if ascending else float(car.get("price", 0)) < float(price)
            except (ValueError, TypeError):
                return False
        filtered_cars = filter(safe_filter, self.cars)
        count = reduce(lambda x, y: x + 1, filtered_cars, 0)
        return round(count/len(self.cars), 2)

    def ratio_cars_by_year(self, year, ascending=True):
        """Using filter reduce to count cars by year."""
        def safe_filter(car):
            try:
                return int(car.get("Anul fabricației", 0)) >= int(year) if ascending else int(car.get("Anul fabricației", 0)) < int(year)
            except (ValueError, TypeError):
                return False

        filtered_cars = filter(safe_filter, self.cars)
        count = reduce(lambda acc, _: acc + 1, filtered_cars, 0)
        return round(count/len(self.cars), 2)
