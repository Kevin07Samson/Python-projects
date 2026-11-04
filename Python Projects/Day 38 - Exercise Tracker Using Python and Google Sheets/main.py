import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
NUTRITION_URL = os.environ["NUTRITION_URL"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 178
AGE = 20

# Nutrition API

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    url=NUTRITION_URL,
    headers=headers,
    json=data
)

result = response.json()

# Sheety

sheet_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:

    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=sheet_headers
    )

    print(sheet_response.status_code)
    print(sheet_response.text)