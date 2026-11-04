import requests
from twilio.rest import Client

api_key = "YOUR_OPENWEATHER_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

parameters = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to rain today. Remember to take your Umbrella!☔️",
        from_="YOUR_TWILIO_PHONE_NUMBER",
        to="YOUR_VERIFIED_PHONE_NUMBER",
    )

    print(message.sid)