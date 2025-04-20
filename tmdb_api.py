import requests
from config import TMDB_BEARER_TOKEN

url = "https://api.themoviedb.org/3/configuration"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_BEARER_TOKEN}"
}

response = requests.get(url, headers=headers)

print(response.text)