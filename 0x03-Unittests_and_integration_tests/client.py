#!/usr/bin/env python3
"""A client to interact with Github organization data."""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """Client class for accessing Github organization data."""
    
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initializes the client with the organization's name."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Retrieves and memoizes the organization details."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Gets the URL for accessing the organization's public repositories."""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Retrieves and memoizes the payload for the organization's repositories."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Fetches a list of public repository names, optionally filtered by license type.
        
        Args:
            license: Optional; the license type to filter repositories by.
        
        Returns:
            A list of repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Checks if a repository has a specific license.
        
        Args:
            repo: A dictionary representing a repository's data.
            license_key: The license key to check for.
        
        Returns:
            True if the repository has the specified license, False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
