# Importing modules
from bs4 import BeautifulSoup
import requests
import lxml
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Asking the user what date they would like to go back too
date_input = input("What time would you like to go back to? YYYY-MM-DD: ")

# Setting constants
URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")


# Retrieving the html in a text format from the url
response = requests.get(url=f"{URL}{date_input}/")
website_html = response.text

# Using soup to change the text into html format
soup = BeautifulSoup(website_html, "lxml")

# Finding the song titles
song_titles_un_formatted = soup.select(selector="li ul li h3")
song_titles = [song.getText().replace("\n", "").replace("\t", "") for song in song_titles_un_formatted]

# Using spotipy to authorise me to access data on spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=SPOTIPY_REDIRECT_URI,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"))

user_id = sp.current_user()["id"]

# Getting all the songs URI's and putting them into a list
song_uris = []
year = date_input.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Making a playlist with all the songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
