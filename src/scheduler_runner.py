"""
Scheduled automation runner.

Runs automatically from
Windows Task Scheduler.
"""

from datetime import datetime

from detector import scan_folder
from parser import extract_module
from mover import move_file

from config import DOWNLOADS_PATH

from discord_reporter import (
    send_summary
)


def build_report(
        moved_files,
        failed_files
):
    """
    Create Discord report.
    """

    report = (
        "📁 Daily File Automation Report\n\n"
    )

    report += (
        f"Date: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n"
    )

    report += (
        f"Files moved: {len(moved_files)}\n"
    )

    report += (
        f"Errors: {len(failed_files)}\n\n"
    )


    if moved_files:

        report += "Moved Files:\n"

        for file in moved_files:

            report += (
                f"✓ {file}\n"
            )


    if failed_files:

        report += (
            "\nFailed Files:\n"
        )

        for file in failed_files:

            report += (
                f"❌ {file}\n"
            )


    report += (
        "\nStatus: Success ✅"
    )

    return report


def main():

    files = scan_folder(
        DOWNLOADS_PATH
    )

    moved_files = []

    failed_files = []


    for file in files:

        try:

            module = extract_module(
                file.name
            )

            move_file(
                file,
                module
            )

            moved_files.append(
                file.name
            )

        except Exception:

            failed_files.append(
                file.name
            )


    report = build_report(
        moved_files,
        failed_files
    )


    send_summary(
        report
    )


if __name__ == "__main__":

    main()