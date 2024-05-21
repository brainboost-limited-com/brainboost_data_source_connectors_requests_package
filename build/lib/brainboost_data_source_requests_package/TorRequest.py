from .ProxyRequest import ProxyRequest

class TorRequest(ProxyRequest):

    def __init__(self):
        print('Tor request initialized')
        tor_proxy = {"ip": "127.0.0.1", "port": 9050}
        super().__init__(proxy=tor_proxy)

    def get(self, page, data={}):
        print('executing get from Tor')
        get_result = super().get(page=page,data=data)       
        if get_result:
            print('Tor request successful for ' + page)
        return get_result

    def post(self, page, data={}):
        print('executing post from Tor')
        post_result = super().post(page=page,data=data)       
        if post_result:
            print('Tor request successful for ' + page)
        return post_result