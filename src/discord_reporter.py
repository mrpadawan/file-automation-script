"""
Discord reporting functionality.

Sends execution summaries and
status reports to configured
Discord webhooks.
"""

from discord_webhook import DiscordWebhook

from config import (
    MANUAL_DISCORD_WEBHOOK_URL,
    DAILY_DISCORD_WEBHOOK_URL,
    WEEKLY_DISCORD_WEBHOOK_URL
)


def send_manual_report(message):
    """
    Send a manual execution report.

    Args:
        message (str):
            Report content.
    """

    _send_message(
        MANUAL_DISCORD_WEBHOOK_URL,
        message
    )


def send_daily_report(message):
    """
    Send a daily scheduler report.

    Args:
        message (str):
            Report content.
    """

    _send_message(
        DAILY_DISCORD_WEBHOOK_URL,
        message
    )


def send_weekly_report(message):
    """
    Send a weekly scheduler report.

    Args:
        message (str):
            Report content.
    """

    _send_message(
        WEEKLY_DISCORD_WEBHOOK_URL,
        message
    )


def _send_message(
        webhook_url,
        message
):
    """
    Send a Discord webhook message.

    Args:
        webhook_url (str):
            Target webhook URL.

        message (str):
            Message content.
    """

    try:

        webhook = DiscordWebhook(
            url=webhook_url,
            content=message
        )

        webhook.execute()

    except Exception as error:

        print(
            f"Discord error: {error}"
        )