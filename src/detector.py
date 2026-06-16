"""
File detection functionality.

Responsibilities:
- Check input folders
- Return processable files
- Ignore operating system metadata files
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
    Retrieve all files from a folder.

    Args:
        folder_path (str):
            Path to scan.

    Returns:
        list:
            List containing all
            detected file objects.
    """

    folder = Path(folder_path)

    files = []

    for item in folder.iterdir():

        if not item.is_file():
            continue
        if item.name.lower() in IGNORED_FILES:
            continue

        files.append(item)

    return files


def scan_folder(folder_path):
    """
    Scan a folder and return all
    detected files.

    Args:
        folder_path (str):
            Folder to scan.

    Returns:
        list:
            List of detected files.

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
