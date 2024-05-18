import requests
from collections import namedtuple
from . import utils as utl
from src.brainboost_data_source_requests_package.UserAgentPool import UserAgentPool

class Request(object):
    '''Performs HTTP requests. A `requests` wrapper, essentialy'''
    def __init__(self, timeout=10, proxy=None, user_agent='random'):
        self._useragent_database = UserAgentPool()
        self.session = requests.session()

        if proxy:
            self.session.proxies = {
                'http': f'socks5h://{proxy["ip"]}:{proxy["port"]}',
                'https': f'socks5h://{proxy["ip"]}:{proxy["port"]}'
            }

        if user_agent == 'random':
            self.session.headers['User-Agent'] = self._useragent_database.get_random_user_agent()
        else:
            self.session.headers['User-Agent'] = user_agent
        self.session.headers['Accept-Language'] = 'en-GB,en;q=0.5'
        self.timeout = timeout
        self.response = namedtuple('response', ['http', 'html'])
        self.my_ip = None

    def get(self, page, data):
        '''Submits a HTTP GET request.'''
        page = self._quote(page)
        try:
            req = self.session.get(url=page, data=data, timeout=self.timeout)
            self.session.headers['Referer'] = page
        except requests.exceptions.RequestException as e:
            return self.response(http=0, html=e.__doc__)
        return self.response(http=req.status_code, html=req.text)

    def post(self, page, data):
        '''Submits a HTTP POST request.'''
        page = self._quote(page)
        try:
            req = self.session.post(url=page, data=data, timeout=self.timeout)
            self.session.headers['Referer'] = page
        except requests.exceptions.RequestException as e:
            return self.response(http=0, html=e.__doc__)
        return self.response(http=req.status_code, html=req.text)

    def _quote(self, url):
        '''URL-encodes URLs.'''
        if utl.decode_bytes(utl.unquote_url(url)) == utl.decode_bytes(url):
            url = utl.quote_url(url)
        return url

    def get_current_ip(self):
        if self.my_ip is None:
            try:
                # Use ipify service to get the current IP address
                response = self.session.get('https://api.ipify.org')
                response.raise_for_status()  # Raise an exception for HTTP errors
                self.my_ip = response.text
                return self.my_ip
            except requests.exceptions.RequestException as e:
                return f"Error: {str(e)}"
        else:
            return self.my_ip

    def get_geolocation(self):
        ip_address = self.get_current_ip()
        url = f"http://ip-api.com/json/{ip_address}"
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            if data['status'] == 'success':
                location = {
                    'IP Address': ip_address,
                    'Country': data.get('country', 'N/A'),
                    'Region': data.get('regionName', 'N/A'),
                    'City': data.get('city', 'N/A'),
                    'Latitude': data.get('lat', 'N/A'),
                    'Longitude': data.get('lon', 'N/A'),
                    'ISP': data.get('isp', 'N/A'),
                    'Organization': data.get('org', 'N/A')
                }
            else:
                location = {'Error': data.get('message', 'Unknown error')}

            return location

        except requests.exceptions.RequestException as e:
            return {'Error': str(e)}
