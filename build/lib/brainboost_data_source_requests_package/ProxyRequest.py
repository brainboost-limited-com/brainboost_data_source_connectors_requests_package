from .Request import Request
from .ProxyPool import ProxyPool
from .UserAgentPool import UserAgentPool
import re
import requests


import subprocess

class ProxyRequest(Request):
    def __init__(self, proxy=None):
        self.proxy_pool = ProxyPool()
        self._useragent_database = UserAgentPool()
        if proxy is None:
            proxy = self.proxy_pool.get_best_proxy()
        super().__init__(timeout=10, proxy=proxy, user_agent=self._useragent_database.get_random_user_agent())

    def get(self, page, data={}):
        return super().get(page=page, data=data)

    def post(self, page, data={}):
        return super().post(page=page, data=data)
    


    # Executes the current request instance and executes a plain requests method using the
    # wrapped requests framework
    def verify_sender_ip(self):
        try:
            response = requests.get('https://api.ipify.org', timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors           
            capped_ip_address = self.get_current_ip()
            print('The naked ip address is : ' + response.text + ' and the capped ip address is ' + capped_ip_address)
            print('The naked ip location is : ' + str(self.get_geolocation(another_ip=response.text)) + ' and the capped geolocation is ' + str(self.get_geolocation()))
            return response.text != capped_ip_address
        except requests.RequestException as e:
            print(f"Error using external service: {e}")
    

       