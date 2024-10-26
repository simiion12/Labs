import requests
from config import API_KEY

# Simple XML request
url = f"http://api.weatherapi.com/v1/astronomy.xml"  # Note the .xml extension
params = {'key': API_KEY, 'q': 'Paris', 'dt': '2024-10-25'}
response = requests.get(url, params=params)
print(response.text)  # This will print the XML response
