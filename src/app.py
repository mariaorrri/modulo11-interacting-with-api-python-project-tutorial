import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Pasos 4 y 5

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret,requests_session=True)
billie_uri = 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH'
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(billie_uri)
canciones = results['tracks']

for track in results['tracks'][:10]:
    print(f"Cancion   :  {track["name"]}")
    print(f"Popularidad: {track["popularity"]}") 
    print(f"Duracion: {track["duration_ms"]}")

# Paso 6
# Pasamos a dataframe solo los datos mas interesantes
df_canciones = pd.DataFrame([{
    'nombre': track['name'],
    'popularidad': track['popularity'],
    'duracion_ms': track['duration_ms'],
    'album': track['album']['name'],
    'id': track['id'],
    'url': track['external_urls']['spotify']
} for track in canciones])

df_canciones_ordenado = df_canciones.sort_values(by='popularidad', ascending=False)
top3 = df_canciones_ordenado.head(3)
print(top3)

# Paso 7
import matplotlib.pyplot as plt

x = df_canciones["popularidad"]
y = df_canciones["duracion_ms"]

plt.scatter(x, y,alpha=0.5)
plt.xlabel("Popularidad")
plt.ylabel("Duracion de la canción")
plt.title("popularidad vd duracion")
plt.show()