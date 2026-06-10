"""
GUI sorting cleanup.

Responsibilities:
- Clear processed checkboxes
- Reset selection state
- Restore sorting controls
"""

from gui_helpers import update_statistics
from gui_checkbox_files import get_selected_files


def clear_sorted_files(state):
    """
    Clear the checkbox area after
    sorting has completed.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    for widget in state.scrollable_frame.winfo_children():

        widget.destroy()

    state.detected_files.clear()

    update_statistics(
        state,
        get_selected_files
    )

    state.canvas.config(
        height=30
    )

    state.scrollbar.pack_forget()

    state.execute_button.config(
        state="disabled"
    )
