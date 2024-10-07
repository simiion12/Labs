class Car:
    def __init__(self, capacit_motor, tip_combustibil, anul_fabricatiei, cutia_de_viteze, marca, modelul, tip_tractiune, distanta_parcursa, tip_caroserie, price, link):
        self.capacit_motor = capacit_motor
        self.tip_combustibil = tip_combustibil
        self.anul_fabricatiei = anul_fabricatiei
        self.cutia_de_viteze = cutia_de_viteze
        self.marca = marca
        self.modelul = modelul
        self.tip_tractiune = tip_tractiune
        self.distanta_parcursa = distanta_parcursa
        self.tip_caroserie = tip_caroserie
        self.price = price
        self.link = link

    def to_json(self):
        return {
            "Capacit. motor": self.capacit_motor,
            "Tip combustibil": self.tip_combustibil,
            "Anul fabricației": self.anul_fabricatiei,
            "Cutia de viteze": self.cutia_de_viteze,
            "Marcă": self.marca,
            "Modelul": self.modelul,
            "Tip tractiune": self.tip_tractiune,
            "Distanță parcursă": self.distanta_parcursa,
            "Tip caroserie": self.tip_caroserie,
            "price": self.price,
            "link": self.link
        }

    def to_xml(self):
        xml_str = (
            f"<Car>\n"
            f"    <Capacit_motor>{self.capacit_motor}</Capacit_motor>\n"
            f"    <Tip_combustibil>{self.tip_combustibil}</Tip_combustibil>\n"
            f"    <Anul_fabricatiei>{self.anul_fabricatiei}</Anul_fabricatiei>\n"
            f"    <Cutia_de_viteze>{self.cutia_de_viteze}</Cutia_de_viteze>\n"
            f"    <Marca>{self.marca}</Marca>\n"
            f"    <Modelul>{self.modelul}</Modelul>\n"
            f"    <Tip_tractiune>{self.tip_tractiune}</Tip_tractiune>\n"
            f"    <Distanta_parcursa>{self.distanta_parcursa}</Distanta_parcursa>\n"
            f"    <Tip_caroserie>{self.tip_caroserie}</Tip_caroserie>\n"
            f"    <Price>{self.price}</Price>\n"
            f"    <Link>{self.link}</Link>\n"
            f"</Car>\n"
        )

        return xml_str

    @staticmethod
    def serialize_list_to_json(cars):
        json_list = []
        for car in cars:
            json_list.append(car.to_json())
        json_str = '[' + ', '.join(
            '{' + ', '.join(f'"{k}": "{v}"' for k, v in car.items()) + '}' for car in json_list
        ) + ']'
        return json_str

    @staticmethod
    def serialize_list_to_xml(cars):
        xml_list_str = '<Cars>'
        for car in cars:
            xml_list_str += car.to_xml()
        xml_list_str += '</Cars>'
        return xml_list_str


