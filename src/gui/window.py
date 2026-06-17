"""
GUI window setup.

Responsibilities:
- Create the root window
- Add the title
- Add progress and statistics widgets
"""

import tkinter as tk
from tkinter import ttk


def create_root(state):
    """
    Create and configure the
    main application window.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.root = tk.Tk()

    state.root.title(
        "M122 File Organizer"
    )

    state.root.geometry(
        "850x650"
    )

    state.root.configure(
        bg="#f5f5f5"
    )


def create_title(state):
    """
    Create the main window title.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    title = tk.Label(
        state.root,
        text="M122 File Organizer",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5",
        fg="#202124"
    )

    title.pack(
        pady=20
    )


def create_progress_area(state):
    """
    Create progress and statistics
    widgets.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.progress = ttk.Progressbar(
        state.root,
        length=600
    )

    state.progress.pack(
        pady=20
    )

    state.stats_label = tk.Label(
        state.root,
        text="Files detected: 0 | Selected: 0",
        bg="#f5f5f5",
        fg="#202124",
        font=("Arial", 10)
    )

    state.stats_label.pack(
        pady=(0, 10)
    )
