"""
Unit tests for GUI selection behavior.
"""

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

os.environ["DOWNLOADS_PATH"] = str(PROJECT_ROOT / "tests" / "test_input")
os.environ["LOG_PATH"] = str(PROJECT_ROOT / "logs")
os.environ["DEFAULT_UNKNOWN_PATH"] = str(
    PROJECT_ROOT / "tests" / "test_output" / "unknown"
)
os.environ["MAPPING_FILE"] = str(
    PROJECT_ROOT / "config" / "module_mapping.json"
)

from src.gui import selection as gui_selection
from src.gui import sorting as gui_sorting
from src.gui import sorting_cleanup as gui_sorting_cleanup


class FakeCheckbutton(gui_selection.tk.Checkbutton):
    """
    Lightweight checkbutton test double used to validate GUI selection logic
    without creating a real Tkinter window.
    """

    def __init__(self, file_name, selected=False):
        """
        Store the checkbox state and associated file name for assertions.
        """

        self.file = file_name
        self.destroyed = False
        self.variable = MagicMock()
        self.variable.get.return_value = selected

    def destroy(self):
        """
        Record that the checkbox would have been removed from the GUI.
        """

        self.destroyed = True


class TestGUISelection(unittest.TestCase):
    """
    Validates checkbox-based GUI selection actions independently from the
    graphical window lifecycle.
    """

    def setUp(self):
        """
        Create a minimal GUI state test double containing selectable files.
        """

        self.first_checkbox = FakeCheckbutton("M122_Report.pdf")
        self.second_checkbox = FakeCheckbutton("M114_Notes.pdf")
        self.state = MagicMock()
        self.state.detected_files = [
            self.first_checkbox.file,
            self.second_checkbox.file,
        ]
        self.state.scrollable_frame.winfo_children.return_value = [
            self.first_checkbox,
            self.second_checkbox,
        ]

    def test_file_selection(self):
        """
        Verify that an individual selected checkbox can be identified from the
        current GUI state.
        """

        self.first_checkbox.variable.get.return_value = True
        self.second_checkbox.variable.get.return_value = False

        selected_files = [
            widget.file
            for widget in self.state.scrollable_frame.winfo_children()
            if isinstance(widget, gui_selection.tk.Checkbutton)
            and widget.variable.get()
        ]

        self.assertEqual(["M122_Report.pdf"], selected_files)

    @patch("src.gui.selection.update_statistics")
    def test_select_all(self, mocked_update_statistics):
        """
        Verify that Select All marks every displayed file checkbox as selected
        and requests a statistics refresh.
        """

        gui_selection.select_all(self.state)

        self.first_checkbox.variable.set.assert_called_once_with(True)
        self.second_checkbox.variable.set.assert_called_once_with(True)
        mocked_update_statistics.assert_called_once()

    @patch("src.gui.selection.update_statistics")
    def test_deselect_all(self, mocked_update_statistics):
        """
        Verify that Deselect All clears every displayed file checkbox and
        requests a statistics refresh.
        """

        gui_selection.deselect_all(self.state)

        self.first_checkbox.variable.set.assert_called_once_with(False)
        self.second_checkbox.variable.set.assert_called_once_with(False)
        mocked_update_statistics.assert_called_once()

    @patch("src.gui.sorting_cleanup.update_checkbox_area")
    def test_clear_sorted_files_keeps_unselected_file(self, mocked_update_area):
        """
        Verify that cleanup removes only moved files and keeps unchecked files
        visible for a later sorting run.
        """

        gui_sorting_cleanup.clear_sorted_files(
            self.state,
            [self.first_checkbox.file]
        )

        self.assertTrue(self.first_checkbox.destroyed)
        self.assertFalse(self.second_checkbox.destroyed)
        self.assertEqual(
            [self.second_checkbox.file],
            self.state.detected_files
        )
        self.state.execute_button.config.assert_not_called()
        mocked_update_area.assert_called_once_with(self.state)

    @patch("src.gui.sorting_cleanup.update_checkbox_area")
    def test_clear_sorted_files_disables_execute_when_empty(
            self,
            mocked_update_area
    ):
        """
        Verify that the execute button is disabled when no detected files remain
        after sorting.
        """

        gui_sorting_cleanup.clear_sorted_files(
            self.state,
            [
                self.first_checkbox.file,
                self.second_checkbox.file,
            ]
        )

        self.assertEqual(
            [],
            self.state.detected_files
        )
        self.state.execute_button.config.assert_called_once_with(
            state="disabled"
        )
        mocked_update_area.assert_called_once_with(self.state)


class TestGUISorting(unittest.TestCase):
    """
    Validates the GUI sorting workflow independently from real Tkinter windows.
    """

    @patch("src.gui.sorting.update_status")
    @patch("src.gui.sorting.send_manual_report")
    @patch("src.gui.sorting.clear_sorted_files")
    @patch("src.gui.sorting.move_file")
    @patch("src.gui.sorting.extract_module")
    @patch("src.gui.sorting.get_selected_files")
    def test_execute_sorting_shows_destination_path(
            self,
            mocked_get_selected_files,
            mocked_extract_module,
            mocked_move_file,
            mocked_clear_sorted_files,
            mocked_send_manual_report,
            mocked_update_status
    ):
        """
        Verify that processed output shows where each selected file was moved.
        """

        selected_file = Path("M122_Report.pdf")
        destination_file = (
            PROJECT_ROOT /
            "output" /
            "M122" /
            "Theory" /
            "M122_Report.pdf"
        )
        state = MagicMock()
        state.detected_files = [selected_file]
        state.progress = {}

        mocked_get_selected_files.return_value = [
            selected_file
        ]
        mocked_extract_module.return_value = "M122"
        mocked_move_file.return_value = destination_file

        gui_sorting.execute_sorting(state)

        state.files_listbox.insert.assert_called_once_with(
            gui_sorting.tk.END,
            f"Moved: M122_Report.pdf -> {destination_file.resolve()}"
        )
        mocked_send_manual_report.assert_called_once_with(
            [
                f"M122_Report.pdf -> {destination_file.resolve()}"
            ]
        )
        mocked_clear_sorted_files.assert_called_once_with(
            state,
            [selected_file]
        )


if __name__ == "__main__":
    unittest.main()
