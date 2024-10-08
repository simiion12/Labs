class Car:
    def __init__(self, capacit_motor=None, tip_combustibil=None, anul_fabricatiei=None, cutia_de_viteze=None,
                 marca=None, modelul=None, tip_tractiune=None, distanta_parcursa=None, tip_caroserie=None, price=None,
                 link=None):
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

    @classmethod
    def from_json(cls, json_data):
        return cls(
            capacit_motor=json_data.get("Capacit. motor"),
            tip_combustibil=json_data.get("Tip combustibil"),
            anul_fabricatiei=json_data.get("Anul fabricației"),
            cutia_de_viteze=json_data.get("Cutia de viteze"),
            marca=json_data.get("Marcă"),
            modelul=json_data.get("Modelul"),
            tip_tractiune=json_data.get("Tip tractiune"),
            distanta_parcursa=json_data.get("Distanță parcursă"),
            tip_caroserie=json_data.get("Tip caroserie"),
            price=json_data.get("price"),
            link=json_data.get("link")
        )

    @classmethod
    def from_xml(cls, xml_str):
        car_data = {}
        lines = xml_str.strip().split('\n')
        for line in lines[1:-1]:  # Skip first and last lines (opening and closing Car tags)
            key, value = line.strip().split('>')
            key = key[1:].lower().replace('_', ' ')
            value = value.split('<')[0]
            car_data[key] = value

        return cls(
            capacit_motor=car_data.get("capacit motor"),
            tip_combustibil=car_data.get("tip combustibil"),
            anul_fabricatiei=car_data.get("anul fabricatiei"),
            cutia_de_viteze=car_data.get("cutia de viteze"),
            marca=car_data.get("marca"),
            modelul=car_data.get("modelul"),
            tip_tractiune=car_data.get("tip tractiune"),
            distanta_parcursa=car_data.get("distanta parcursa"),
            tip_caroserie=car_data.get("tip caroserie"),
            price=car_data.get("price"),
            link=car_data.get("link")
        )

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
