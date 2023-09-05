import requests, dotenv
def get_auth_token():
    config = dotenv.dotenv_values(dotenv_path=".env")
    response = requests.post(
        url="https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type":"client_credentials",
            "client_id":config["CLIENT_ID"],
            "client_secret":config["CLIENT_SECRET"]
        }
    )
    return response.json()["access_token"]