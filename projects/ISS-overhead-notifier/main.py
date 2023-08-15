import requests
from datetime import datetime
import smtplib, time
time_now = datetime.now()

MY_LAT = 30.044477 # Your latitude
MY_LONG = 31.235659 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def ISS_is_above() -> bool:
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

def is_dark() -> bool:
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True
    else:
        return False

if is_dark() and ISS_is_above():
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(user="tom864849@gmail.com", password="zubfgvbtxwsalkys")
    server.sendmail(
        from_addr="tom864849@gmail.com",
        to_addrs="tom864849@gmail.com",
        msg="Subject:ISS is above you\n\nLook UP"
    )