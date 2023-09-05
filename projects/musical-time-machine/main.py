import dotenv, spotipy, requests, pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


def main():
    config = dotenv.dotenv_values(dotenv_path=".env")
    print("Welcome to the musical time machine")
    date = input("Which date do you want to travel to ?\nType the date in the format of YYYY-MM-DD\n")

    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
    response.raise_for_status()
    soup = BeautifulSoup(markup=response.text, features="html.parser")
    tracks = soup.select(selector="ul li ul li h3")
    tracks = [(h3.text).strip() for h3 in tracks]    


    config = dotenv.dotenv_values(dotenv_path=".env")

    auth_manager = SpotifyOAuth(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"],
        username=config["USER_ID"],
        redirect_uri="https://example.com/",
        show_dialog=False,
        scope='playlist-modify-private'
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # print(sp.current_user()["id"]) #type: ignore
    tracks_uri = []
    year = date[0:4]
    for track in tracks:
        s = sp.search(
            q=f"track:{track} year:{year}",
            limit=1,
            type="track"
        )
        try:
            tracks_uri.append(str(s['tracks']['items'][0]['uri'])) #type: ignore
        except IndexError:
            continue
            
    mylist = sp.user_playlist_create(user=config["USER_ID"],name=f"{date} billboard 100", public=False, description="created by spotipy", collaborative=False)
    sp.playlist_add_items(playlist_id=mylist["id"], items=tracks_uri) #type: ignore
        
main()