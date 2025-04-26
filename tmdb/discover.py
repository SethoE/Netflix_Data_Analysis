import httpx
from tmdb.tmdb_base import TMDbbase


class Discover(TMDbbase):
    DEFAULT_REGION = "DE"
    DEFAULT_SORT_BY = "popularity.desc"
    DEFAULT_PROVIDER_NETFLIX = "8"
    DEFAULT_PAGE = 1
    ENDPOINTS  = {
        "movie" : "/discover/movie",
        "tv": "/discover/tv"
    }

    def get_movies(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, provider_id=DEFAULT_PROVIDER_NETFLIX, page=DEFAULT_PAGE):
        """Discover movies from TMBb and use parameters to filter the result."""
        params = {
            "sort_by": sort_by,
            "with_watch_providers": provider_id,
            "watch_region": region,
            "page": page
        }
        return self.get_request(self.ENDPOINTS.get("movie"), params)

    def get_tv_shows(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, provider_id=DEFAULT_PROVIDER_NETFLIX, page=DEFAULT_PAGE):
        """Discover TV shows from TMBb and use parameters to filter the result."""
        params = {
            "sort_by": sort_by,
            "with_watch_providers": provider_id,
            "watch_region": region,
            "page": page
        }
        return self.get_request(self.ENDPOINTS.get("tv"), params)