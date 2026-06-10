"""
Duplicate-safe filename generation.

Responsibilities:
- Generate versioned filenames
- Prevent file overwrites
"""


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
