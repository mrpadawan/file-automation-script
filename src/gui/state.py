"""
GUI state container.

Stores references to all widgets
and shared GUI data.
"""


class GUIState:
    """
    Stores references to GUI widgets
    and application state.
    """

    def __init__(self):
        """
        Initialize the GUI state.

        Creates placeholder
        attributes for widgets and
        shared application data.
        """

        # Main window
        self.root = None

        # Labels
        self.status_label = None
        self.stats_label = None
        self.processed_label = None

        # Buttons
        self.scan_button = None
        self.execute_button = None
        self.select_all_button = None
        self.deselect_all_button = None

        # Progress
        self.progress = None

        # File list
        self.files_listbox = None

        # Checkbox area
        self.canvas = None
        self.scrollbar = None
        self.scrollable_frame = None
        self.checkbox_container = None

        # File data
        self.detected_files = []