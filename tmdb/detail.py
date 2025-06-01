import httpx
from tmdb.tmdb_base import TMDbbase
import time
import json

class Detail(TMDbbase):

    ENDPOINTS = {
        "movie_details": "/movie/{movie_id}",
        "movie_providers": "/movie/{movie_id}/watch/providers",
        "tv_details": "/tv/{series_id}"
    }

    def safe_get_movie_details(
            self,
            movie_id: int,
            retries: int = 3,
            delay: float = 0.2,
            backoff_factor: float = 2.0
    ) -> dict:
        """
        Versucht get_movie_details(movie_id) bis zu `retries` Mal,
        mit exponentiellem Backoff bei Netzwerk- oder JSON-Fehlern.
        """
        current_delay = delay

        for attempt in range(1, retries + 1):
            try:
                response = self.get_movie_details(movie_id)

                # Optional: Wenn dein Wrapper bei HTTP-Fehlern nicht schon eine Exception wirft,
                # könntest du hier noch prüfen:
                # if response.get("status_code", 200) >= 400:
                #     raise httpx.HTTPError(f"HTTP {response['status_code']}")

                # Wir gehen davon aus, dass response bereits ein dict ist
                return response

            except httpx.HTTPError as e:
                # Netzwerk- oder HTTP-Fehler (Timeout, 5xx, 4xx etc.)
                print(f"[WARN] HTTPError für ID {movie_id} ({attempt}/{retries}): {e}")
            except json.JSONDecodeError as e:
                # JSON nicht parsebar
                print(f"[WARN] JSONDecodeError für ID {movie_id} ({attempt}/{retries}): {e}")
            except KeyError as e:
                # Falls später in deinen Detail-Daten ein Key fehlt
                print(f"[WARN] KeyError für ID {movie_id} ({attempt}/{retries}): {e}")
            except Exception as e:
                # Alles andere – wirklich nur als „letzten Ausweg“, um nicht abzubrechen
                print(f"[WARN] Unerwarteter Fehler für ID {movie_id} ({attempt}/{retries}): {e}")

            # Wenn wir hier landen, war ein Fehler. Und wir haben noch Versuche übrig:
            if attempt < retries:
                wait = current_delay
                print(f"    Warte {wait:.2f}s vor dem nächsten Versuch …")
                time.sleep(wait)
                current_delay *= backoff_factor
            else:
                print(f"[ERROR] Alle {retries} Versuche für ID {movie_id} sind fehlgeschlagen.")
                return {}

        # Eigentlich nie erreicht, aber für die Syntax
        return {}
    def get_movie_details(self, movie_id: int) -> dict:
        """Get the details of a specific movie using the movie id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("movie_details"), movie_id=movie_id))

    def get_movie_providers(self, movie_id) -> dict:
        """Get the providers of a specific movie using the movie id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("movie_providers"), movie_id=movie_id))

    def get_tv_details(self, series_id: int) -> dict:
        """Get the details of a specific TV show using the TV show id."""
        return self.get_request(self.resolve_endpoint(self.ENDPOINTS.get("tv_details"), series_id=series_id))