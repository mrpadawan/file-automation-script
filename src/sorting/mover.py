"""
File movement functionality.

Responsibilities:
- Determine destination folders
- Determine file subfolders
- Generate duplicate-safe names
- Move files and folders to their destination
"""

from pathlib import Path
import shutil

from src.shared.config import MODULE_MAPPING
from src.shared.config import DEFAULT_UNKNOWN_PATH
from src.shared.config import SUBFOLDER_MAPPING
from src.sorting.mover_categories import get_subfolder_key
from src.sorting.mover_filename import generate_filename


def determine_destination(module):
    """
    Determine module destination path.

    Args:
        module (str): Module identifier.

    Returns:
        str:
            Destination folder path.
    """

    if module in MODULE_MAPPING:
        return MODULE_MAPPING[module]

    if module and module.endswith("E"):
        module_without_suffix = module[:-1]

        if module_without_suffix in MODULE_MAPPING:
            return MODULE_MAPPING[module_without_suffix]

    return MODULE_MAPPING.get(
        module,
        DEFAULT_UNKNOWN_PATH
    )


def determine_subfolder(
        extension,
        destination_folder
):
    """
    Determine subfolder category.

    Args:
        extension (str):
            File extension.

        destination_folder (Path):
            Base folder.

    Returns:
        Path:
            Destination subfolder.
    """
    subfolder_key = get_subfolder_key(
        extension
    )

    if subfolder_key:
        return (
            destination_folder /
            SUBFOLDER_MAPPING[subfolder_key]
        )

    return destination_folder


def move_file(
        file_path,
        module
):
    """
    Move a file or folder to its
    destination.

    Args:
        file_path (Path):
            File or folder to move.

        module (str):
            Extracted module identifier.

    Returns:
        Path:
            Final destination path.
    """

    destination = determine_destination(
        module
    )

    destination_folder = Path(
        destination
    )

    file_path = Path(file_path)

    if file_path.is_file():

        extension = (
            file_path.suffix.lower()
        )

        destination_folder = (
            determine_subfolder(
                extension,
                destination_folder
            )
        )

    destination_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    destination_file = (
        destination_folder /
        file_path.name
    )

    destination_file = (
        generate_filename(
            destination_file,
            file_path
        )
    )

    shutil.move(
        str(file_path),
        str(destination_file)
    )

    return destination_file
