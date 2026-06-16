"""
For the versioning on the bottom of the GUI.
"""
import tkinter as tk

from version import __version__


def create_version_label(state):
    """
    Create application version label.
    """

    version_label = tk.Label(
        state.root,
        text=f"Version {__version__}",
        bg="#f5f5f5",
        fg="gray",
        font=("Arial", 9)
    )

    version_label.pack(
        side="bottom",
        pady=5
    )

    state.version_label = version_label