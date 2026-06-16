"""
Graphical User Interface for the
M122 File Organizer project.

Responsibilities:
- Create GUI widgets
- Configure the main window
- Connect user actions
- Start the application
"""

from gui_footer import create_version_label
from gui_state import GUIState
from gui_window import (
    create_root,
    create_title,
    create_progress_area
)
from gui_buttons import create_buttons
from gui_file_area import (
    create_checkbox_area,
    create_processed_file_area,
    create_status_label
)

state = GUIState()

create_root(state)
create_title(state)
create_buttons(state)
create_progress_area(state)
create_checkbox_area(state)
create_processed_file_area(state)
create_status_label(state)
create_version_label(state)

state.root.mainloop()