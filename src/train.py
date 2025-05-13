import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY = "Gomel"

response_city = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={CITY},BY&appid={API_KEY}")

lat = response_city.json()[0].get("lat")
lon = response_city.json()[0].get("lon")

response_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")

status_code = response_weather.status_code
result = response_weather.json()
print(status_code)
with open("weather.json", "w") as f:
    json.dump(result, f, indent=4)
print(f"Now in {CITY} temp= {round(result['main']['temp'] - 273)} degrees")
