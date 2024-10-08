from functools import reduce


class Statistics:
    def __init__(self, cars):
        self.cars = cars

    def get_statistics(self):
        return {
            "total_cars": len(self.cars),
            "total_price": self.get_total_price(),
            "average_price": self.get_average_price(),
            "most_expensive_car": self.get_most_expensive_car(),
            "cheapest_car": self.get_cheapest_car(),
            "average_year": self.get_average_year(),
            "cars_under_400000": self.count_cars_by_maximum_price(400000),
            "cars_upper_400000": self.count_cars_by_maximum_price(400000, False),
            "diesel_cars": self.count_cars_by_fuel("Diesel"),
            "petrol_cars": self.count_cars_by_fuel("Benzină"),
            "electric_cars": self.count_cars_by_fuel("Electric"),
            "hybrid_cars": self.count_cars_by_fuel("Hybrid"),
            "cars_under_2020": self.count_cars_by_year("2020"),
            "cars_upper_2020": self.count_cars_by_year(2020, False),
            "bmw_cars": self.count_cars_by_make("BMW"),
            "audi_cars": self.count_cars_by_make("Audi"),
            "mercedes_cars": self.count_cars_by_make("Mercedes"),
            "volkswagen_cars": self.count_cars_by_make("Volkswagen"),
            "tesla_cars": self.count_cars_by_make("Tesla"),
        }



    def get_total_price(self):
        return reduce(lambda acc, car: acc + float(car.get("price", 0)), self.cars, 0)

    def get_average_price(self):
        return self.get_total_price() / len(self.cars) if len(self.cars) > 0 else 0

    def get_most_expensive_car(self):
        return max(self.cars, key=lambda car: car.get("price", 0))

    def get_cheapest_car(self):
        return min(self.cars, key=lambda car: car.get("price", 0))

    def get_average_year(self):
        years = [int(car.get("Anul fabricației", 0)) for car in self.cars]
        return sum(years) / len(years) if len(years) > 0 else 0

    def count_cars_by_make(self, make):
        """Count cars where the make is contained in the 'Marcă' field."""
        mapped_cars = map(lambda car: make.lower() in car.get("Marcă", "").lower(), self.cars)
        return reduce(lambda acc, x: acc + (1 if x else 0), mapped_cars, 0)

    def count_cars_by_fuel(self, fuel_type):
        """Count cars where the fuel type is contained in the 'Tip combustibil' field."""
        mapped_cars = map(lambda car: fuel_type.lower() in car.get("Tip combustibil", "").lower(), self.cars)
        return reduce(lambda acc, x: acc + (1 if x else 0), mapped_cars, 0)

    def count_cars_by_maximum_price(self, price, ascending=True):
        """Using filter reduce to count cars by price and ascending."""
        if ascending:
            filtered_cars = list(filter(lambda car: car.get("price") >= price, self.cars))
        else:
            filtered_cars = list(filter(lambda car: car.get("price") < price, self.cars))
        count = reduce(lambda x, y: x + 1, filtered_cars, 0)
        return count

    def count_cars_by_year(self, year, ascending=True):
        """Using filter reduce to count cars by year."""
        if ascending:
            filtered_cars = list(filter(lambda car: int(car.get("Anul fabricației")) >= int(year), self.cars))
        else:
            filtered_cars = list(filter(lambda car: int(car.get("Anul fabricației")) < int(year), self.cars))
        count = reduce(lambda x, y: x + 1, filtered_cars, 0)
        return count

