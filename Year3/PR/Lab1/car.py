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
        """Method to convert the object to a JSON string"""
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
        """Method to convert the object to an XML string"""
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
    def from_json(cls, json_string):
        """Method to create a Car objects from a JSON string"""
        json_string = json_string.strip()
        if not json_string:
            return []

        # Check if it's a JSON array or a single object
        if json_string.startswith('['):
            json_string = json_string[1:-1].strip()
        elif not json_string.startswith('{'):
            raise ValueError("Invalid JSON format")

        # Split the string into individual JSON objects
        json_objects = []
        bracket_count = 0
        current_object = ""

        for char in json_string:
            if char == '{':
                bracket_count += 1
            elif char == '}':
                bracket_count -= 1

            current_object += char

            if bracket_count == 0 and current_object.strip():
                json_objects.append(current_object.strip())
                current_object = ""

        # Parse each JSON object
        parsed_objects = []
        for json_obj in json_objects:
            # Remove the outer braces
            json_obj = json_obj.strip()[1:-1]

            # Split the string into key-value pairs
            pairs = json_obj.split(',')

            # Create a dictionary to store the parsed data
            data = {}

            for pair in pairs:
                if ':' not in pair:
                    continue  # Skip invalid pairs
                key, value = pair.split(':', 1)
                key = key.strip().strip('"')
                value = value.strip().strip('"')

                # Convert to appropriate types
                if value.lower() in ('null', 'n/a', ''):
                    value = 'N/A'
                elif value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                elif value.replace('.', '').isdigit():
                    value = float(value) if '.' in value else int(value)

                data[key] = value

            parsed_objects.append(data)

        return parsed_objects

    @classmethod
    def from_xml(cls, xml_str):
        """Method to create a Car object from an XML string"""
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
        """Method to convert a list of Car objects to a JSON string"""
        json_list = []
        for car in cars:
            json_list.append(car.to_json())
        json_str = '[' + ', '.join(
            '{' + ', '.join(f'"{k}": "{v}"' for k, v in car.items()) + '}' for car in json_list
        ) + ']'
        return json_str

    @staticmethod
    def serialize_list_to_xml(cars):
        """Method to convert a list of Car objects to an XML string"""
        xml_list_str = '<Cars>'
        for car in cars:
            xml_list_str += car.to_xml()
        xml_list_str += '</Cars>'
        return xml_list_str
