import httpx
from tmdb_base import TMDbbase

class Genre(TMDbbase):

    ENDPOINTS = {
        "movie": "/genre/movie/list",
        "tv": "/genre/tv/list"
    }

    def get_movie(self) -> dict:
        """Get all the genres available for movies"""
        return self.get_request(self.ENDPOINTS.get("movie"))

    def get_tv(self) -> dict:
        """Get all the genres available for TV"""
        return self.get_request(self.ENDPOINTS.get("tv"))