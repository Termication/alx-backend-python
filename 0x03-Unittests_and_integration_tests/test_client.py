#!/usr/bin/env python3
"""Unit tests for the client module."""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for methods in the `GithubOrgClient` class."""
    
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests that `org` retrieves the correct organization information."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Tests that `_public_repos_url` returns the correct repository URL."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': "https://api.github.com/users/google/repos"}
            self.assertEqual(GithubOrgClient("google")._public_repos_url, "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests that `public_repos` retrieves a list of repository names."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {"name": "episodes.dart", "fork": False},
                {"name": "kratu", "fork": False},
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(), ["episodes.dart", "kratu"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests `has_license` to check if a repository has a specific license."""
        gh_org_client = GithubOrgClient("google")
        self.assertEqual(gh_org_client.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the `GithubOrgClient` class."""
    
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up HTTP request mocks before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            return Mock(**{'json.return_value': route_payload.get(url, HTTPError)})

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests that `public_repos` returns the expected repository names."""
        self.assertEqual(GithubOrgClient("google").public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Tests that `public_repos` returns repos with the specified license."""
        self.assertEqual(GithubOrgClient("google").public_repos(license="apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Stops HTTP request mocks after all tests run."""
        cls.get_patcher.stop()
