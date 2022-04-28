import os

import tweepy
from dhooks import Webhook
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from twitter_image_collage_maker import settings
from twitter_image_collage_maker.download_images import download_images

DESCRIPTION = """
Web application that makes 2x2, 3x1 or 2x1 collages from images from Tweets.
Made for
[thelovinator1/discord-twitter-webhooks](https://github.com/TheLovinator1/discord-twitter-webhooks)

Send issues to
[twitter-image-collage-maker](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
Feel free to send a pull request!

I can be contacted at TheLovinator#9276 on Discord.
"""

app = FastAPI(
    title="twitter-image-collage-maker",
    description=DESCRIPTION,
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
api = tweepy.API(settings.auth)
hook = Webhook(settings.webhook_url)


@app.get(
    "/add",
    responses={
        200: {
            "description": "Return the JSON item.",
            "content": {
                "application/json": {
                    "example": {
                        "url": "https://twitter.lovinator.space/static/tweets/1197649654785069057.webp"  # noqa: E501
                    },
                }
            },
        }
    },
    summary="Make a collage from a tweet",
)
async def add(tweet_id: int):
    """
    Download image from tweet, and return the URL to the image.

    Needs:
    - **tweet_id**: The ID of the tweet. For example: `1197649654785069057`.

    This function will return a JSON object with the URL to the image.

    Example: `https://twitter.lovinator.space/add?tweet_id=1197649654785069057`
    """
    try:
        # Check if file already exists and if so, return the URL to the image
        if os.path.isfile(f"{settings.static_location}/tweets/{tweet_id}.png"):
            json_content = {
                "url": f"{settings.url}/static/tweets/{tweet_id}.png",
            }
            hook.send(
                f"Already had a image for tweet "
                f"https://twitter.com/i/status/{tweet_id}\n"
                f"`{json_content}`"
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=json_content,
            )
        elif os.path.isfile(
            f"{settings.static_location}/tweets/{tweet_id}.webp",
        ):
            json_content = {
                "url": f"{settings.url}/static/tweets/{tweet_id}.webp",
            }
            hook.send(
                "Already had a image for tweet "
                f"https://twitter.com/i/status/{tweet_id}\n"
                f"`{json_content}`"
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=json_content,
            )

        # Otherwise download the image and return the URL to the image
        json_content = download_images(tweet_id, api, hook)
        hook.send(
            "Returned image for tweet "
            f"https://twitter.com/i/status/{tweet_id}\n"
            f"`{json_content}`"
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json_content,
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        hook.send(
            f"<@{settings.discord_id}> Got exception for "
            f"https://twitter.com/i/status/{tweet_id}\n"
            f"{e}"
        )