# data = [{'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2021', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'E-Class', 'Tip tractiune': 'Din spate', 'Distanță parcursă': '58 000 km', 'Tip caroserie': 'Sedan', 'price': 42900, 'link': 'https://sargutrans.md/cars/mercedes-e-class-2-0-2021-5/'}, {'Capacit. motor': '0', 'Tip combustibil': 'Electricitate', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Renault', 'Modelul': 'ZOE', 'Tip tractiune': 'Din față', 'Distanță parcursă': '113 000 km', 'Tip caroserie': 'Hatchback', 'price': 15500, 'link': 'https://sargutrans.md/cars/renault-zoe-electric-2019/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Volvo', 'Modelul': 'XC60', 'Tip tractiune': '4×4', 'Distanță parcursă': '149 000 km', 'Tip caroserie': 'Crossover', 'price': 33900, 'link': 'https://sargutrans.md/cars/volvo-xc60-2-0-2022/'}, {'Capacit. motor': '2.2', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'GLC', 'Tip tractiune': '4×4', 'Distanță parcursă': '144 000', 'Tip caroserie': 'Crossover', 'price': 27800, 'link': 'https://sargutrans.md/cars/mercedes-glc-2-2-2017/'}, {'Tip combustibil': 'Electricitate', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'EQC', 'Tip tractiune': '4×4', 'Distanță parcursă': '23 000 km', 'Tip caroserie': 'Crossover', 'price': 49900, 'link': 'https://sargutrans.md/cars/mercedes-eqc-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'BMW', 'Modelul': 'X4', 'Tip tractiune': '4×4', 'Distanță parcursă': '80 000 km', 'Tip caroserie': 'Crossover', 'price': 47900, 'link': 'https://sargutrans.md/cars/bmw-x4-2-0-2022/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Kodiaq', 'Tip tractiune': '4×4', 'Distanță parcursă': '109 000', 'Tip caroserie': 'Crossover', 'price': 32900, 'link': 'https://sargutrans.md/cars/skoda-kodiaq-2-0-2019/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Opel', 'Modelul': 'Grandland X', 'Tip tractiune': 'Din față', 'Distanță parcursă': '128 000', 'Tip caroserie': 'Crossover', 'price': 13900, 'link': 'https://sargutrans.md/cars/opel-grandland-x-1-5-2019/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mercedes', 'Modelul': 'GLE', 'Tip tractiune': '4×4', 'Distanță parcursă': '90 000 km', 'Tip caroserie': 'Crossover', 'price': 64900, 'link': 'https://sargutrans.md/cars/mercedes-gle-2-0-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Superb', 'Tip tractiune': 'Din față', 'Distanță parcursă': '152 000 km', 'Tip caroserie': 'Hatchback', 'price': 21800, 'link': 'https://sargutrans.md/cars/skoda-superb-2-0-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Kadjar', 'Tip tractiune': 'Din față', 'Distanță parcursă': '180 000 km', 'Tip caroserie': 'Crossover', 'price': 11900, 'link': 'https://sargutrans.md/cars/renault-kadjar-1-5-2017/'}, {'Capacit. motor': '3.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2013', 'Cutia de viteze': 'Automată', 'Marcă': 'Land Rover', 'Modelul': 'Range Rover', 'Tip tractiune': '4×4', 'Distanță parcursă': '160 000 km', 'Tip caroserie': 'SUV', 'price': 32900, 'link': 'https://sargutrans.md/cars/land-rover-range-rover-3-0-2013/'}, {'Capacit. motor': '2.4', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2014', 'Cutia de viteze': 'Automată', 'Marcă': 'Honda', 'Modelul': 'CR-V', 'Tip tractiune': '4×4', 'Distanță parcursă': '180 000 km', 'Tip caroserie': 'Crossover', 'price': 12400, 'link': 'https://sargutrans.md/cars/honda-cr-v-2-4-2014/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Audi', 'Modelul': 'Q5', 'Tip tractiune': '4×4', 'Distanță parcursă': '7500 km', 'Tip caroserie': 'Crossover', 'price': 39900, 'link': 'https://sargutrans.md/cars/audi-q5-2-0-2022/'}, {'Capacit. motor': '1.6', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2016', 'Cutia de viteze': 'Automată', 'Marcă': 'Hyundai', 'Modelul': 'Accent', 'Tip tractiune': 'Din față', 'Distanță parcursă': '99 000', 'Tip caroserie': 'Sedan', 'price': 9800, 'link': 'https://sargutrans.md/cars/hyundai-accent-1-6-2016/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Renault', 'Modelul': 'Talisman', 'Tip tractiune': 'Din față', 'Distanță parcursă': '160 200 km', 'Tip caroserie': 'Universal', 'price': 12800, 'link': 'https://sargutrans.md/cars/renault-talisman-1-5-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2015', 'Cutia de viteze': 'Macanică', 'Marcă': 'Nissan', 'Modelul': 'Qashqai', 'Tip tractiune': 'Din față', 'Distanță parcursă': '165 000 km', 'Tip caroserie': 'Crossover', 'price': 13800, 'link': 'https://sargutrans.md/cars/nissan-qashqai-1-5-2015/'}, {'Capacit. motor': '1.4', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2016', 'Cutia de viteze': 'Macanică', 'Marcă': 'Toyota', 'Modelul': 'Corolla', 'Tip tractiune': 'Din față', 'Distanță parcursă': '123 000 km', 'Tip caroserie': 'Sedan', 'price': 11500, 'link': 'https://sargutrans.md/cars/toyota-corolla-1-4-2016/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2023', 'Cutia de viteze': 'Automată', 'Marcă': 'Toyota', 'Modelul': 'Proace City', 'Tip tractiune': 'Din față', 'Distanță parcursă': '9 700', 'Tip caroserie': 'Minivan', 'price': 28900, 'link': 'https://sargutrans.md/cars/toyota-proace-city-1-5-2023/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2011', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Megane', 'Tip tractiune': 'Din față', 'Distanță parcursă': '220 000 km', 'Tip caroserie': 'Hatchback', 'price': 6400, 'link': 'https://sargutrans.md/cars/renault-megane-1-5-2011/'}, {'Capacit. motor': '3.3', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Toyota', 'Modelul': 'Land Cruiser', 'Tip tractiune': '4×4', 'Distanță parcursă': '79 000 km', 'Tip caroserie': 'SUV', 'price': 73900, 'link': 'https://sargutrans.md/cars/toyota-land-cruiser-3-3-2022/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2019', 'Cutia de viteze': 'Automată', 'Marcă': 'Skoda', 'Modelul': 'Superb', 'Tip tractiune': '4×4', 'Distanță parcursă': '125 000', 'Tip caroserie': 'Sedan', 'price': 31900, 'link': 'https://sargutrans.md/cars/skoda-superb-2-0-2019-3/'}, {'Capacit. motor': '0', 'Tip combustibil': 'Electricitate', 'Anul fabricației': '2022', 'Cutia de viteze': 'Automată', 'Marcă': 'Lexus', 'Modelul': 'UX', 'Tip tractiune': 'Din față', 'Distanță parcursă': '5700 KM', 'Tip caroserie': 'Crossover', 'price': 36800, 'link': 'https://sargutrans.md/cars/lexus-ux-300e-electric-2022/'}, {'Capacit. motor': '3.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'BMW', 'Modelul': '7 Series', 'Tip tractiune': '4×4', 'Distanță parcursă': '138 000 km', 'Tip caroserie': 'Sedan', 'price': 66900, 'link': 'https://sargutrans.md/cars/bmw-7-series-3-0-2020/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Macanică', 'Marcă': 'Renault', 'Modelul': 'Megane', 'Tip tractiune': 'Din față', 'Distanță parcursă': '143 588 km', 'Tip caroserie': 'Universal', 'price': 13800, 'link': 'https://sargutrans.md/cars/renault-megane-1-5-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2017', 'Cutia de viteze': 'Automată', 'Marcă': 'Volvo', 'Modelul': 'S90', 'Tip tractiune': 'Din față', 'Distanță parcursă': '168 050 km', 'Tip caroserie': 'Sedan', 'price': 23900, 'link': 'https://sargutrans.md/cars/volvo-s90-2-0-2017/'}, {'Capacit. motor': '1.5', 'Tip combustibil': 'Benzină', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Mini', 'Modelul': 'One', 'Tip tractiune': 'Din față', 'Distanță parcursă': '27 000 km', 'Tip caroserie': 'Hatchback', 'price': 18500, 'link': 'https://sargutrans.md/cars/mini-one-1-5-2020/'}, {'Capacit. motor': '2.0', 'Tip combustibil': 'Diesel', 'Anul fabricației': '2020', 'Cutia de viteze': 'Automată', 'Marcă': 'Volkswagen', 'Modelul': 'Tiguan', 'Tip tractiune': '4×4', 'Distanță parcursă': '150 000 km', 'Tip caroserie': 'Crossover', 'price': 27900, 'link': 'https://sargutrans.md/cars/volkswagen-tiguan-2-0-2020/'}]

def get_car_objects_from_data(data):
    return [Car(d.get('Capacit. motor', 'N/A'), d.get('Tip combustibil', 'N/A'), d.get('Anul fabricației', 'N/A'),
                d.get('Cutia de viteze', 'N/A'), d.get('Marcă', 'N/A'), d.get('Modelul', 'N/A'),
                d.get('Tip tractiune', 'N/A'), d.get('Distanță parcursă', 'N/A'), d.get('Tip caroserie', 'N/A'),
                d.get('price', 0), d.get('link', 'N/A')) for d in data]


def save_json(cars):
    json_output = Car.serialize_list_to_json(cars)
    with open('cars.json', 'w', encoding='utf-8') as f:
        f.write(json_output)


def save_xml(cars):
    xml_output = Car.serialize_list_to_xml(cars)
    with open('cars.xml', 'w', encoding='utf-8') as f:
        f.write(xml_output)
