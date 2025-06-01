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
    def safe_get_movies(self, region=DEFAULT_REGION, sort_by=DEFAULT_SORT_BY, with_watch_providers=DEFAULT_PROVIDER_NETFLIX, retries=3,
            delay=0.2,
            backoff_factor=2.0,
            page=DEFAULT_PAGE,
            **kwargs
    ):
        """
        Holt sequenziell die Discover-/Movies-Liste (TMDb) und versucht bei leeren Responses
        bis zu 'retries'-mal, mit einem exponentiellen Backoff.
        """
        params = dict(sort_by=sort_by, with_watch_providers=with_watch_providers, watch_region=region, page=page)
        if "params" in kwargs:
            params.update(kwargs["params"])

        current_delay = delay
        for attempt in range(1, retries + 1):
            response = self.get_request(self.ENDPOINTS.get("movie"), params)

            # Wenn wir ein valides Ergebnis haben (nicht {}), geben wir es zurück
            if response and response != {}:
                # kurz pausieren, um sicher unter TMDb-Limit zu bleiben
                time.sleep(delay)
                return response

            # Hier sind wir also auf einen „leeren“ oder fehlgeschlagenen Response gestoßen
            if attempt < retries:
                print(f"[WARN] Versuch {attempt}/{retries} für {region} Page {page} fehlgeschlagen. "
                      f"Sleep {current_delay:.2f}s und neuer Versuch...")
                time.sleep(current_delay)
                # Exponential Backoff (um beim nächsten Mal etwas länger zu warten)
                current_delay *= backoff_factor
            else:
                # Letzter Versuch war auch erfolglos → breche endgültig ab
                print(f"[ERROR] Alle {retries} Versuche für {region} Page {page} sind fehlgeschlagen.")
                return {}

        # Sicherheitshalber, sollte nie erreicht werden:
        return {}