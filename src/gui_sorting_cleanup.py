"""
GUI sorting cleanup.

Responsibilities:
- Clear processed checkboxes
- Reset selection state
- Restore sorting controls
"""

from gui_helpers import (
    update_checkbox_area,
    update_statistics
)
from gui_checkbox_files import get_selected_files


def clear_sorted_files(state, sorted_files):
    """
    Remove sorted files from the
    checkbox area after sorting has
    completed.

    Args:
        state (GUIState):
            Shared GUI state.

        sorted_files (list):
            Files that were moved.
    """

    sorted_file_set = set(
        sorted_files
    )

    remaining_files = []

    for widget in list(
            state.scrollable_frame.winfo_children()
    ):

        if widget.file in sorted_file_set:

            widget.destroy()

        else:

            remaining_files.append(
                widget.file
            )

    state.detected_files = remaining_files

    update_statistics(
        state,
        get_selected_files
    )

    update_checkbox_area(state)

    if not state.detected_files:

        state.execute_button.config(
            state="disabled"
        )
