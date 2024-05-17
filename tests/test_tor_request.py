# Save this as test_tor_request.py

import pytest
from src.TorRequest import TorRequest

# Fixture to create an instance of TorRequest for each test
@pytest.fixture
def tor_request():
    return TorRequest()

# Test the GET request method
def test_get_request(tor_request):
    test_url = "http://httpbin.org/get"
    response = tor_request.get(test_url)
    
    # Check if the response is a dictionary and contains the expected keys
    assert response is not None
    assert isinstance(response, dict)
    assert "args" in response

# Test the POST request method
def test_post_request(tor_request):
    test_url = "http://httpbin.org/post"
    data = {"key": "value"}
    response = tor_request.post(test_url, data=data)
    
    # Check if the response is a dictionary and contains the expected keys
    assert response is not None
    assert isinstance(response, dict)
    assert "form" in response
    assert response["form"] == data

