import os

from flask import jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import json

load_dotenv()


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv('client_id'),
                                                           client_secret=os.getenv('client_secret')))

print(json.dumps(sp.audio_features(tracks=["https://open.spotify.com/track/751srcHf5tUqcEa9pRCQwP?si=76e9d56e64a34cc6"])))