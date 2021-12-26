import os

import tweepy
import uvicorn
from dhooks import Webhook
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse

from download_images import download_images
from settings import Settings

description = """
Web application that makes 2x2, 3x1 or 2x1 collages from images from Tweets.
Made for [thelovinator1/discord-twitter-webhooks](https://github.com/TheLovinator1/discord-twitter-webhooks)

Send issues to [twitter-image-collage-maker](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
Feel free to send a pull request!

I can be contacted at TheLovinator#9276 on Discord.
"""

app = FastAPI(
    title="twitter-image-collage-maker",
    description=description,
    version="0.0.1",
    contact={
        "name": "Joakim Hellsén",
        "url": "https://github.com/TheLovinator1/twitter-image-collage-maker/",
        "email": "tlovinator@gmail.com",
    },
    license_info={
        "name": "GPLv3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    docs_url="/",
)
api = tweepy.API(Settings.auth)
hook = Webhook(Settings.webhook_url)


@app.get("/add")
async def add(tweet_id: int) -> JSONResponse:
    """
    The page where we add tweets that will be downloaded.
    Example: /add?tweet_id=1197649654785069057 to download tweet with ID 1197649654785069057

    Returns following format: {"url": "https://twitter.lovinator.space/static/tweets/1197649654785069057.png"}
    """
    try:
        # Check if file already exists and if so, return the URL to the image
        if os.path.isfile(f"{Settings.static_location}/tweets/{tweet_id}.png"):
            json_content = {"url": f"{Settings.url}/static/tweets/{tweet_id}.png"}
            hook.send(f"Already had a image for tweet https://twitter.com/i/status/{tweet_id}\n`{json_content}`")
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=json_content)

        # Otherwise download the image and return the URL to the image
        json_content = download_images(tweet_id, api, hook)
        hook.send(f"Returned image for tweet https://twitter.com/i/status/{tweet_id}\n`{json_content}`")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=json_content)

    except Exception as e:
        print("Error: " + str(e))
        hook.send(f"Got exception for https://twitter.com/i/status/{tweet_id}\n{e} <@{Settings.discord_id}>")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)