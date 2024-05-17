import pytest
from src.ProxyPool import ProxyPool

# Fixture to create an instance of ProxyPool for each test
@pytest.fixture
def proxy_pool():
    return ProxyPool()



def test_get_random_proxy(proxy_pool):

    proxy_url = proxy_pool.get_random_proxy()

    # Proxy URL should be in the correct format
    print("Selected Proxy is: "+proxy_url)
    assert proxy_url is not None

def test_proxy(proxy_pool):
    proxy = {
        'http': 'http://10.10.1.10:9050',
        'https': 'http://10.10.1.10:9050',
    }
    proxy_pool.test_proxy(proxy)


