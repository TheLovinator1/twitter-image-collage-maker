import os

import tweepy
import uvicorn
from dhooks import Webhook
from fastapi import FastAPI, HTTPException

from download_images import download_images
from settings import Settings

app = FastAPI(docs_url="/")
api = tweepy.API(Settings.auth)
hook = Webhook(Settings.webhook_url)


@app.get("/add")
async def add(tweet_id: int = None):
    """
    The page where we add tweets that will be downloaded.
    Example: /add?tweet_id=1197649654785069057 to download tweet with ID 1197649654785069057

    Returns string with URL to the image.
    """
    if tweet_id is None:
        raise HTTPException(status_code=404, detail="Tweet not found")

    if os.path.isfile(f"static/tweets/{tweet_id}.png"):
        return {"url": f"{Settings.url}/static/tweets/{tweet_id}.png"}
    return download_images(tweet_id, api, hook)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
