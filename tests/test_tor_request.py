# Save this as test_tor_request.py

import pytest
from src.TorRequest import TorRequest
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fixture to create an instance of TorRequest for each test
@pytest.fixture
def tor_request():
    return TorRequest()

# Test the GET request method
def test_get_request(tor_request):
    test_url = "http://httpbin.org/get"
    response = tor_request.get(page=test_url,data={})

    logger.info(f"POST request IP: {response}")
    
    # Check if the response is a dictionary and contains the expected keys
    assert response is not None


    current_location = tor_request.get_geolocation()

    assert current_location is not None

# Test the POST request method
def test_post_request(tor_request):
    test_url = "http://httpbin.org/post"
    data = {"key": "value"}
    response = tor_request.post(page=test_url,data=data)

    logger.info(f"POST request IP: {response}")
    
    # Check if the response is a dictionary and contains the expected keys
    assert response is not None

    current_location = tor_request.get_geolocation()
    assert current_location is not None
