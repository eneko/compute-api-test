import json, requests, urlparse
from settings import headers, host


class APIClient:

    def __init__(self):
        self.api_calls = 0

    def url(self, path):
        return urlparse.urljoin(host, path)

    def get(self, path):
        self.api_calls += 1
        return requests.get(self.url(path), headers=headers).json()
