import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

stock_url = "https://www.alphavantage.co/query"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(stock_url, params=stock_parameters)
stock_data = response.json()

data = stock_data["Time Series (Daily)"]
data_list = [value for value in data.values()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_price = float(data_list[1]["4. close"])

difference = yesterday_closing_price - day_before_yesterday_price

percentage_change = (difference / day_before_yesterday_price) * 100

print(f"Stock change: {percentage_change:.2f}%")



NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

news_url = "https://newsapi.org/v2/everything"

news_parameters = {
    "q": STOCK_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "pageSize": 3
}

news_response = requests.get(news_url, params=news_parameters)
news_data = news_response.json()

articles = news_data["articles"][:3]


news_messages = []

for article in articles:
    headline = article["title"]
    description = article["description"]

    message = f"{headline}\n{description}"
    news_messages.append(message)



TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if percentage_change > 5 or percentage_change < -5:

    for news_message in news_messages:

        sms_body = f"{STOCK_NAME}: {percentage_change:.2f}%\n\n{news_message}"

        message = client.messages.create(
            body=sms_body,
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            to=os.environ.get("MY_PHONE_NUMBER")
        )

        print(message.status)