#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
import spotipy


client_id = "to_fill"
client_secret = "to_fill"
redirect_url = 'http://example.com'
scope = "playlist-modify-public"

date = input('Please enter the date: YYYY-MM-DD:')
r = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(r.text, 'html.parser')
titles = soup.select(
    selector="div.o-chart-results-list-row-container> ul > li:nth-child(4)>ul>li>h3")
songs = [i.text.strip() for i in titles]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_url,
        scope=scope))


playlist_name = f'{date} Billboard 100'

user_id = sp.current_user()['id']
playlist_id = sp.user_playlist_create(user_id, playlist_name)['id']
print("playlist_id", playlist_id)

year = date.split("-")[0]
uris = []
for song in songs:
    results = sp.search(q=f"track: {song} year: {year} ", type="track")
    try:
        uri = results['tracks']['items'][0]['uri']
        uris.append(uri)
    except IndexError:
        print('no matched musics')

print("uris", uris)

sp.playlist_add_items(playlist_id, uris)
