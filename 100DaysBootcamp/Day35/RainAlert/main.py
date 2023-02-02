import requests

api_key = "f5912a48d4773b4c4065704428c281af"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": 25.761681,
    "lon": -80.191788,
    "appid": api_key,
}

url = "https://api.openweathermap.org/data/3.0/onecall?lat=25.761681&lon=-80.191788&appid=806c516ce240b6fb47652ca601cbb1d4"

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
print(data)
