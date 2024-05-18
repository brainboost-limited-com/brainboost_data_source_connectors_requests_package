import pytest
from unittest.mock import mock_open, patch
from src.brainboost_data_source_requests_package.UserAgentPool import UserAgentPool

@pytest.fixture
def user_agent():
    return UserAgentPool()



def test_get_random_user_agent(user_agent):
    assert user_agent.get_random_user_agent() != None

