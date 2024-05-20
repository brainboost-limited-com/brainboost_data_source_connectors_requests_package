from .Request import Request
from .ProxyPool import ProxyPool
from .UserAgentPool import UserAgentPool

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
