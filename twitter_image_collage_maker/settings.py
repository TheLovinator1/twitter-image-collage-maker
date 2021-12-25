import os
from pathlib import Path

import tweepy
from platformdirs import user_data_dir


class Settings:

    webhook_url = os.environ["WEBHOOK_URL"]
    url = os.environ["URL"]

    data_dir = user_data_dir("twitter-image-collage-maker", "TheLovinator")
    static_location = os.getenv("STATIC_LOCATION", default=data_dir)

    # Create folder for our images
    Path(os.path.join(static_location, "tweets")).mkdir(parents=True, exist_ok=True)

    # TODO: Change this to actual boolean instead of a string that is True or False lol
    hidden_ip = os.getenv("DISABLE_IP", default="True")
    discord_username = os.getenv("DISCORD_ID", default="126462229892694018")

    auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])

    auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
