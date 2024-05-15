import pytest
from requests.exceptions import RequestException
from unittest.mock import patch, MagicMock
from src.Request import Request

@pytest.fixture
def request_instance():
    # Create a Request instance with default parameters
    return Request()

def test_get_success(request_instance):
    # Mock the requests.session.get method to simulate a successful GET request
    with patch('request.Request.session.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><body>Hello</body></html>'
        mock_get.return_value = mock_response

        # Call the get() method
        response = request_instance.get('http://whatismyip.com')

        # Assert that the correct response is returned
        assert response.http == 200
        assert response.html == '<html><body>Hello</body></html>'

def test_get_failure(request_instance):
    # Mock the requests.session.get method to simulate a failed GET request
    with patch('request.Request.session.get') as mock_get:
        mock_get.side_effect = RequestException('Failed to connect')

        # Call the get() method
        response = request_instance.get('http://whatismyip.com')

        # Assert that the response indicates a failure
        assert response.http == 0
        assert 'Failed to connect' in response.html

def test_post_success(request_instance):
    # Mock the requests.session.post method to simulate a successful POST request
    with patch('request.Request.session.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.text = '<html><body>Posted</body></html>'
        mock_post.return_value = mock_response

        # Call the post() method
        response = request_instance.post('http://whatismyip.com', data={'key': 'value'})

        # Assert that the correct response is returned
        assert response.http == 201
        assert response.html == '<html><body>Posted</body></html>'

def test_post_failure(request_instance):
    # Mock the requests.session.post method to simulate a failed POST request
    with patch('request.Request.session.post') as mock_post:
        mock_post.side_effect = RequestException('Failed to connect')

        # Call the post() method
        response = request_instance.post('http://whatismyip.com', data={'key': 'value'})

        # Assert that the response indicates a failure
        assert response.http == 0
        assert 'Failed to connect' in response.html
