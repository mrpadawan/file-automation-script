"""
Graphical User Interface for the
M122 File Organizer project.

Responsibilities:
- Create GUI widgets
- Configure the main window
- Connect user actions
- Start the application

Notes:
    This file is intentionally
    larger than the other GUI
    modules because it contains
    the complete user interface
    layout and widget creation.

    Functional logic such as file
    operations, Discord reporting,
    selection handling and helper
    functions has been separated
    into dedicated modules to
    improve maintainability and
    readability.
"""

import tkinter as tk
from tkinter import ttk

from gui_state import GUIState

from gui_file_operations import (
    scan_files,
    execute_sorting
)

from gui_selection import (
    select_all,
    deselect_all
)

state = GUIState()

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

state.root.mainloop()