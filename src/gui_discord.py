"""
Discord reporting helpers.

Creates and sends manual file
sorting reports to Discord.
"""

from discord_reporter import (
    send_manual_report as discord_manual_report
)


def send_manual_report(moved_files):
    """
    Send a manual file sorting
    report to Discord.

    Args:
        moved_files (list):
            List of successfully
            moved file names.

    Notes:
        Errors during report
        transmission are caught
        and printed to the console.
    """

    report = (
        "📁 Manual File Sorting Report\n\n"
    )

    report += (
        f"Files moved: {len(moved_files)}\n\n"
    )

    for file in moved_files:

        report += (
            f"✓ {file}\n"
        )

    report += (
        "\nStatus: Success ✅"
    )

    try:

        discord_manual_report(
            report
        )

    except Exception as error:

        print(
            f"Discord error: {error}"
        )