"""
File operation handlers.

Responsibilities:
- Scan files
- Create file selection checkboxes
- Retrieve selected files
- Execute file sorting

Notes:
    This file is relatively large
    because it contains the complete
    workflow for scanning, selecting
    and sorting files, including GUI
    updates and error handling.
"""

import tkinter as tk

from detector import scan_folder
from parser import extract_module
from mover import move_file
from config import DOWNLOADS_PATH

from gui_helpers import (
    reset_interface,
    update_status,
    update_statistics,
    update_checkbox_area
)

from gui_discord import (
    send_manual_report
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
            f"❌ {error}"
        )


def get_selected_files(state):
    """
    Return all selected files.

    Args:
        state (GUIState):
            Shared GUI state.

    Returns:
        list:
            List containing all
            selected file objects.
    """

    selected_files = []

    for widget in state.scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            if widget.variable.get():

                selected_files.append(
                    widget.file
                )

    return selected_files


def create_checkboxes(
        state,
        files
):
    """
    Create selectable checkboxes
    for all detected files.

    Args:
        state (GUIState):
            Shared GUI state.

        files (list):
            Files to display as
            selectable checkboxes.
    """

    for widget in state.scrollable_frame.winfo_children():

        widget.destroy()

    for file in files:

        variable = tk.BooleanVar(
            value=True
        )

        variable.trace_add(
            "write",
            lambda *args:
            update_statistics(
                state,
                get_selected_files
            )
        )

        checkbox = tk.Checkbutton(
            state.scrollable_frame,
            text=file.name,
            variable=variable,
            bg="#f5f5f5",
            font=("Arial", 10),
            anchor="w"
        )

        checkbox.pack(
            fill="x",
            padx=10,
            pady=2
        )

        checkbox.variable = variable
        checkbox.file = file

    update_checkbox_area(
        state
    )


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
                f"✓ {file.name}"
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
            f"✓ Finished ({total_files} files moved)"
        )

        send_manual_report(
            moved_files
        )

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

    except Exception as error:

        update_status(
            state,
            f"❌ {error}"
        )

    finally:

        state.execute_button.config(
            state="normal",
            text="Execute Sorting"
        )