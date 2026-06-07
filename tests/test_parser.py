"""
Unit tests for module identifier parsing.
"""

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from parser import extract_module


class TestModuleParser(unittest.TestCase):
    """
    Validates extraction of module identifiers from filenames using the
    project's parser rules.
    """

    def test_valid_module(self):
        """
        Verify that a valid filename containing a module identifier returns
        the expected module code.
        """

        module = extract_module("M122_ProjectDocumentation.pdf")

        self.assertEqual("M122", module)

    def test_invalid_module(self):
        """
        Verify that a filename without a valid module identifier returns None
        instead of producing an incorrect module assignment.
        """

        module = extract_module("ProjectDocumentation.pdf")

        self.assertIsNone(module)


if __name__ == "__main__":
    unittest.main()
