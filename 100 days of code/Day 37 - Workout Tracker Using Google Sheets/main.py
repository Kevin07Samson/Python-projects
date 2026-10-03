import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = "hilarius17"
TOKEN = os.getenv("PIXELA_TOKEN")
print("Token loaded:",TOKEN is not None)
GRAPH_ID = "gym-streak"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Streak",
    "unit": "day",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Kolkata",
    "description": "Number of days I went to the gym",
    "startOnMonday": True
}

headers = {
    "X-USER-TOKEN":TOKEN
}
#response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Did you go to the gym today? Enter 1 for Yes, 0 for No: "),
}

#response = requests.post(url=pixela_creation_endpoint,json=pixel_data,headers=headers)
#print(response.text)

update_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"

}
#response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
#print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)