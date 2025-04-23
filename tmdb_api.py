# Anderes Modul eventuell verwenden
import requests
import pandas as pd
from config import TMDB_BEARER_TOKEN

url = "https://api.themoviedb.org/3/configuration"
url_rated_tv = "https://api.themoviedb.org/3/guest_session/guest_session_id/rated/tv?language=en-US&page=1&sort_by=created_at.asc"
url_movies = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_BEARER_TOKEN}"
}

# response = requests.get(url, headers=headers)
response = requests.get(url_movies, headers=headers)
data = response.json()

movies = data.get("results", [])

# In ein DataFrame umwandeln
if movies:
    df = pd.DataFrame(movies)

    # Nur bestimmte Spalten zur Übersicht auswählen
    df_view = df[["title", "release_date", "vote_average", "vote_count"]]

    # Tabelle anzeigen
    from IPython.display import display
    display(df_view.head(10))
else:
    print("Keine Filme gefunden oder Antwort ungültig.")
print(response.text)