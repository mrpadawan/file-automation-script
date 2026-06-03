"""
Scheduled automation runner.

Runs automatically from
Windows Task Scheduler.

Responsibilities:
- Scan files automatically
- Sort detected files
- Generate execution reports
- Send Discord notifications

Note:
    This module is executed by
    Windows Task Scheduler and
    performs the same file sorting
    workflow as the manual process
    without user interaction.
"""

from datetime import datetime

from detector import scan_folder
from parser import extract_module
from mover import move_file

from config import DOWNLOADS_PATH

from discord_reporter import (
    send_daily_report
)


def build_report(
        moved_files,
        failed_files
):
    """
    Create a Discord report for
    the automated execution.

    Args:
        moved_files (list):
            Successfully processed
            file names.

        failed_files (list):
            File names that could
            not be processed.

    Returns:
        str:
            Formatted Discord report.
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


    if len(failed_files) == 0:

        report += (
            "\nStatus: Success ✅"
        )

    else:

        report += (
            "\nStatus: Completed with Errors ⚠️"
        )

    return report


def main():
    """
    Execute the automated file
    sorting workflow.

    Scans the configured folder,
    processes all detected files,
    creates an execution report
    and sends the report to
    Discord.
    """

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


    send_daily_report(
        report
    )


if __name__ == "__main__":

    main()