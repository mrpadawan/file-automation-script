"""
Unit tests for file detection functionality.
"""

import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from detector import scan_folder


class TestFileDetector(unittest.TestCase):
    """
    Validates that the detector module identifies files from a configured
    input directory without returning nested folders as processable files.
    """

    def test_file_detection(self):
        """
        Verify that files located directly inside the input folder are detected
        and returned as pathlib Path objects.
        """

        with tempfile.TemporaryDirectory() as temporary_directory:
            input_folder = Path(temporary_directory)
            expected_file = input_folder / "M122_TestDocument.pdf"
            ignored_folder = input_folder / "nested"

            expected_file.write_text("test content", encoding="utf-8")
            ignored_folder.mkdir()

            detected_files = scan_folder(input_folder)

            self.assertIn(expected_file, detected_files)
            self.assertNotIn(ignored_folder, detected_files)
            self.assertEqual(1, len(detected_files))


if __name__ == "__main__":
    unittest.main()
