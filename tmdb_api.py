# Anderes Modul eventuell verwenden

import httpx
import pandas as pd
from config import TMDB_BEARER_TOKEN



url_discover_movies = "https://api.themoviedb.org/3/discover/movie"
headers = {"Authorization": f"Bearer {TMDB_BEARER_TOKEN}"}
params = {
    "sort_by": "popularity.desc", # Nach popularität sortiert
    "with_watch_providers": "8", # Netflix
    "watch_region": "DE" # Deutschland
}

response = httpx.get(url_discover_movies, headers=headers, params=params)
data = response.json()

print(data)

# In ein DataFrame umwandeln
print(response.text)