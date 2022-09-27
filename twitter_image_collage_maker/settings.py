import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

webhook_url = os.getenv("WEBHOOK_URL")
url = os.getenv("URL")
static_location = os.getenv("STATIC_LOCATION")
discord_id = os.getenv("DISCORD_ID")
bearer_token = os.getenv("BEARER_TOKEN")

if not webhook_url:
    raise ValueError("WEBHOOK_URL is not set")
if not url:
    raise ValueError("URL is not set")
if not static_location:
    raise ValueError("STATIC_LOCATION is not set")
if not discord_id:
    raise ValueError("DISCORD_ID is not set")
if not bearer_token:
    raise ValueError("BEARER_TOKEN is not set")

# Create the directory for our images
os.makedirs(os.path.join(static_location, "tweets"), exist_ok=True)

# We check if the URL ends with a forward slash. If it does, we remove it.
if url.endswith("/"):
    url = url[:-1]
