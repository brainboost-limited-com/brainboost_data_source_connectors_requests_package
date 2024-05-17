import requests

from src.ProxyRequest import ProxyRequest

class TorRequest(ProxyRequest):

    def __init__(self):
        self.proxy = {
            'http': 'socks5://localhost:9050',
            'https': 'socks5://localhost:9050'
        }
        super().__init__(proxy=self.proxy)

    
    def get(self, page=None, data=None):
        try:
            response = super().get(page=page,data=data)
            return response  # Return JSON response if available
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
            return None
    
    def post(self, page=None, data=None):
        try:
            response = super().post(page=page, data=data)
            return response
        except requests.RequestException as e:
            print(f"Error during POST request: {e}")
            return None

