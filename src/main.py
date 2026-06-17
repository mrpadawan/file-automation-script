"""
Main application workflow.

Coordinates:
- File detection
- Parsing
- File movement
- Logging
- Error handling

Note:
    This module serves as the
    application's entry point and
    coordinates all core workflow
    components.
"""


from src.core.detector import scan_folder
from src.core.parser import extract_module
from src.sorting.mover import move_file

from src.shared.config import DOWNLOADS_PATH
from src.shared.logger import logger

def process_file(file):
    """
    Process a single file.

    Extracts the module name,
    moves the file to its target
    location and writes log
    entries for successful or
    failed operations.

    Args:
        file (Path):
            File to process.
    """

    try:

        module = extract_module(
            file.name
        )


        moved_file = move_file(
            file,
            module
        )


        print(
            f"{file.name} -> {moved_file}"
        )


        logger.info(
            f"Moved file: {file.name}"
        )


    except PermissionError as error:

        logger.error(
            f"Permission denied: {error}"
        )


    except Exception as error:

        logger.error(
            f"File processing failed: {error}"
        )


def process_all_files():
    """
    Process all files found in the
    configured downloads folder.

    Scans the folder for files and
    processes each file
    individually.
    """

    files = scan_folder(
        DOWNLOADS_PATH
    )


    print(
        "\nProcessing files:\n"
    )


    for file in files:

        process_file(
            file
        )


def main():

    """
    Start the application.

    Initializes the workflow,
    processes all detected files
    and handles critical
    application errors.
    """

    logger.info(
        "Application started"
    )


    try:

        process_all_files()


    except Exception as error:

        logger.critical(
            f"Application failed: {error}"
        )


if __name__ == "__main__":

    main()
