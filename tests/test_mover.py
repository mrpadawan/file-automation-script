"""
Unit tests for file movement functionality.
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


class TestFileMover(unittest.TestCase):
    """
    Validates file movement behavior including destination resolution, missing
    folder creation, and duplicate-safe filename generation.
    """

    def setUp(self):
        """
        Create an isolated filesystem configuration for each mover test.
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
        Remove the isolated filesystem configuration after each mover test.
        """

        self.temporary_directory.cleanup()

    def test_file_move(self):
        """
        Verify that a file is moved to the configured module destination and
        categorized into the expected extension-based subfolder.
        """

        source_file = self.input_folder / "M122_Report.pdf"
        source_file.write_text("report", encoding="utf-8")

        destination_file = self.mover.move_file(source_file, "M122")

        self.assertFalse(source_file.exists())
        self.assertTrue(destination_file.exists())
        self.assertEqual("Theory", destination_file.parent.name)

    def test_duplicate_handling(self):
        """
        Verify that moving a file with an existing target filename creates a
        versioned filename instead of overwriting the existing file.
        """

        target_folder = self.output_folder / "M122" / "Theory"
        target_folder.mkdir(parents=True)
        existing_file = target_folder / "M122_Report.pdf"
        existing_file.write_text("original", encoding="utf-8")

        source_file = self.input_folder / "M122_Report.pdf"
        source_file.write_text("duplicate", encoding="utf-8")

        destination_file = self.mover.move_file(source_file, "M122")

        self.assertEqual("M122_Report_V2.pdf", destination_file.name)
        self.assertEqual("original", existing_file.read_text(encoding="utf-8"))
        self.assertEqual("duplicate", destination_file.read_text(encoding="utf-8"))

    def test_missing_folder_creation(self):
        """
        Verify that the mover creates missing module and category folders
        before moving the selected file.
        """

        source_file = self.input_folder / "M114_Exercise.docx"
        source_file.write_text("exercise", encoding="utf-8")

        destination_file = self.mover.move_file(source_file, "M114")

        self.assertTrue(destination_file.exists())
        self.assertEqual("Exercises", destination_file.parent.name)
        self.assertTrue((self.output_folder / "M114").exists())

    def test_unknown_module_uses_fallback_destination(self):
        """
        Verify that files with modules missing from the mapping are moved into
        the configured fallback destination.
        """

        source_file = self.input_folder / "M999_Notes.pdf"
        source_file.write_text("unknown module", encoding="utf-8")

        destination_file = self.mover.move_file(source_file, "M999")

        self.assertFalse(source_file.exists())
        self.assertTrue(destination_file.exists())
        self.assertEqual(self.output_folder / "unknown" / "Theory", destination_file.parent)

if __name__ == "__main__":
    unittest.main()
