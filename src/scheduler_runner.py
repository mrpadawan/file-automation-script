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

from detector import scan_folder
from parser import extract_module
from mover import move_file
from config import DOWNLOADS_PATH
from scheduler_report import build_report
from discord_reporter import send_daily_report


def process_scheduled_files(files):
    """
    Process files for scheduled
    automation.

    Args:
        files (list):
            Files detected in the
            configured input folder.

    Returns:
        tuple:
            Moved file names and
            failed file names.
    """

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

    return moved_files, failed_files


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

    moved_files, failed_files = process_scheduled_files(
        files
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
