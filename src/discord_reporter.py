from discord_webhook import DiscordWebhook

from config import (
    DISCORD_WEBHOOK_URL
)


def send_summary(message):

    try:

        webhook = DiscordWebhook(
            url=DISCORD_WEBHOOK_URL,
            content=message
        )

        webhook.execute()

    except Exception as error:

        print(
            f"Discord error: {error}"
        )