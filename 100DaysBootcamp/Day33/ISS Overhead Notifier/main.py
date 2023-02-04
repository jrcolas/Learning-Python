import requests
from datetime import datetime
import math
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/colasf/Coding/ENVs/.env")
MY_LAT = 25.761681 # Your latitude
MY_LONG = -80.191788 # Your longitude
USERNAME = os.getenv("EMAIL")
PASSWORD = os.getenv("E_PASSWORD")

# MY_LAT = -39.761681 # Your test latitude
# MY_LONG = 67.191788 # Your test longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 5

time_now = datetime.now()


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
print(f"({iss_latitude}, {iss_longitude})")
print(f"time in hour:{time_now.hour}")
print(sunrise)
print(sunset)

while True:
    time.sleep(60)
    if math.isclose(iss_latitude, MY_LAT, abs_tol=5) and math.isclose(iss_longitude, MY_LONG, abs_tol=5):
        if 7 > time_now.hour >= 18:
            print("Look outside bruh")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=USERNAME, password=PASSWORD)
                connection.sendmail(
                    from_addr=USERNAME,
                    to_addrs=USERNAME,
                    msg="Subject: Look outside bruh!\n\nThe ISS is up there. You can actually see it right now if you run."
                )
        else:
            pass
    else:
        print("It dont be close")

