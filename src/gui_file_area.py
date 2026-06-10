"""
GUI file display areas.

Responsibilities:
- Create checkbox scroll area
- Create processed file list
- Create status label
"""

import tkinter as tk


def create_checkbox_area(state):
    """
    Create the selectable file area.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.checkbox_container = tk.Frame(
        state.root,
        bg="#f5f5f5"
    )

    state.checkbox_container.pack(
        fill="both",
        expand=False,
        padx=20
    )

    state.canvas = tk.Canvas(
        state.checkbox_container,
        bg="#f5f5f5",
        height=30,
        highlightthickness=0
    )

    state.scrollbar = tk.Scrollbar(
        state.checkbox_container,
        orient="vertical",
        command=state.canvas.yview
    )

    state.scrollable_frame = tk.Frame(
        state.canvas,
        bg="#f5f5f5"
    )

    state.scrollable_frame.bind(
        "<Configure>",
        lambda e:
        state.canvas.configure(
            scrollregion=state.canvas.bbox("all")
        )
    )

    state.canvas.create_window(
        (0, 0),
        window=state.scrollable_frame,
        anchor="nw"
    )

    state.canvas.configure(
        yscrollcommand=state.scrollbar.set
    )

    state.canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    state.scrollbar.pack_forget()


def create_processed_file_area(state):
    """
    Create the processed files list.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.processed_label = tk.Label(
        state.root,
        text="Processed Files",
        bg="#f5f5f5",
        fg="#202124",
        font=("Arial", 12, "bold")
    )

    state.processed_label.pack(
        pady=(20, 5)
    )

    state.files_listbox = tk.Listbox(
        state.root,
        width=100,
        height=12,
        font=("Consolas", 10)
    )

    state.files_listbox.pack(
        padx=20,
        pady=10
    )


def create_status_label(state):
    """
    Create the status label.

    Args:
        state (GUIState):
            Shared GUI state.
    """

    state.status_label = tk.Label(
        state.root,
        text="Waiting...",
        bg="#f5f5f5",
        fg="#1a73e8",
        font=("Arial", 16, "bold")
    )

    state.status_label.pack(
        pady=10
    )
