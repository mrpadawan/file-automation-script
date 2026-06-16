"""
Weekly Discord report.

Sends a weekly summary report.
"""

from datetime import datetime

from discord_reporter import (
    send_weekly_report
)


def main():
    """
    Send weekly report.
    """

    report = (
        "Weekly Automation Report\n\n"
    )

    report += (
        f"Generated: "
        f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n"
    )

    report += (
        "Weekly automation completed successfully."
    )

    send_weekly_report(
        report
    )


if __name__ == "__main__":

    main()
