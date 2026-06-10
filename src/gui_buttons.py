"""
GUI button creation.

Responsibilities:
- Create action buttons
- Connect button commands
"""

import tkinter as tk

from gui_file_operations import (
    scan_files,
    execute_sorting
)

from gui_selection import (
    select_all,
    deselect_all
)


def create_buttons(state):
    """
    Create the main action buttons.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    buttons_frame = tk.Frame(
        state.root,
        bg="#f5f5f5"
    )

    buttons_frame.pack()

    state.scan_button = tk.Button(
        buttons_frame,
        text="Scan Files",
        command=lambda: scan_files(state),
        bg="#4285F4",
        fg="white",
        font=("Arial", 11),
        width=20
    )

    state.scan_button.grid(
        row=0,
        column=0,
        padx=10
    )

    state.execute_button = tk.Button(
        buttons_frame,
        text="Execute Sorting",
        command=lambda: execute_sorting(state),
        bg="#34A853",
        fg="white",
        font=("Arial", 11),
        width=20,
        state="disabled"
    )

    state.execute_button.grid(
        row=0,
        column=1,
        padx=10
    )

    state.select_all_button = tk.Button(
        buttons_frame,
        text="Select All",
        command=lambda: select_all(state),
        bg="#FBBC05",
        fg="black",
        font=("Arial", 11),
        width=15
    )

    state.select_all_button.grid(
        row=0,
        column=2,
        padx=10
    )

    state.deselect_all_button = tk.Button(
        buttons_frame,
        text="Deselect All",
        command=lambda: deselect_all(state),
        bg="#EA4335",
        fg="white",
        font=("Arial", 11),
        width=15
    )

    state.deselect_all_button.grid(
        row=0,
        column=3,
        padx=10
    )
