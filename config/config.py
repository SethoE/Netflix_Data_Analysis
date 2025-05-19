from dotenv import load_dotenv
import os

# Automatisch richtigen Pfad ermitteln
dotenv_path = os.path.join(os.path.dirname(__file__), "./secrets.env")
load_dotenv(dotenv_path)


# Zugriff auf die Tokens
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")