import unittest
from parameterized import parameterized
from utils import access_nested_map  # Make sure to import the function from the correct module


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected value for given inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
