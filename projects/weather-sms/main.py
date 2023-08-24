import os, requests
from twilio.rest import Client
# --------------------Getting Weather data --------------------#
url="https://api.openweathermap.org/data/2.5/weather"

# -------------------- ENVIRONMENT VARIABLES --------------------#
OWM_APPID = os.environ.get("OWM_APPID")
ACC_SID = os.environ.get("ACC_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
SENDER = os.environ.get("SENDER")
RECEIVER= os.environ.get("RECEIVER")

params = {
    "lat": 30.0444,
    "lon": 31.2357,
    "appid": OWM_APPID
}

response = requests.get(url, params=params).json()
description = response["weather"][0]["description"]
temp = round(response["main"]["temp"] - 273)

message = f"Weather report for {response['name']}: {description}\nTemp = {temp} deg.C"

# -------------------- sending the message --------------------#

client = Client(ACC_SID, AUTH_TOKEN)
message = client.messages.create(
    from_=SENDER,
    to=RECEIVER, #type: ignore
    body=message
)
print(message.status)