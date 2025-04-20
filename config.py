from dotenv import load_dotenv
import os

# .env-Datei laden
load_dotenv("./secrets.env")

# Zugriff auf die Tokens
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")

print(TMDB_API_KEY)
print(TMDB_BEARER_TOKEN)