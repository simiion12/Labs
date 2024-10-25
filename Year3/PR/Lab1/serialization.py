from typing import Any


class Serializer:
    """
    This class converts Python objects (like dictionaries and lists) into strings
    and back again - like turning a complex object into text that can be saved
    and later rebuilt back into the original object.
    """

    @staticmethod
    def serialize(obj: Any) -> str:
        """
        This is the main function that converts Python objects to strings.
        It's like taking a photo of your data structure - converting it to a format
        that can be easily stored or transmitted.
        """

        if isinstance(obj, dict):
            # Convert each key-value pair and join them with commas
            items = [
                f"{Serializer.serialize(k)}: {Serializer.serialize(v)}"
                for k, v in obj.items()
            ]
            return "{" + ", ".join(items) + "}"


        if isinstance(obj, list):
            # Convert each item and join them with commas
            items = [Serializer.serialize(x) for x in obj]
            return "[" + ", ".join(items) + "]"


        if isinstance(obj, tuple):
            # Similar to lists, but with regular brackets
            items = [Serializer.serialize(x) for x in obj]
            return "(" + ", ".join(items) + ")"


        if isinstance(obj, str):
            # Put quotes around strings and handle special characters
            escaped = obj.replace("'", "\\'")  # Replace ' with \' to avoid breaking the string
            return f"'{escaped}'"


        if isinstance(obj, (int, float)):
            return str(obj)


        if isinstance(obj, bool):
            return str(obj)


        if obj is None:
            return "None"


        raise ValueError(f"Unsupported type: {type(obj)}")

    @staticmethod
    def deserialize(text: str) -> Any:
        """
        This function does the opposite of serialize - it takes a string and
        converts it back into Python objects. Like developing a photo back
        into the original scene.
        """
        text = text.strip()

        # Handle empty containers first
        if text in ["[]", "{}", "()"]:
            return {"[]": [], "{}": {}, "()": tuple()}[text]

        # Handle simple values
        if text == "None":
            return None
        if text == "True":
            return True
        if text == "False":
            return False

        # Handle strings (anything in quotes)
        if text.startswith("'") and text.endswith("'"):
            # Remove quotes and handle escaped characters
            content = text[1:-1]
            return content.replace("\\'", "'")

        # Handle numbers
        if text.replace(".", "").replace("-", "").isdigit():
            # Convert to float if there's a decimal point, otherwise integer
            return float(text) if "." in text else int(text)

        # Handle dictionaries
        if text.startswith("{") and text.endswith("}"):
            if not text[1:-1].strip():
                return {}
            # Split into key-value pairs and process each
            pairs = Serializer._split_items(text[1:-1])
            result = {}
            for pair in pairs:
                key, value = pair.split(":", 1)
                result[Serializer.deserialize(key)] = Serializer.deserialize(value)
            return result

        # Handle lists
        if text.startswith("[") and text.endswith("]"):
            if not text[1:-1].strip():
                return []
            # Split into items and process each
            items = Serializer._split_items(text[1:-1])
            return [Serializer.deserialize(item) for item in items]

        # Handle tuples
        if text.startswith("(") and text.endswith(")"):
            if not text[1:-1].strip():
                return tuple()
            # Similar to lists but return a tuple
            items = Serializer._split_items(text[1:-1])
            return tuple(Serializer.deserialize(item) for item in items)


        raise ValueError(f"Invalid format: {text}")

    @staticmethod
    def _split_items(text: str) -> list:
        """
        This helper function splits text into items while respecting nested structures.
        For example, splitting "1, [2, 3], 4" into ["1", "[2, 3]", "4"]
        """
        items = []
        current = ""
        # Keep track of nested levels
        depth = 0

        for char in text:
            if char in "[{(":
                depth += 1
            elif char in "]})":
                depth -= 1
            # Split only when we're at the top level
            elif char == "," and depth == 0:
                items.append(current.strip())
                current = ""
                continue
            current += char

        if current:
            items.append(current.strip())

        return items



if __name__ == "__main__":
    car1 = {
        "Capacit. motor": "N/A",
        "Tip combustibil": "Electricitate",
        "Anul fabricației": "2020",
        "Cutia de viteze": "Automată",
        "Marcă": "Mercedes",
        "Modelul": "EQC",
        "Tip tractiune": "4×4",
        "Distanță parcursă": "23 000 km",
        "Tip caroserie": "Crossover",
        "price": "1022950.0",
        "link": "https://sargutrans.md/cars/mercedes-eqc-2020/"
    }

    car = [[1, 2, 3], {'a': 1, 'b': 2}, (4, 5, 6), 'hello', 42, 3.14, True, False, None]

    cars = [car1, car]
    for car in cars:
        print("\n=== Simple Car Example ===")
        print("\nOriginal car data:")
        print(car)

        # Convert to string
        print("\nConverting to string...")
        car_string = Serializer.serialize(car)
        print("Serialized data:")
        print(car_string)

        # Convert back to object
        print("\nConverting back to Python object...")
        car_restored = Serializer.deserialize(car_string)
        print("Deserialized data:")
        print(car_restored)

        # Verify they match
        print("\nDo they match?", car == car_restored)