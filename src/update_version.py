"""
Version update script.

This script updates the project version
in the central version files.

Usage:
    python src/update_version.py 1.0.1

After updating the version:
    git add VERSION README.md src/shared/version.py
    git commit -m "Bump version to 1.0.1"
    git tag -a v1.0.1 -m "Version 1.0.1"
    git push
    git push origin v1.0.1

Versioning scheme:
    MAJOR.MINOR.PATCH

Examples:
    1.0.0 = First stable release
    1.1.0 = New feature added
    1.1.1 = Bug fix
Notes:
    - For my own usage (this and version.py).
"""
from pathlib import Path
import re
import sys


VERSION_FILE = Path("VERSION")
PY_VERSION_FILE = Path("src/shared/version.py")
README_FILE = Path("README.md")


def main():
    """
    Update VERSION, README.md and src/shared/version.py.
    """

    if len(sys.argv) != 2:
        print("Usage: python src/update_version.py 1.0.1")
        return

    version = sys.argv[1]

    VERSION_FILE.write_text(
        version + "\n",
        encoding="utf-8"
    )

    PY_VERSION_FILE.write_text(
        f'"""\nApplication version information.\n"""\n\n__version__ = "{version}"\n',
        encoding="utf-8"
    )

    update_readme_version(
        version
    )

    print(f"Updated version to {version}")


def update_readme_version(version):
    """
    Update the README header version values.
    """

    content = README_FILE.read_text(
        encoding="utf-8"
    )

    content = re.sub(
        r"Version: \*\*[^*]+\*\*",
        f"Version: **{version}**",
        content,
        count=1
    )

    content = re.sub(
        r"Latest Release: \*\*v[^*]+\*\*",
        f"Latest Release: **v{version}**",
        content,
        count=1
    )

    README_FILE.write_text(
        content,
        encoding="utf-8"
    )


if __name__ == "__main__":
    main()
