from discord_webhook import DiscordWebhook

from twitter_image_collage_maker import settings


def send_webhook(message: str):
    """Send a message to Discord.
    
    Args:
        message (str): Message to send to Discord.
    """
    webhook = DiscordWebhook(url=settings.webhook_url, content=message)
    return webhook.execute()
