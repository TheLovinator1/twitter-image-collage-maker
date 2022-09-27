import os

import tweepy
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from twitter_image_collage_maker import settings
from twitter_image_collage_maker.download_images import download_images
from twitter_image_collage_maker.webhooks import send_webhook

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
client = tweepy.Client(bearer_token=settings.bearer_token, wait_on_rate_limit=True)


@app.get(
    "/add",
    responses={
        200: {
            "description": "Return the JSON item.",
            "content": {
                "application/json": {
                    "example": {
                        "url": "https://twitter.lovinator.space/static/tweets/1197649654785069057.webp"
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

    # Check if file already exists and if so, return the URL to the image.
    file_name = f"{settings.static_location}/tweets/{tweet_id}"

    if os.path.isfile(f"{file_name}.png"):
        file_type = "png"
    elif os.path.isfile(f"{file_name}.webp"):
        file_type = "webp"
    else:
        json_content = download_images(tweet_id, client)
        send_webhook(
            "Returned image for tweet "
            f"https://twitter.com/i/status/{tweet_id}\n"
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json_content,
        )

    json_content = {
        "url": f"{settings.url}/static/tweets/{tweet_id}.{file_type}",
    }

    send_webhook(
        f"Already had a image for tweet https://twitter.com/i/status/{tweet_id}\n"
    )
    return JSONResponse(status_code=status.HTTP_200_OK, content=json_content)
