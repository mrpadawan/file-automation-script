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
    Validates that the detector module identifies processable files and
    folders from a configured input directory.
    """

    def test_file_detection(self):
        """
        Verify that files located directly inside the input folder are detected
        and returned as pathlib Path objects.
        """

        with tempfile.TemporaryDirectory() as temporary_directory:
            input_folder = Path(temporary_directory)
            expected_file = input_folder / "M122_TestDocument.pdf"
            expected_folder = input_folder / "M122_ProjectFolder"

            expected_file.write_text("test content", encoding="utf-8")
            expected_folder.mkdir()

            detected_files = scan_folder(input_folder)

            self.assertIn(expected_file, detected_files)
            self.assertIn(expected_folder, detected_files)
            self.assertEqual(2, len(detected_files))

    def test_technical_folder_ignored(self):
        """
        Verify that clearly technical folders are not returned as processable
        user folders.
        """

        with tempfile.TemporaryDirectory() as temporary_directory:
            input_folder = Path(temporary_directory)
            technical_folder = input_folder / "__pycache__"
            user_folder = input_folder / "M122_ProjectFolder"

            technical_folder.mkdir()
            user_folder.mkdir()

            detected_items = scan_folder(input_folder)

            self.assertIn(user_folder, detected_items)
            self.assertNotIn(technical_folder, detected_items)

    def test_empty_input_folder(self):
        """
        Verify that an existing but empty input folder returns an empty list
        without raising an exception.
        """

        with tempfile.TemporaryDirectory() as temporary_directory:
            detected_files = scan_folder(Path(temporary_directory))

            self.assertEqual([], detected_files)


if __name__ == "__main__":
    unittest.main()
