from Labs.Year3.PR.Lab1.parser import CarScraper
from Labs.Year3.PR.Lab1.web_utils import get_car_objects_from_data, save_json, save_xml, read_json
from Labs.Year3.PR.Lab1.web_utils import change_to_mdl_currency, save_statistics
from Labs.Year3.PR.Lab1.statistics import Statistics


def main():
    base_url = "https://sargutrans.md/page/{}/"
    final_cars = []

    for i in range(2, 4):
        url = base_url.format(i)
        final_cars.extend(CarScraper(url).parse_page())

    final_cars_mdl_currency = change_to_mdl_currency(final_cars)
    car_objects = get_car_objects_from_data(final_cars_mdl_currency)
    filename_json, filename_xml = 'cars.json', 'cars.xml'
    save_json(car_objects, filename=filename_json)
    save_xml(car_objects, filename=filename_xml)

    cars = read_json(filename_json)
    statistics = Statistics(cars).get_statistics()
    save_statistics(statistics, 'statistics.json')


if __name__ == "__main__":
    main()
