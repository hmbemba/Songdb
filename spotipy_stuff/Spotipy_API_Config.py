import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
load_dotenv()




auth_manager = SpotifyClientCredentials(
  client_id = os.environ['SPOTIPY_CLIENT_ID'],
  client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
)
spotipy_client = spotipy.Spotify(auth_manager=auth_manager)

