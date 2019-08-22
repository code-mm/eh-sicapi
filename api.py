import requests
from enum import Enum
import json

http_method = Enum('method', 'get post put patch delete')

class Api:
    def __init__(self, apikey):
        self.url = 'https://api-demo.single-invoice.co/v2/'
        self.apikey = apikey

    def _get_headers(self):
        return {
            'apikey': self.apikey,
            'cache-control': "no-cache",
        }

    def request(self, method, path, data_body=None, parameter=None):
        if method is http_method.get:
            return requests.get(self.url+path, headers=self._get_headers(), params=parameter).json()
        elif method is http_method.post:
            return requests.post(self.url+path, headers=self._get_headers(), data=data_body, params=parameter).json()
        elif method is http_method.put:
            return requests.put(self.url+path, headers=self._get_headers(), data=data_body, params=parameter).json()
        elif method is http_method.patch:
            return requests.patch(self.url+path, headers=self._get_headers(), data=data_body, params=parameter).json()
        elif method is http_method.delete:
            return requests.delete(self.url+path, headers=self._get_headers()).json()
        else:
            return None
