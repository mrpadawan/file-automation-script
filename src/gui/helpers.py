"""
GUI helper functions.

Provides utility functions for:
- Updating status information
- Updating file statistics
- Managing scrollbars
- Resizing checkbox areas
- Resetting interface elements
"""

import tkinter as tk


def update_status(state, message):
    """
    Update the status label.

    Args:
        state (GUIState):
            Shared GUI state.

        message (str):
            Status message to display.
    """

    state.status_label.config(
        text=message
    )

    state.root.update_idletasks()


def update_statistics(state, get_selected_files):
    """
    Update file statistics.

    Displays the total number of
    detected files and currently
    selected files.

    Args:
        state (GUIState):
            Shared GUI state.

        get_selected_files (function):
            Function used to retrieve
            selected files.
    """

    detected = len(
        state.detected_files
    )

    selected = len(
        get_selected_files(state)
    )

    state.stats_label.config(
        text=f"Files detected: {detected} | Selected: {selected}"
    )


def update_scrollbar(state):
    """
    Show or hide the scrollbar
    depending on the content size.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.root.update_idletasks()

    content_height = (
        state.scrollable_frame.winfo_reqheight()
    )

    canvas_height = (
        state.canvas.winfo_height()
    )

    if content_height > canvas_height:

        state.scrollbar.pack(
            side="right",
            fill="y"
        )

    else:

        state.scrollbar.pack_forget()


def update_checkbox_area(state):
    """
    Dynamically resize the checkbox
    area based on the number of
    displayed files.

    Scrolling is enabled when the
    maximum visible size is reached.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.root.update_idletasks()

    file_count = len(
        state.scrollable_frame.winfo_children()
    )

    visible_rows = min(
        file_count,
        8
    )

    new_height = max(
        visible_rows * 28,
        30
    )

    state.canvas.config(
        height=new_height
    )

    update_scrollbar(state)


def reset_interface(state):
    """
    Reset progress information and
    clear the processed files list.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.progress["value"] = 0

    state.files_listbox.delete(
        0,
        tk.END
    )