
from tmdb.tmdb_base import TMDbbase
from typing import Literal
from enum import Enum, unique


@unique
class TimeWindow(Enum):
    DAY = "day"
    WEEK = "week"

class Trending(TMDbbase):



    ENDPOINTS  = {
        "movie" : "/trending/movie/week",
        "all": "/trending/all/{time_window}",
        "person": "/trending/person/{time_window}",
        "tv": "/trending/tv/{time_window}"
    }

    def get_trending_movies(self, time_window: TimeWindow = TimeWindow.WEEK) -> dict:
        """Trending movies from TMBb and use day or week to filter results."""
        endpunkt = self.resolve_endpoint(self.ENDPOINTS.get("movie"), time_window=time_window.value)
        return self.get_request(endpunkt)