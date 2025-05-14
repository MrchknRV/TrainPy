from unittest.mock import patch
import requests


def get_github_user_info(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.json()


@patch("requests.get")
def test_get_github_user_info(mock_get):
    mock_get.return_value.json.return_value = {"login": "testuser", "name": "Test User"}
    assert get_github_user_info("testuser") == {"login": "testuser", "name": "Test User"}
    mock_get.assert_called_once_with("https://api.github.com/users/testuser")
