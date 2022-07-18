import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

##### BILLBOARD MUSIC LIST CREATION #########
date = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, "html.parser")
song_name_spans = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in song_name_spans]

##### SPOTIFY MUSIC LIST CREATION #########

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="b7f8c711847440a6b0ccb0c0ed2d6edd",
        client_secret="a70c303d6de340729eff356c121156ac",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
new_playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
playlist_id = new_playlist["id"]

track_uris = []
year = date.split("-")[0]

for song in song_names:
    try:
        track_id = sp.search(q=f"track:{song} year:{year}", type="track")['tracks']['items']
        if track_id[0]['type'] == 'track':
            track_uris.append(track_id[0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)


