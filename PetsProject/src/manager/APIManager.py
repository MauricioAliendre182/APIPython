import requests
import json
from requests import Response, Session


class APIManager:
    _self = None

    # session = Session()
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.url = "https://petstore.swagger.io/v2"

    def get(self, endpoint: str, headers: dict) -> Response:
        return requests.get(
            url=self.url + endpoint,
            headers=headers
        )

    def post(self, endpoint: str, headers: dict, payload: object) -> Response:
        return requests.post(
            url=self.url + endpoint,
            headers=headers,
            data=json.dumps(payload, indent=4)
        )

    def post1(self, endpoint: str, headers: dict, payload: str) -> Response:
        return requests.post(
            url=self.url + endpoint,
            headers=headers,
            data=payload
        )

    def put(self, endpoint: str, headers: dict, payload: object) -> Response:
        return requests.put(
            url=self.url + endpoint,
            headers=headers,
            data=json.dumps(payload, indent=4)
        )

    def delete(self, endpoint: str, headers: dict) -> Response:
        return requests.delete(
            url=self.url + endpoint,
            headers=headers
        )

