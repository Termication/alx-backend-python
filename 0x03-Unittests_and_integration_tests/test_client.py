#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class in the client module."""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected_response: dict, mock_get_json: MagicMock) -> None:
        """
        Tests that `GithubOrgClient.org` returns the correct organization data.

        Args:
            org (str): The organization name to be passed to GithubOrgClient.
            expected_response (dict): The expected JSON response for the org.
            mock_get_json (MagicMock): Mocked get_json function.
        """
        # Set the return value for get_json to simulate the API response
        mock_get_json.return_value = expected_response
        
        # Initialize the client and call the org method
        gh_org_client = GithubOrgClient(org)
        result = gh_org_client.org()
        
        # Assert the org method returns the correct response
        self.assertEqual(result, expected_response)
        
        # Ensure get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )


if __name__ == "__main__":
    unittest.main()
