from discord_webhook import DiscordWebhook
from requests import Response

from twitter_image_collage_maker import settings


def send_webhook(message: str) -> Response | None:
    """Send a message to Discord.

    Args:
        message (str): Message to send to Discord.

    Returns:
        Response: Response from Discord.
    """

    if not settings.webhook_url:
        return

    webhook: DiscordWebhook = DiscordWebhook(url=settings.webhook_url, content=message)
    return webhook.execute()
