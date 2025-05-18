import httpx
from tmdb.tmdb_base import TMDbbase

class Configuration(TMDbbase):
    ENDPOINTS = {
        "countries": "/configuration/countries",
        "languages": "/configuration/languages"
    }
    def get_countries(self) -> dict:
        return self.get_request(self.ENDPOINTS.get("countries"))

    def get_language(self) -> dict:
        return self.get_request(self.ENDPOINTS.get("language"))