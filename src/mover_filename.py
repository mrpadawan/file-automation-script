"""
Duplicate-safe filename generation.

Responsibilities:
- Generate versioned item names
- Prevent file and folder overwrites
"""


def generate_filename(
        destination_file,
        file_path
):
    """
    Generate duplicate-safe item name.

    Args:
        destination_file (Path):
            Target file or folder path.

        file_path (Path):
            Source file or folder path.

    Returns:
        Path:
            Safe file path.
    """

    counter = 2

    while destination_file.exists():

        if file_path.is_dir():
            new_name = (
                f"{file_path.name}_V{counter}"
            )

        else:
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
