import requests

from app.clients.base import BaseClient

class HttpbinClient(BaseClient):
    def __init__(self, url: str):
        self.url = url

    def generate_uuid(self):
        response = requests.get(f"{self.url}/uuid")

        return response.json()["uuid"]

