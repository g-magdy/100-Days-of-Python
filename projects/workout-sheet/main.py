import datetime, os, requests
from dotenv import load_dotenv
load_dotenv(override=True)
NOW = datetime.datetime.now()
TODAY = NOW.strftime("%d/%m/%Y")
NOW = NOW.strftime("%H:%M:%S")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
sheet = os.getenv("SHEET_ENDPOINT")

base_endpoint="https://trackapi.nutritionix.com"
plaintext = input("What are the exercises you did ? ")
head = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY
}
bearer = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
body = {
    "query":plaintext,
    "gender":"male",
    "weight_kg":"66",
    "height_cm": "171",
    "age": "20"
}
response = requests.post(
    url=f"{base_endpoint}/v2/natural/exercise",
    headers=head,
    json=body
)

response.raise_for_status()
exercises = response.json()["exercises"]
for exercise in exercises:
    row = {
        "sheet1": {
            "date": TODAY,
            "time": NOW,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    req = requests.post(url=sheet, headers=bearer, json=row)
    req.raise_for_status()