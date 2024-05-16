import pytest
from bs4 import BeautifulSoup
from src.Request import Request
import json

def test_get_request():
    req = Request()
    response = req.get('https://whatsmyip.com/')
    
    # Check if the request was successful
    assert response.http == 200  # Assuming 'status' is the attribute for HTTP status code
    
    # Parse the HTML content
    soup = BeautifulSoup(response.html, 'html.parser')  # Assuming 'html' attribute contains HTML content
    
    # Find the element with id 'shownIpv4'
    ip_element = soup.find(id='shownIpv4')
    
    if ip_element is not None:
        # Extract the text content of the element
        ip_address = ip_element.get_text().strip()
        print("Extracted IP Address:", ip_address)
        
        # Assert if the expected IP address is present in the text
        expected_ip = "191.110.58.7"
        assert expected_ip in ip_address, f"Expected IP '{expected_ip}' not found in '{ip_address}'"
    else:
        pytest.fail("The element with id 'shownIpv4' was not found.")

def test_post_request():
    # Create a Request instance
    req = Request()

    # Define the URL for the POST request (JSONPlaceholder's /posts endpoint)
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Define the data to be sent in the POST request (as JSON)
    post_data = {
        'title': 'Test Post',
        'body': 'This is a test post using Request class.',
        'userId': 1
    }

    # Make the POST request
    response = req.post(url, data=post_data)
    
    # Check if the request was successful (assuming 'http' is the attribute for HTTP status code)
    assert response.http == 201  # HTTP status code 201 indicates successful resource creation
    
    # Verify the response content
    # Since 'html' attribute contains the response content, parse it as JSON
    try:
        response_data = json.loads(response.html)
    except json.JSONDecodeError:
        pytest.fail("Failed to parse response content as JSON")
    
    # Verify the response data matches the sent data
    assert response_data['title'] == post_data['title'], "Title mismatch"
    assert response_data['body'] == post_data['body'], "Body mismatch"
    
    # Convert response_data['userId'] to integer for comparison
    response_user_id = int(response_data['userId'])
    assert response_user_id == post_data['userId'], "UserID mismatch"