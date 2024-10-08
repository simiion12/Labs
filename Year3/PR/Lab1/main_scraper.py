from parser import CarScraper
from web_utils import get_car_objects_from_data, save_json, save_xml, read_json, read_xml
from web_utils import change_to_mdl_currency, save_statistics
from statistics import Statistics


def main():
    base_url = "https://sargutrans.md/page/{}/"
    final_cars = []

    # for i in range(1, 2):
    #     url = base_url.format(i)

    #     final_cars.extend(parse_page(url))
    final_cars = CarScraper("https://sargutrans.md/page/1/").parse_page()
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
