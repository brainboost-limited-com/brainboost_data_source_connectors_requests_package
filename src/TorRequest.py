import requests
from src.ProxyRequest import ProxyRequest

class TorRequest(ProxyRequest):

    def __init__(self):

        self.proxy = {"ip": "127.0.0.1", "port": 9050}
    
    def get(self, page, data=None):
        try:
            response = requests.get(page, params=data, proxies=self.proxy)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses
            return response.json()  # Return JSON response if available
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
            return None
    
    def post(self, page, data=None):
        try:
            response = requests.post(page, params=data, proxies=self.proxy)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses
            return response.json()  # Return JSON response if available
        except requests.RequestException as e:
            print(f"Error during POST request: {e}")
            return None

