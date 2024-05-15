import requests
import Request

class RequestProxy(Request):
    def __init__(self, proxy=None):
        self.proxy = proxy
    
    def get(self, url, params=None):
        try:
            response = requests.get(url, params=params, proxies=self.proxy)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses
            return response.json()  # Return JSON response if available
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
            return None
    
    def post(self, url, data=None):
        try:
            response = requests.post(url, data=data, proxies=self.proxy)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses
            return response.json()  # Return JSON response if available
        except requests.RequestException as e:
            print(f"Error during POST request: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Create a RequestProxy instance without a proxy
    proxy = RequestProxy()
    
    # Example GET request
    get_url = "https://api.whatismyip.com/data"
    get_params = {"key": "value"}
    get_response = proxy.get(get_url, params=get_params)
    if get_response:
        print("GET Response:", get_response)
    
    # Example POST request
    post_url = "https://api.whatismyip.com/submit"
    post_data = {"name": "John", "age": 30}
    post_response = proxy.post(post_url, data=post_data)
    if post_response:
        print("POST Response:", post_response)
