from parser import CarScraper
from web_utils import get_car_objects_from_data, save_json, save_xml


def main():
    base_url = "https://sargutrans.md/page/{}/"
    final_cars = []

    # for i in range(1, 2):
    #     url = base_url.format(i)

    #     final_cars.extend(parse_page(url))
    final_cars = CarScraper("https://sargutrans.md/page/1/").parse_page()
    car_objects = get_car_objects_from_data(final_cars)
    save_json(car_objects)
    save_xml(car_objects)
    print(final_cars)
    print(len(final_cars))


if __name__ == "__main__":
    main()
