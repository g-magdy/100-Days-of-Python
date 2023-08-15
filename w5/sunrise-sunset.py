import datetime, requests, json

my_lat = 30.044477
my_lng = 31.235659
time_now = datetime.datetime.now()
params = {
    "lat":my_lat, 
    "lng":my_lng,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
data = response.json()
# print(json.dumps(data , indent=4))
sunrise = data["results"]["sunrise"].split('T')[1]
sunset = data["results"]["sunset"].split('T')[1]
sunrise_h = sunrise[0:2]
sunrise_m = sunrise[3:5]
sunset_h = sunset[0:2]
sunset_m = sunset[3:5]
print(f"sunrise : {sunrise_h}:{sunrise_m}")
print(f"sunset : {sunset_h}:{sunset_m}")
print(f"now : {time_now.hour}:{time_now.minute}")