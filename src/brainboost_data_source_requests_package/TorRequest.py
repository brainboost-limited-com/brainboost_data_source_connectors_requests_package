from .ProxyRequest import ProxyRequest

class TorRequest(ProxyRequest):
    def __init__(self):
        tor_proxy = {"ip": "127.0.0.1", "port": 9050}
        super().__init__(proxy=tor_proxy)
