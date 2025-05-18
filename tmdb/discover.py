import httpx
from tmdb.tmdb_base import TMDbbase
import time


class Discover(TMDbbase):
    DEFAULT_REGION = "DE"
    DEFAULT_SORT_BY = "popularity.desc"
    DEFAULT_PROVIDER_NETFLIX = "8"
    DEFAULT_PAGE = 1
    ENDPOINTS  = {
        "movie" : "/discover/movie",
        "tv": "/discover/tv"
    }

    def get_movies(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, provider_id=DEFAULT_PROVIDER_NETFLIX, page=DEFAULT_PAGE, **kwargs) -> dict:
        """Discover movies from TMBb and use parameters to filter the result."""
        params = {
            "sort_by": sort_by,
            "with_watch_providers": provider_id,
            "watch_region": region,
            "page": page
        }
        if "params" in kwargs:
            params.update(kwargs["params"])

        return self.get_request(self.ENDPOINTS.get("movie"), params)

    def get_tv_shows(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, provider_id=DEFAULT_PROVIDER_NETFLIX, page=DEFAULT_PAGE, **kwargs) -> dict:
        """Discover TV shows from TMBb and use parameters to filter the result."""
        params = {
            "sort_by": sort_by,
            "with_watch_providers": provider_id,
            "watch_region": region,
            "page": page
        }
        params.update(kwargs)
        return self.get_request(self.ENDPOINTS.get("tv"), params)

    # Idee: Respektiere TMDb-Ratenlimits durch Einfügen von Wartezeiten und einfachem Retry bei Fehler 429


    # Neue Funktion mit automatischem Delay und Retry bei Rate Limit
    def safe_get_movies(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, provider_id=DEFAULT_PROVIDER_NETFLIX, retries=3, delay=0.2, page=DEFAULT_PAGE, **kwargs):
        params = {
            "sort_by": sort_by,
            "with_watch_providers": provider_id,
            "watch_region": region,
            "page": page
        }
        if "params" in kwargs:
            params.update(kwargs["params"])

        for attempt in range(retries):
            response = self.get_request(self.ENDPOINTS.get("movie"), params)
            if response != {}:
                time.sleep(delay)  # Respect rate limits
                return response
            print(f"Retrying ({attempt + 1}/{retries}) for {region} - Page {page}...")
            time.sleep(2)
            print(f"[WARN] Abbruch nach {retries} Fehlversuchen für {region} Page {page}")
            return {}
        return {}