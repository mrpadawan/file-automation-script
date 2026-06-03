"""
Module parsing functionality.

Responsibilities:
- Detect module identifiers
- Extract module numbers from filenames
"""

import re


def find_module(filename):
    """
    Search for a module identifier.

    Args:
        filename (str): Name of the file.

    Returns:
        Match | None:
            Regex match object.
    """

    return re.search(
        r"M\d+",
        filename
    )


def extract_module(filename):
    """
    Extract the module identifier.

    Args:
        filename (str): Name of file.

    Returns:
        str | None:
            Module identifier or None.
    """

    match = find_module(
        filename
    )

    if match:

        return match.group()

    return None