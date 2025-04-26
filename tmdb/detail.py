import httpx
from tmdb_base import TMDbbase

class Detail(TMDbbase):

    ENDPOINTS = {
        "movie_details": "/movie/{movie_id}",
        "movie_providers": "/movie/{movie_id}/watch/providers",
        "tv_details": "/tv/{series_id}"
    }

    def get_movie_details(self, movie_id: int) -> dict:
        """Get the details of a specific movie using the movie id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("movie_details"), movie_id=movie_id))

    def get_movie_providers(self, movie_id) -> dict:
        """Get the providers of a specific movie using the movie id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("movie_providers"), movie_id=movie_id))

    def get_tv_details(self, series_id: int) -> dict:
        """Get the details of a specific TV show using the TV show id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("tv_details"), series_id=series_id))