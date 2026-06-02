"""
Graphical User Interface for the
M122 File Organizer project.

Responsibilities:
- Scan files
- Display selectable files
- Execute sorting
- Show progress
- Display status information
"""

import tkinter as tk
from tkinter import ttk

from detector import scan_folder
from parser import extract_module
from mover import move_file
from config import DOWNLOADS_PATH
from discord_reporter import send_summary


detected_files = []


def update_status(message):
    """
    Update status label.

    Args:
        message (str):
            Status text
    """

    status_label.config(
        text=message
    )

    root.update_idletasks()

def update_statistics():
    """
    Update file statistics.
    """

    detected = len(
        detected_files
    )

    selected = len(
        get_selected_files()
    )

    stats_label.config(
        text=f"Files detected: {detected} | Selected: {selected}"
    )

def update_scrollbar():
    """
    Show scrollbar only when needed.
    """

    root.update_idletasks()

    content_height = (
        scrollable_frame.winfo_reqheight()
    )

    canvas_height = (
        canvas.winfo_height()
    )

    if content_height > canvas_height:

        scrollbar.pack(
            side="right",
            fill="y"
        )

    else:

        scrollbar.pack_forget()

def update_checkbox_area():
    """
    Resize checkbox area dynamically.

    The checkbox container grows
    with the number of files until
    a maximum size is reached.

    After that, scrolling is used.
    """

    root.update_idletasks()

    file_count = len(
        scrollable_frame.winfo_children()
    )

    visible_rows = min(
        file_count,
        8
    )

    new_height = max(
        visible_rows * 28,
        30
    )

    canvas.config(
        height=new_height
    )

    update_scrollbar()

def select_all():
    """
    Select all files.
    """

    for widget in scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            widget.variable.set(True)

    update_statistics()


def deselect_all():
    """
    Deselect all files.
    """

    for widget in scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            widget.variable.set(False)

    update_statistics()

def reset_interface():
    """
    Reset progress and file list.
    """

    progress["value"] = 0

    files_listbox.delete(
        0,
        tk.END
    )


def create_checkboxes(files):
    """
    Create selectable checkboxes.

    Args:
        files (list):
            Detected files
    """

    for widget in scrollable_frame.winfo_children():

        widget.destroy()


    for file in files:

        variable = tk.BooleanVar(
            value=True
        )

        variable.trace_add(
            "write",
            lambda *args: update_statistics()
        )

        checkbox = tk.Checkbutton(
            scrollable_frame,
            text=file.name,
            variable=variable,
            bg="#f5f5f5",
            font=("Arial",10),
            anchor="w"
        )

        checkbox.pack(
            fill="x",
            padx=10,
            pady=2
        )

        checkbox.variable = variable
        checkbox.file = file

    update_checkbox_area()


def scan_files():
    """
    Scan input folder.
    """

    global detected_files

    reset_interface()

    execute_button.config(
        state="disabled"
    )

    try:

        detected_files = scan_folder(
            DOWNLOADS_PATH
        )


        if len(detected_files) == 0:

            canvas.config(
                height=30
            )

            scrollbar.pack_forget()

            update_status(
                "No files found"
            )

            return

        create_checkboxes(
            detected_files
        )


        update_status(
            f"{len(detected_files)} files detected"
        )


        execute_button.config(
            state="normal"
        )
        
        update_statistics()


    except Exception as error:

        update_status(
            f"❌ {error}"
        )


def get_selected_files():
    """
    Return selected files.

    Returns:
        list:
            Selected files
    """

    selected_files = []


    for widget in scrollable_frame.winfo_children():

        if isinstance(
            widget,
            tk.Checkbutton
        ):

            if widget.variable.get():

                selected_files.append(
                    widget.file
                )


    return selected_files

def send_manual_report(moved_files):
    """
    Send manual execution report
    to Discord.

    Args:
        moved_files (list):
            Successfully moved files.
    """

    report = (
        "📁 Manual File Sorting Report\n\n"
    )

    report += (
        f"Files moved: {len(moved_files)}\n\n"
    )

    for file in moved_files:

        report += (
            f"✓ {file}\n"
        )

    report += (
        "\nStatus: Success ✅"
    )

    try:

        send_summary(
            report
        )

    except Exception as error:

        print(
            f"Discord error: {error}"
        )

