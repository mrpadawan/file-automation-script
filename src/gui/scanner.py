"""
GUI scanning workflow.

Responsibilities:
- Scan configured input folder
- Display detected files in the GUI
"""

from src.core.detector import scan_folder
from src.shared.config import DOWNLOADS_PATH

from src.gui.helpers import (
    reset_interface,
    update_status,
    update_statistics
)

from src.gui.checkbox_files import (
    create_checkboxes,
    get_selected_files
)


def scan_files(state):
    """
    Scan the downloads folder and
    display all detected files.

    Args:
        state (GUIState):
            Shared GUI state
            containing widgets and
            application data.

    Notes:
        Enables the execute button
        when files are detected and
        updates the interface
        accordingly.
    """

    reset_interface(state)

    state.execute_button.config(
        state="disabled"
    )

    try:

        state.detected_files = scan_folder(
            DOWNLOADS_PATH
        )

        if len(state.detected_files) == 0:

            state.canvas.config(
                height=30
            )

            state.scrollbar.pack_forget()

            update_status(
                state,
                "No files found"
            )

            return

        create_checkboxes(
            state,
            state.detected_files
        )

        update_status(
            state,
            f"{len(state.detected_files)} files detected"
        )

        state.execute_button.config(
            state="normal"
        )

        update_statistics(
            state,
            get_selected_files
        )

    except Exception as error:

        update_status(
            state,
            f"Error: {error}"
        )
