"""
Version update script.

This script updates the project version
in the central version files.

Usage:
    python scripts/update_version.py 1.0.1

After updating the version:
    git add VERSION src/version.py
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
import sys


VERSION_FILE = Path("VERSION")
PY_VERSION_FILE = Path("src/version.py")


def main():
    """
    Update VERSION and src/version.py.
    """

    if len(sys.argv) != 2:
        print("Usage: python scripts/update_version.py 1.0.1")
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

    print(f"Updated version to {version}")


if __name__ == "__main__":
    main()