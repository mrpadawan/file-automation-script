"""
Scheduled automation report builder.

Responsibilities:
- Format moved file information
- Format failed file information
- Build the final Discord report
"""

from datetime import datetime


def build_report(moved_files, failed_files):
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
        "ðŸ“ Daily File Automation Report\n\n"
        f"Date: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n"
        f"Files moved: {len(moved_files)}\n"
        f"Errors: {len(failed_files)}\n\n"
    )

    if moved_files:
        report += "Moved Files:\n"

        for file in moved_files:
            report += f"âœ“ {file}\n"

    if failed_files:
        report += "\nFailed Files:\n"

        for file in failed_files:
            report += f"âŒ {file}\n"

    if len(failed_files) == 0:
        report += "\nStatus: Success âœ…"
    else:
        report += "\nStatus: Completed with Errors âš ï¸"

    return report
