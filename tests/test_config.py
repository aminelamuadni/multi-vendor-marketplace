"""
Unit tests for checking PEP 8 conformance of the config.py file.

This module includes tests to ensure that the configuration file adheres to
PEP 8, the Python style guide, which helps maintain a consistent coding style
throughout the project.
"""

import unittest
import pycodestyle


class TestConfigDocs(unittest.TestCase):
    """
    A test case for checking PEP 8 compliance of the config.py file.
    """

    def test_pep8_conformance(self):
        """
        Test if config.py adheres to PEP 8 standards.

        This test will fail if any PEP 8 standards are violated in config.py.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['config.py'])
        self.assertEqual(result.total_errors, 0, result.messages)


if __name__ == '__main__':
    unittest.main()
