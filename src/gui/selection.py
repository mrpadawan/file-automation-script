"""
File selection handlers.

Provides functionality for:
- Selecting all files
- Deselecting all files
"""

import tkinter as tk

from src.gui.helpers import (
    update_statistics
)
from src.gui.checkbox_files import get_selected_files


def select_all(state):
    """
    Select all displayed files.

    Marks every file checkbox as
    selected and updates the file
    statistics.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    for widget in state.scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            widget.variable.set(True)

    update_statistics(
        state,
        get_selected_files
    )


def deselect_all(state):
    """
    Deselect all displayed files.

    Clears every file checkbox and
    updates the file statistics.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    for widget in state.scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            widget.variable.set(False)

    update_statistics(
        state,
        get_selected_files
    )