def execute_sorting():
    """
    Execute sorting workflow.
    """

    execute_button.config(
        state="disabled",
        text="Sorting..."
    )

    try:

        selected_files = (
            get_selected_files()
        )

        total_files = len(
            selected_files
        )

        if total_files == 0:

            update_status(
                "No files selected"
            )

            return

        progress["maximum"] = (
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

            files_listbox.insert(
                tk.END,
                f"✓ {file.name}"
            )

            progress["value"] = (
                index + 1
            )

            percentage = int(
                ((index + 1)
                 / total_files)
                * 100
            )

            update_status(
                f"Progress: {percentage}%"
            )

        update_status(
            f"✓ Finished ({total_files} files moved)"
        )

        send_manual_report(
            moved_files
        )

        for widget in scrollable_frame.winfo_children():

            widget.destroy()

        detected_files.clear()

        update_statistics()

        canvas.config(
            height=30
        )

        scrollbar.pack_forget()

        execute_button.config(
            state="disabled"
        )

    except Exception as error:

        update_status(
            f"❌ {error}"
        )

    finally:

        execute_button.config(
            state="normal",
            text="Execute Sorting"
        )


"""
Main window
"""

root = tk.Tk()

root.title(
    "M122 File Organizer"
)

root.geometry(
    "850x650"
)

root.configure(
    bg="#f5f5f5"
)


"""
Title
"""

title = tk.Label(
    root,
    text="M122 File Organizer",
    font=("Arial",20,"bold"),
    bg="#f5f5f5",
    fg="#202124"
)

title.pack(
    pady=20
)


"""
Buttons frame
"""

buttons_frame = tk.Frame(
    root,
    bg="#f5f5f5"
)

buttons_frame.pack()


"""
Scan button
"""

scan_button = tk.Button(
    buttons_frame,
    text="Scan Files",
    command=scan_files,
    bg="#4285F4",
    fg="white",
    font=("Arial",11),
    width=20
)

scan_button.grid(
    row=0,
    column=0,
    padx=10
)


"""
Execute button
"""

execute_button = tk.Button(
    buttons_frame,
    text="Execute Sorting",
    command=execute_sorting,
    bg="#34A853",
    fg="white",
    font=("Arial",11),
    width=20,
    state="disabled"
)

execute_button.grid(
    row=0,
    column=1,
    padx=10
)


select_all_button = tk.Button(
    buttons_frame,
    text="Select All",
    command=select_all,
    bg="#FBBC05",
    fg="black",
    font=("Arial",11),
    width=15
)

select_all_button.grid(
    row=0,
    column=2,
    padx=10
)


deselect_all_button = tk.Button(
    buttons_frame,
    text="Deselect All",
    command=deselect_all,
    bg="#EA4335",
    fg="white",
    font=("Arial",11),
    width=15
)

deselect_all_button.grid(
    row=0,
    column=3,
    padx=10
)

"""
Progress bar
"""

progress = ttk.Progressbar(
    root,
    length=600
)

progress.pack(
    pady=20
)

stats_label = tk.Label(
    root,
    text="Files detected: 0 | Selected: 0",
    bg="#f5f5f5",
    fg="#202124",
    font=("Arial",10)
)

stats_label.pack(
    pady=(0,10)
)


"""
Checkbox frame
"""

checkbox_container = tk.Frame(
    root,
    bg="#f5f5f5"
)

checkbox_container.pack(
    fill="both",
    expand=False,
    padx=20
)


canvas = tk.Canvas(
    checkbox_container,
    bg="#f5f5f5",
    height=30,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    checkbox_container,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(
    canvas,
    bg="#f5f5f5"
)


scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack_forget()


"""
Processed files label
"""

processed_label = tk.Label(
    root,
    text="Processed Files",
    bg="#f5f5f5",
    fg="#202124",
    font=("Arial",12,"bold")
)

processed_label.pack(
    pady=(20,5)
)


"""
Processed files list
"""

files_listbox = tk.Listbox(
    root,
    width=100,
    height=12,
    font=("Consolas",10)
)

files_listbox.pack(
    padx=20,
    pady=10
)


"""
Status label
"""

status_label = tk.Label(
    root,
    text="Waiting...",
    bg="#f5f5f5",
    fg="#1a73e8",
    font=("Arial",16,"bold")
)

status_label.pack(
    pady=10
)


root.mainloop()