from bs4 import BeautifulSoup
from Labs.Year3.PR.Lab1.web_utils import get_webpage
import re


class CarScraper:
    def __init__(self, url):
        self.url = url
        self.cars = []

    def parse_page(self):
        """Fetch the webpage and parse car links."""
        try:
            html_content = get_webpage(self.url)
            soup = BeautifulSoup(html_content, 'html.parser')
            car_links = self.get_car_links(soup)
            self.cars = self.parse_car_links(car_links)
        except Exception as e:
            print(f"Error in parse_page: {e}")
        return self.cars

    def parse_car_links(self, links):
        """Parse car data from each link."""
        car_data = []
        try:
            for link in links:
                try:
                    html_content = get_webpage(link)
                    soup = BeautifulSoup(html_content, 'html.parser')
                    car_data.append(self.parse_car_data(soup, link))
                except Exception as e:
                    print(f"Error in parse_car_links for link {link}: {e}")
                    continue
            return car_data
        except Exception as e:
            print(f"Error in parse_car_links: {e}")
            return car_data

    @staticmethod
    def get_car_links(soup):
        """Extract car links from the primary div."""
        try:
            primary_div = soup.find('div', id='primary')
            cars_links = primary_div.find_all('a', href=re.compile(r'^https://sargutrans.md/cars/'))
            links = set([a['href'] for a in cars_links])
            return links
        except Exception as e:
            print(f"Error in get_car_links: {e}")
            return set()

    @staticmethod
    def process_price(amount):
        """Process price, by removing EU stamp, the dot and spaces"""
        try:
            amount = int(amount.replace('€', '').replace(' ', '').replace('.', ''))
            if amount > 1000:
                return amount
        except Exception as e:
            print(f"Error in process_price: {e}")
            return 0

    @staticmethod
    def parse_car_data(soup, car_link):
        """Extract car data from the soup object."""
        car_data = {}
        try:
            prod_right_div = soup.find('div', class_='prod-right')
            table = prod_right_div.find('table')
            rows = table.find_all('tr')

            if len(rows) == 0:
                return car_data

            for row in rows:
                try:
                    key = row.find('th').text
                    if key == 'Для подборки':
                        continue
                    value = row.find('td').text.strip()
                    car_data[key] = value
                except Exception as e:
                    print(f"Error in row parsing: {e}")
                    continue

            car_data['price'] = CarScraper.process_price(prod_right_div.find('bdi').text)
            car_data['link'] = car_link

            return car_data

        except AttributeError as e:
            print(f"Error in parse_car_data: {e}")
            return car_data
        except Exception as e:
            print(f"Unexpected error in parse_car_data: {e}")
            return car_data
