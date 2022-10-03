from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
<<<<<<< HEAD
from dotenv import load_dotenv
import os
load_dotenv()



=======
import os
from dotenv import load_dotenv

load_dotenv() 
>>>>>>> 947e9df3c0ab06b2d9b2a8c7e511058eddb0d61a

auth_manager = SpotifyClientCredentials(
  client_id = os.environ['SPOTIPY_CLIENT_ID'],
  client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
)
spotipy_client = spotipy.Spotify(auth_manager=auth_manager)

