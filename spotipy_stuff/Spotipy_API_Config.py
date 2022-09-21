import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID='65733477d5d145e990d262ea7854c537'
SPOTIPY_CLIENT_SECRET='739153f14e2940148da0340819b59512'


auth_manager = SpotifyClientCredentials(
  client_id = SPOTIPY_CLIENT_ID,
  client_secret = SPOTIPY_CLIENT_SECRET
)
spotipy_client = spotipy.Spotify(auth_manager=auth_manager)

