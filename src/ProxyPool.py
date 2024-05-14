import asyncio
import aiohttp
import schedule
from tinydb import TinyDB


class ProxyPool:
    '''Manages a pool of proxies for HTTP requests.'''
    def __init__(self):
        self.proxies_db = TinyDB('resources/proxies_db.json')
        self.current_proxy = None

        # Schedule the proxy list update every 10 minutes
        schedule.every(10).minutes.do(self.update_proxies_from_url_async)
        # Start the scheduler in a separate thread
        asyncio.ensure_future(self.run_scheduler())

    async def update_proxies_from_url_async(self):
        url = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.json'
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()  # Raise an exception for bad status codes
                    proxies_data = await response.json()

                    if not isinstance(proxies_data, list):
                        raise ValueError("Invalid proxy data format")

                    # Clear existing proxies in the database
                    self.proxies_db.truncate()

                    # Insert new proxies into the database
                    for proxy_info in proxies_data:
                        if 'ip' in proxy_info and 'port' in proxy_info and 'protocol' in proxy_info:
                            self.proxies_db.insert(dict(proxy_info))
        
        except aiohttp.ClientError as e:
            print(f"Error fetching proxies: {e}")

    async def run_scheduler(self):
        while True:
            await asyncio.sleep(1)  # Sleep briefly to allow other tasks to run
            schedule.run_pending()

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
