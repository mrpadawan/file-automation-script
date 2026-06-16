"""
GUI sorting workflow.

Responsibilities:
- Process selected files
- Move files to destinations
- Update GUI progress
- Send manual report
"""

import tkinter as tk

from parser import extract_module
from mover import move_file

from gui_helpers import (
    update_status
)

from gui_discord import (
    send_manual_report
)

from gui_checkbox_files import (
    get_selected_files
)
from gui_sorting_cleanup import clear_sorted_files


def execute_sorting(state):
    """
    Execute the file sorting
    workflow.

    Args:
        state (GUIState):
            Shared GUI state.

    Notes:
        Processes all selected
        files, moves them to the
        correct destination,
        updates progress
        information and sends a
        Discord report after
        completion.
    """

    state.execute_button.config(
        state="disabled",
        text="Sorting..."
    )

    try:

        selected_files = (
            get_selected_files(
                state
            )
        )

        total_files = len(
            selected_files
        )

        if total_files == 0:

            update_status(
                state,
                "No files selected"
            )

            return

        state.progress["maximum"] = (
            total_files
        )

        moved_files = []

        for index, file in enumerate(
                selected_files
        ):

            module = extract_module(
                file.name
            )

            move_file(
                file,
                module
            )

            moved_files.append(
                file.name
            )

            state.files_listbox.insert(
                tk.END,
                f"Done: {file.name}"
            )

            state.progress["value"] = (
                index + 1
            )

            percentage = int(
                ((index + 1)
                 / total_files)
                * 100
            )

            update_status(
                state,
                f"Progress: {percentage}%"
            )

        update_status(
            state,
            f"Finished ({total_files} files moved)"
        )

        send_manual_report(
            moved_files
        )

        clear_sorted_files(
            state
        )

    except Exception as error:

        update_status(
            state,
            f"Error: {error}"
        )

    finally:

        state.execute_button.config(
            state="normal",
            text="Execute Sorting"
        )
