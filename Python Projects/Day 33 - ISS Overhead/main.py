import requests
import smtplib
import time
from datetime import datetime
from zoneinfo import ZoneInfo

MY_LAT = 13.059031
MY_LONG = 80.232605

MY_EMAIL = "kevin07samson@gmail.com"
MY_PASSWORD = "ynguzssrlgahsjov"


def check_iss_position():

    response = requests.get(
        url="http://api.open-notify.org/iss-now.json"
    )
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True

    return False


def check_if_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()

    data = response.json()

    sunrise = datetime.fromisoformat(
        data["results"]["sunrise"]
    ).astimezone(ZoneInfo("Asia/Kolkata"))

    sunset = datetime.fromisoformat(
        data["results"]["sunset"]
    ).astimezone(ZoneInfo("Asia/Kolkata"))

    time_now = datetime.now(ZoneInfo("Asia/Kolkata"))

    if time_now.hour >= sunset.hour or time_now.hour < sunrise.hour:
        return True

    return False


while True:

    if check_iss_position() and check_if_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(
                user=MY_EMAIL,
                password=MY_PASSWORD
            )

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS Overhead 🚀\n\nLook up! The International Space Station is overhead!"
            )

    time.sleep(60)