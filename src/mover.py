"""
File movement functionality.

Responsibilities:
- Determine destination folders
- Determine file subfolders
- Generate duplicate-safe names
- Move files to their destination
"""

from pathlib import Path
import shutil

from config import MODULE_MAPPING
from config import DEFAULT_UNKNOWN_PATH
from config import SUBFOLDER_MAPPING


def determine_destination(module):
    """
    Determine module destination path.

    Args:
        module (str): Module identifier.

    Returns:
        str:
            Destination folder path.
    """

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

    exercise_extensions = [
        ".docx",
        ".doc",
        ".xlsx",
        ".pptx"
    ]

    theory_extensions = [
        ".pdf",
        ".txt"
    ]

    code_extensions = [
        ".py",
        ".cs",
        ".java",
        ".js",
        ".html",
        ".css",
        ".cpp"
    ]

    if extension in exercise_extensions:

        return (
            destination_folder /
            SUBFOLDER_MAPPING["exercise"]
        )

    elif extension in theory_extensions:

        return (
            destination_folder /
            SUBFOLDER_MAPPING["theory"]
        )

    elif extension in code_extensions:

        return (
            destination_folder /
            SUBFOLDER_MAPPING["code"]
        )

    return destination_folder


def generate_filename(
        destination_file,
        file_path
):
    """
    Generate duplicate-safe filename.

    Args:
        destination_file (Path):
            Target file path.

        file_path (Path):
            Source file path.

    Returns:
        Path:
            Safe file path.
    """

    counter = 2

    while destination_file.exists():

        filename = file_path.stem

        extension = file_path.suffix

        new_name = (
            f"{filename}_V{counter}{extension}"
        )

        destination_file = (
            destination_file.parent /
            new_name
        )

        counter += 1

    return destination_file


def move_file(
        file_path,
        module
):
    """
    Move a file to its destination.

    Args:
        file_path (Path):
            File to move.

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