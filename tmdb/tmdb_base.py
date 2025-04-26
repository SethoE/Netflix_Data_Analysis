import httpx

class TMDbbase:
    DEFAULT_API_VERSION = "v3"
    BASE_URL = {
        "v3": "https://api.themoviedb.org/3",
        "v4": "https://api.themoviedb.org/4"
    }

    @staticmethod
    def resolve_endpoint(template: str, **kwargs) -> str:
        return template.format(**kwargs)

    def __init__(self, bearer_token: str):
        self.bearer_token = bearer_token if isinstance(bearer_token, str) else ""
        self.client = httpx.Client(
            headers={
                "Authorization": f"Bearer {self.bearer_token}",
                "accept": "application/json"
            }
        )

    def get_request(self, endpoint: str, params: dict = None, api_version: str = DEFAULT_API_VERSION) -> dict:
        """Creates a get request and returns JSON response if status code is 200"""
        url = f"{self.BASE_URL.get(api_version)}{endpoint}"
        response = self.client.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Fehler {response.status_code}: {response.text}")
            return {}

    def close(self):
        """Close client"""
        self.client.close()