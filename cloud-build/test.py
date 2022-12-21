import requests
import json

city = "Indianapolis"
country = "US"

api_key = "aca82b561b9b05d6651612c4332fed2f"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

weather_data = weather_url.json()
