"""
GUI checkbox file helpers.

Responsibilities:
- Create file selection checkboxes
- Retrieve selected files
"""

import tkinter as tk

from gui_helpers import (
    update_statistics,
    update_checkbox_area
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

        item_type = (
            "Folder"
            if file.is_dir()
            else "File"
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
            text=f"[{item_type}] {file.name}",
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
