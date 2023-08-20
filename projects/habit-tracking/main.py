import requests, datetime

# TODAY = str(datetime.date.today())
# TODAY = TODAY.replace("-", "")
# print(TODAY)
TODAY = datetime.datetime.now().strftime("%Y%m%d")
USERNAME = "g-magdy"
TOKEN = "dygfo847usdfv"
# --------------------------- CREATE ACCOUNT --------------------------- #
# info = {
#     "token": "dygfo847usdfv",
#     "username": "g-magdy",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url="https://pixe.la/v1/users", json=info)

# print(response.text)

# endpoint = "https://pixe.la/v1/users/g-magdy/graphs"

# --------------------------- CREATE GRAPH --------------------------- #
request_header = {
    "X-USER-TOKEN": TOKEN
}

# graph_config = {
#     "id": "g0",
#     "name": "coding-tracker",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora",
#     "timezone":"Africa/Cairo"
# }

# response = requests.post(url=endpoint, headers=request_header ,json=graph_config)
# print(response.text)

graph = "https://pixe.la/v1/users/g-magdy/graphs/g0"

data = {
    "date": TODAY,
    "quantity": "3.5"
}

# --------------------------- POST A PIXEL --------------------------- #
# response = requests.post(url=graph, headers=request_header, json=data)

# --------------------------- PUT --------------------------- #
data_update = {
    "quantity":"1.5"
}
response = requests.put(url=f"{graph}/{TODAY}", headers=request_header, json=data_update)

# --------------------------- DELETE A PIXEL --------------------------- #
response = requests.delete(url=f"{graph}/{TODAY}", headers=request_header)
print(response.text)
