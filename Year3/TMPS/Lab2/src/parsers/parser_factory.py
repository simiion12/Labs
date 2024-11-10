from Year3.TMPS.Lab2.src.parsers.parsers import JsonWeatherDataParser, XmlWeatherDataParser

class WeatherParserFactory:
    _parsers = {
        'json': JsonWeatherDataParser,
        'xml': XmlWeatherDataParser
    }

    @staticmethod
    def get_parser(parser_type: str):
        parser = WeatherParserFactory._parsers.get(parser_type.lower())
        if not parser:
            raise ValueError(f"Invalid parser type: {parser_type}")
        return parser()
