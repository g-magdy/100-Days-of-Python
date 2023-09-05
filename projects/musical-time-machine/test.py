import dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy, requests

config = dotenv.dotenv_values(dotenv_path=".env")

def main(config : dict):
    config = dotenv.dotenv_values(dotenv_path=".env")

    auth_manager = SpotifyOAuth(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"],
        username=config["USER_ID"],
        redirect_uri="https://example.com/",
        show_dialog=False,
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # print(sp.current_user()["id"]) #type: ignore
    tracks_uri = []

def get_auth_token(config : dict):
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


main(config=config)


    # url = f"https://api.spotify.com/v1/users/{config['USER_ID']}/playlists"
    # head = {
    #     "Authorization": f"Bearer {get_auth_token(config)}",
    #     'Content-Type': 'application/json',
    # }
    # body = {
    #     "name": "Python Playlist",
    #     "description": "I hope this works",
    #     "public": False
    # }
    # response = requests.post(
    #     url=url,
    #     headers= head,
    #     params=body
    # )
    # response.raise_for_status()
    # print(response.text)