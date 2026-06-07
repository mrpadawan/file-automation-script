"""
Unit tests for GUI selection behavior.
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import gui_selection


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
        self.variable = MagicMock()
        self.variable.get.return_value = selected


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

    @patch("gui_selection.update_statistics")
    def test_select_all(self, mocked_update_statistics):
        """
        Verify that Select All marks every displayed file checkbox as selected
        and requests a statistics refresh.
        """

        gui_selection.select_all(self.state)

        self.first_checkbox.variable.set.assert_called_once_with(True)
        self.second_checkbox.variable.set.assert_called_once_with(True)
        mocked_update_statistics.assert_called_once()

    @patch("gui_selection.update_statistics")
    def test_deselect_all(self, mocked_update_statistics):
        """
        Verify that Deselect All clears every displayed file checkbox and
        requests a statistics refresh.
        """

        gui_selection.deselect_all(self.state)

        self.first_checkbox.variable.set.assert_called_once_with(False)
        self.second_checkbox.variable.set.assert_called_once_with(False)
        mocked_update_statistics.assert_called_once()


if __name__ == "__main__":
    unittest.main()
