import configparser
import os

import sys
import tweepy
from dotenv import load_dotenv
from platformdirs import site_data_dir, user_config_dir
from sys import platform

load_dotenv(verbose=True, dotenv_path="../.env")

static_location = site_data_dir(
    "twitter-image-collage-maker",
    "TheLovinator",
)

config_dir = user_config_dir(
    "twitter-image-collage-maker",
    "TheLovinator",
    roaming=True,
)

if platform == "linux":
    # Cool guys don't use /usr/local
    static_location = static_location.replace(
        "/usr/local/share/",
        "/usr/share/",
    )

# Create folder for our images
os.makedirs(os.path.join(static_location, "tweets"), exist_ok=True)

# Create folder for our config
os.makedirs(config_dir, exist_ok=True)

config_location = os.path.join(config_dir, "config.conf")

if not os.path.isfile(config_location):
    print("No config file found, creating one...")
    with open(config_location, "w", encoding="utf8") as config_file:
        config = configparser.ConfigParser()
        config.add_section("twitter")
        config.set("twitter", "api_key", "k3mzbn1SCZ10Pi2D3kz8oX5n0")
        config.set(
            "twitter",
            "api_key_secret",
            "PutfRqOlvEtGQuWuci1gh8FkNZUNlw2vQhyr6sL26SchhlAPI0",
        )
        config.set(
            "twitter",
            "access_token",
            "43123408-Je4YsZBd0cGiifvSS2c84mIr4kopAw8V0oyHi6jN",
        )
        config.set(
            "twitter",
            "access_token_secret",
            "VlHwEQsYqkQd5XvyunwPJb0NAmNNK8zPMTZ6IZKFwmGwN0",
        )

        config.add_section("config")
        config.set(
            "config",
            "webhook_url",
            "https://discord.com/api/webhooks/1234/567890/ABCDEFGHI",
        )
        config.set("config", "url", "https://twitter.lovinator.space/")
        config.set("config", "static_location", static_location)
        config.set("config", "discord_id", "126462229892694018")
        config.set("config", "hidden_ip", "True")

        config.write(config_file)
    sys.exit(f"Please edit the config file at {config_location}")

# Read the config file
config = configparser.ConfigParser()
config.read(config_location)

# Get the configs from the config file
config_webhook_url = config.get("config", "webhook_url")
config_url = config.get("config", "url")
config_static_location = config.get("config", "static_location")
config_discord_id = config.get("config", "discord_id")
config_api_key = config.get("twitter", "api_key")
config_api_key_secret = config.get("twitter", "api_key_secret")
config_access_token = config.get("twitter", "access_token")
config_access_token_secret = config.get("twitter", "access_token_secret")

# If user has environment variables, use them instead
webhook_url = os.getenv("WEBHOOK_URL", config_webhook_url)
url = os.getenv("URL", config_url)
static_location = os.getenv("STATIC_LOCATION", config_static_location)
discord_id = os.getenv("DISCORD_ID", config_discord_id)
api_key = os.getenv("API_KEY", config_api_key)
api_key_secret = os.getenv("API_KEY_SECRET", config_api_key_secret)
access_token = os.getenv("ACCESS_TOKEN", config_access_token)
access_token_secret = os.getenv(
    "ACCESS_TOKEN_SECRET",
    config_access_token_secret,
)

# We check if the URL ends with a forward slash. If it does, we remove it.
if url.endswith("/"):
    url = url[:-1]

# Twitter authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
