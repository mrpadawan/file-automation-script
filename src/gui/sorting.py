"""
GUI sorting workflow.

Responsibilities:
- Process selected files
- Move files to destinations
- Update GUI progress
- Send manual report
"""

import tkinter as tk

from src.core.parser import extract_module
from src.sorting.mover import move_file

from src.gui.helpers import (
    update_status
)

from src.gui.discord import (
    send_manual_report
)

from src.gui.checkbox_files import (
    get_selected_files
)
from src.gui.sorting_cleanup import clear_sorted_files


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

            destination_file = move_file(
                file,
                module
            )

            destination_path = (
                destination_file.resolve()
            )

            moved_files.append(
                f"{file.name} -> {destination_path}"
            )

            state.files_listbox.insert(
                tk.END,
                f"Moved: {file.name} -> {destination_path}"
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
            state,
            selected_files
        )

    except Exception as error:

        update_status(
            state,
            f"Error: {error}"
        )

    finally:

        button_state = (
            "normal"
            if state.detected_files
            else "disabled"
        )

        state.execute_button.config(
            state=button_state,
            text="Execute Sorting"
        )