# data = [{'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2021', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'E-Class', 'Tip tractiune': 'Din spate', 'Distanță parcursă': '58 000 km', 'Tip caroserie': 'Sedan', 'price': 42900, 'link': 'https://sargutrans.md/cars/mercedes-e-class-2-0-2021-5/'}, {'Capacit. motor': '0', 'Tip combustibil': 'Electricitate', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Renault', 'Modelul': 'ZOE', 'Tip tractiune': 'Din față', 'Distanță parcursă': '113 000 km', 'Tip caroserie': 'Hatchback', 'price': 15500, 'link': 'https://sargutrans.md/cars/renault-zoe-electric-2019/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Volvo', 'Modelul': 'XC60', 'Tip tractiune': '4×4', 'Distanță parcursă': '149 000 km', 'Tip caroserie': 'Crossover', 'price': 33900, 'link': 'https://sargutrans.md/cars/volvo-xc60-2-0-2022/'}, {'Capacit. motor': '2.2', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'GLC', 'Tip tractiune': '4×4', 'Distanță parcursă': '144 000', 'Tip caroserie': 'Crossover', 'price': 27800, 'link': 'https://sargutrans.md/cars/mercedes-glc-2-2-2017/'}, {'Tip combustibil': 'Electricitate', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'EQC', 'Tip tractiune': '4×4', 'Distanță parcursă': '23 000 km', 'Tip caroserie': 'Crossover', 'price': 49900, 'link': 'https://sargutrans.md/cars/mercedes-eqc-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'BMW', 'Modelul': 'X4', 'Tip tractiune': '4×4', 'Distanță parcursă': '80 000 km', 'Tip caroserie': 'Crossover', 'price': 47900, 'link': 'https://sargutrans.md/cars/bmw-x4-2-0-2022/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Kodiaq', 'Tip tractiune': '4×4', 'Distanță parcursă': '109 000', 'Tip caroserie': 'Crossover', 'price': 32900, 'link': 'https://sargutrans.md/cars/skoda-kodiaq-2-0-2019/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Opel', 'Modelul': 'Grandland X', 'Tip tractiune': 'Din față', 'Distanță parcursă': '128 000', 'Tip caroserie': 'Crossover', 'price': 13900, 'link': 'https://sargutrans.md/cars/opel-grandland-x-1-5-2019/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'GLE', 'Tip tractiune': '4×4', 'Distanță parcursă': '90 000 km', 'Tip caroserie': 'Crossover', 'price': 64900, 'link': 'https://sargutrans.md/cars/mercedes-gle-2-0-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Superb', 'Tip tractiune': 'Din față', 'Distanță parcursă': '152 000 km', 'Tip caroserie': 'Hatchback', 'price': 21800, 'link': 'https://sargutrans.md/cars/skoda-superb-2-0-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Kadjar', 'Tip tractiune': 'Din față', 'Distanță parcursă': '180 000 km', 'Tip caroserie': 'Crossover', 'price': 11900, 'link': 'https://sargutrans.md/cars/renault-kadjar-1-5-2017/'}, {'Capacit. motor': '3.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2013', 'Cutia de viteze': 'Automată', 'Marcă': 'Land Rover', 'Modelul': 'Range Rover', 'Tip tractiune': '4×4', 'Distanță parcursă': '160 000 km', 'Tip caroserie': 'SUV', 'price': 32900, 'link': 'https://sargutrans.md/cars/land-rover-range-rover-3-0-2013/'}, {'Capacit. motor': '2.4', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2014', 'Cutia de viteze': 'Automată', 'Marcă': 'Honda', 'Modelul': 'CR-V', 'Tip tractiune': '4×4', 'Distanță parcursă': '180 000 km', 'Tip caroserie': 'Crossover', 'price': 12400, 'link': 'https://sargutrans.md/cars/honda-cr-v-2-4-2014/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Audi', 'Modelul': 'Q5', 'Tip tractiune': '4×4', 'Distanță parcursă': '7500 km', 'Tip caroserie': 'Crossover', 'price': 39900, 'link': 'https://sargutrans.md/cars/audi-q5-2-0-2022/'}, {'Capacit. motor': '1.6', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2016', 'Cutia de viteze': 'Automată', 'Marcă': 'Hyundai', 'Modelul': 'Accent', 'Tip tractiune': 'Din față', 'Distanță parcursă': '99 000', 'Tip caroserie': 'Sedan', 'price': 9800, 'link': 'https://sargutrans.md/cars/hyundai-accent-1-6-2016/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Renault', 'Modelul': 'Talisman', 'Tip tractiune': 'Din față', 'Distanță parcursă': '160 200 km', 'Tip caroserie': 'Universal', 'price': 12800, 'link': 'https://sargutrans.md/cars/renault-talisman-1-5-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2015', 'Cutia de viteze': 'Macanică', 'Marcă': 'Nissan', 'Modelul': 'Qashqai', 'Tip tractiune': 'Din față', 'Distanță parcursă': '165 000 km', 'Tip caroserie': 'Crossover', 'price': 13800, 'link': 'https://sargutrans.md/cars/nissan-qashqai-1-5-2015/'}, {'Capacit. motor': '1.4', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2016', 'Cutia de viteze': 'Macanică', 'Marcă': 'Toyota', 'Modelul': 'Corolla', 'Tip tractiune': 'Din față', 'Distanță parcursă': '123 000 km', 'Tip caroserie': 'Sedan', 'price': 11500, 'link': 'https://sargutrans.md/cars/toyota-corolla-1-4-2016/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2023', 'Cutia de viteze': 'Automată', 'Marcă': 'Toyota', 'Modelul': 'Proace City', 'Tip tractiune': 'Din față', 'Distanță parcursă': '9 700', 'Tip caroserie': 'Minivan', 'price': 28900, 'link': 'https://sargutrans.md/cars/toyota-proace-city-1-5-2023/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2011', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Megane', 'Tip tractiune': 'Din față', 'Distanță parcursă': '220 000 km', 'Tip caroserie': 'Hatchback', 'price': 6400, 'link': 'https://sargutrans.md/cars/renault-megane-1-5-2011/'}, {'Capacit. motor': '3.3', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Toyota', 'Modelul': 'Land Cruiser', 'Tip tractiune': '4×4', 'Distanță parcursă': '79 000 km', 'Tip caroserie': 'SUV', 'price': 73900, 'link': 'https://sargutrans.md/cars/toyota-land-cruiser-3-3-2022/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Superb', 'Tip tractiune': '4×4', 'Distanță parcursă': '125 000', 'Tip caroserie': 'Sedan', 'price': 31900, 'link': 'https://sargutrans.md/cars/skoda-superb-2-0-2019-3/'}, {'Capacit. motor': '0', 'Tip combustibil': 'Electricitate', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Lexus', 'Modelul': 'UX', 'Tip tractiune': 'Din față', 'Distanță parcursă': '5700 KM', 'Tip caroserie': 'Crossover', 'price': 36800, 'link': 'https://sargutrans.md/cars/lexus-ux-300e-electric-2022/'}, {'Capacit. motor': '3.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'BMW', 'Modelul': '7 Series', 'Tip tractiune': '4×4', 'Distanță parcursă': '138 000 km', 'Tip caroserie': 'Sedan', 'price': 66900, 'link': 'https://sargutrans.md/cars/bmw-7-series-3-0-2020/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Megane', 'Tip tractiune': 'Din față', 'Distanță parcursă': '143 588 km', 'Tip caroserie': 'Universal', 'price': 13800, 'link': 'https://sargutrans.md/cars/renault-megane-1-5-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Volvo', 'Modelul': 'S90', 'Tip tractiune': 'Din față', 'Distanță parcursă': '168 050 km', 'Tip caroserie': 'Sedan', 'price': 23900, 'link': 'https://sargutrans.md/cars/volvo-s90-2-0-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mini', 'Modelul': 'One', 'Tip tractiune': 'Din față', 'Distanță parcursă': '27 000 km', 'Tip caroserie': 'Hatchback', 'price': 18500, 'link': 'https://sargutrans.md/cars/mini-one-1-5-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Volkswagen', 'Modelul': 'Tiguan', 'Tip tractiune': '4×4', 'Distanță parcursă': '150 000 km', 'Tip caroserie': 'Crossover', 'price': 27900, 'link': 'https://sargutrans.md/cars/volkswagen-tiguan-2-0-2020/'}]
#
# statistics = Statistics(data)
# print(statistics.get_statistics())
