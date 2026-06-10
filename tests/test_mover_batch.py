"""
Batch tests for file movement functionality.
"""

import importlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


class TestFileMoverBatch(unittest.TestCase):
    """
    Validates file movement behavior for mixed file batches.
    """

    def setUp(self):
        """
        Create an isolated filesystem configuration for each batch test.
        """

        self.temporary_directory = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temporary_directory.name)
        self.input_folder = self.workspace / "input"
        self.output_folder = self.workspace / "output"
        self.log_folder = self.workspace / "logs"
        self.mapping_file = self.workspace / "module_mapping.json"

        self.input_folder.mkdir()
        self.output_folder.mkdir()

        configuration = {
            "modules": {
                "M122": str(self.output_folder / "M122"),
                "M114": str(self.output_folder / "M114"),
            },
            "subfolders": {
                "exercise": "Exercises",
                "theory": "Theory",
                "code": "Code",
            },
        }

        self.mapping_file.write_text(
            json.dumps(configuration),
            encoding="utf-8"
        )

        os.environ["DOWNLOADS_PATH"] = str(self.input_folder)
        os.environ["LOG_PATH"] = str(self.log_folder)
        os.environ["DEFAULT_UNKNOWN_PATH"] = str(self.output_folder / "unknown")
        os.environ["MAPPING_FILE"] = str(self.mapping_file)

        import config
        import mover

        importlib.reload(config)
        self.mover = importlib.reload(mover)

    def tearDown(self):
        """
        Remove the isolated filesystem configuration after each batch test.
        """

        self.temporary_directory.cleanup()

    def test_large_mixed_file_set(self):
        """
        Verify that a mixed batch of valid, duplicate, code, and unknown-module
        files is processed without data loss.
        """

        existing_target_folder = self.output_folder / "M122" / "Theory"
        existing_target_folder.mkdir(parents=True)
        existing_file = existing_target_folder / "M122_Report.pdf"
        existing_file.write_text("original", encoding="utf-8")

        source_files = [
            (self.input_folder / "M122_Report.pdf", "duplicate", "M122"),
            (self.input_folder / "M114_Exercise.docx", "exercise", "M114"),
            (self.input_folder / "M999_Notes.pdf", "unknown", "M999"),
            (self.input_folder / "M122_Script.py", "code", "M122"),
            (self.input_folder / "M114_Summary.txt", "summary", "M114"),
        ]

        moved_files = []

        for source_file, content, module in source_files:
            source_file.write_text(content, encoding="utf-8")
            moved_files.append(self.mover.move_file(source_file, module))

        self.assertEqual("original", existing_file.read_text(encoding="utf-8"))
        self.assertEqual(5, len(moved_files))
        self.assertTrue(all(destination.exists() for destination in moved_files))
        self.assertTrue(all(not source.exists() for source, _, _ in source_files))
        self.assertIn(existing_target_folder / "M122_Report_V2.pdf", moved_files)
        self.assertIn(self.output_folder / "M114" / "Exercises" / "M114_Exercise.docx", moved_files)
        self.assertIn(self.output_folder / "unknown" / "Theory" / "M999_Notes.pdf", moved_files)
        self.assertIn(self.output_folder / "M122" / "Code" / "M122_Script.py", moved_files)
        self.assertIn(self.output_folder / "M114" / "Theory" / "M114_Summary.txt", moved_files)


if __name__ == "__main__":
    unittest.main()
