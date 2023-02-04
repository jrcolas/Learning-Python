import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv("C:/Users/colasf/Coding/ENVs/.env")
api_key = os.getenv("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

weather_params = {
    "lat": 17.987490,
    "lon": -92.919701,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Raining through them ENVs',
        from_=os.getenv("TWILIO_PHONE"),
        to=os.getenv("PHONE")
    )

    print(message.status)


# print(data["hourly"][0]["weather"][0]["id"])
