import requests
import json
import os
from dotenv import load_dotenv
from unittest.mock import patch


load_dotenv()
CITY = "Gomel"

API_KEY = os.getenv("API_KEY")


def get_coords(city):
    response_city = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},BY&appid={API_KEY}")

    lat = response_city.json()[0].get("lat")
    lon = response_city.json()[0].get("lon")
    return lat, lon


def get_weather(lat: float, lon: float):

    response_weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    status_code = response_weather.status_code
    result = response_weather.json()
    print(status_code)
    with open("weather.json", "w") as f:
        json.dump(result, f, indent=4)
    return f"Now in {CITY} temp= {round(result['main']['temp'] - 273)} degrees"


@patch('requests.get')
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 298}}
    assert get_weather(1, 1) == f"Now in {CITY} temp= {298 - 273} degrees"
    mock_get.assert_called_once_with(f'https://api.openweathermap.org/data/2.5/weather?lat=1&lon=1&appid={API_KEY}')


if __name__ == "__main__":
    lat, lon = get_coords(CITY)
    print(get_weather(lat, lon))
