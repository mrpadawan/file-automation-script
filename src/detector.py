"""
File detection functionality.

Responsibilities:
- Check input folders
- Return processable files and folders
- Ignore operating system metadata items
"""

from pathlib import Path

# Operating system metadata files.
# These values are hardcoded because they
# are application-level technical exclusions
# and not user-configurable business data.
IGNORED_FILES = [
    "desktop.ini",
    "thumbs.db",
    ".ds_store"
]

IGNORED_FOLDERS = [
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache"
]


def folder_exists(folder_path):
    """
    Check whether a folder exists.

    Args:
        folder_path (str):
            Path to the folder.

    Returns:
        bool:
            True if the folder exists,
            otherwise False.
    """

    folder = Path(folder_path)

    return folder.exists()


def get_files(folder_path):
    """
    Retrieve all processable items
    from a folder.

    Args:
        folder_path (str):
            Path to scan.

    Returns:
        list:
            List containing detected
            file and folder objects.
    """

    folder = Path(folder_path)

    items = []

    for item in folder.iterdir():

        item_name = item.name.lower()

        if item.is_file() and item_name in IGNORED_FILES:
            continue

        if item.is_dir() and item_name in IGNORED_FOLDERS:
            continue

        if item.is_file() or item.is_dir():
            items.append(item)

    return items


def scan_folder(folder_path):
    """
    Scan a folder and return all
    detected files and folders.

    Args:
        folder_path (str):
            Folder to scan.

    Returns:
        list:
            List of detected files
            and folders.

    Raises:
        FileNotFoundError:
            Raised when the specified
            folder does not exist.
    """

    if not folder_exists(folder_path):

        raise FileNotFoundError(
            f"Folder does not exist: {folder_path}"
        )

    return get_files(folder_path)
