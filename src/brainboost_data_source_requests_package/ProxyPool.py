
import random
import requests

from tinydb import Query, TinyDB
import time


class ProxyPool:
    '''Manages a pool of proxies for HTTP requests.'''
    def __init__(self,proxy_source_url=None,proxy_db=None):
        if proxy_db == None:
            self.proxies_db = TinyDB('src/brainboost_data_source_requests_package/resources/proxies_db.json')
        else:
            self.proxies_db = TinyDB(proxy_db)
        self.current_proxy = None
        if proxy_source_url == None:
            self.proxy_source_urls = ['https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.json']
        self.download_and_update_proxies()

    def download_and_update_proxies(self,more_proxies_json=None):
        timestamp = int(time.time())
        if (timestamp // 60) % 20 == 0:
            try:
                if (more_proxies_json==None):
                    response = requests.get(self.proxy_source_urls[0])
                else:
                    self.proxy_source_urls.push(more_proxies_json)
                    response = requests.get(self.proxy_source_urls[-1])

                response.raise_for_status()
                proxies_data = response.json()

                for proxy in proxies_data:
                    # Assuming proxy structure in JSON: {"ip": "192.168.1.1", "port": "8080"}

                    self.insert_proxy_if_not_exists(proxy)

            except requests.RequestException as e:
                print(f"Error downloading or parsing JSON data: {e}")



    def insert_proxy_if_not_exists(self, proxy):
        Proxy = Query()
        existing_proxy = self.proxies_db.search(
            (Proxy.ip == proxy['ip']) & (Proxy.port == proxy['port'])
        )
        
        proxy['request_time'] = self.test_proxy(proxy=proxy)
        if not existing_proxy:            
            self.proxies_db.insert(proxy)
            print(f"Inserted proxy: {proxy}")
        else:
            self.proxies_db.update({'time_request': proxy['request_time']}, Proxy.ip == proxy['ip'] and Proxy.port == proxy['port'])
            print(f"Proxy already exists: {proxy}, updating request time {proxy['request_time']}")



    def get_random_proxy(self):
        # Retrieve all proxies from the database
        proxies = self.proxies_db.all()

        if not proxies:
            # If no proxies are available, return None
            return None
        
        # Select a random proxy from the list of proxies
        random_proxy = random.choice(proxies)

        # Extract the proxy information (assuming a dictionary structure)
        proxy_ip = random_proxy.get('ip')
        proxy_port = random_proxy.get('port')
        proxy_protocol = random_proxy.get('protocol')

        # Construct the proxy URL based on protocol, IP, and port
        proxy_url = f"{proxy_protocol}://{proxy_ip}:{proxy_port}"

        # Set the current_proxy attribute to the selected proxy
        self.current_proxy = proxy_url

        return proxy_url


    def get_best_proxy(self):
        if len(self.proxies_db) == 0:
            print("No proxies available in the database.")
            return None

        # Get all proxies from the database
        all_proxies = self.proxies_db.all()

        # Find the proxy with the minimum response time
        best_proxy = min(all_proxies, key=lambda p: p.get('time_request', float('inf')))

        print(f"Best proxy: {best_proxy['proxy']} with response time: {best_proxy['time_request']} ms")
        return best_proxy



    def test_proxy(self,proxy):
        test_url = "http://httpbin.org/ip"
        try:
            start_time = time.time()  # Record the start time
            response = requests.get(test_url, proxies=proxy, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            end_time = time.time()  # Record the end time

            response_time = (end_time - start_time) * 1000  # Calculate response time in milliseconds
            print(f"Proxy is working. Response time: {response_time:.2f} ms")
            return response_time
        except requests.RequestException as e:
            print(f"Proxy failed: {e}")
            return -1