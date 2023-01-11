import os

import tweepy

from twitter_image_collage_maker.download_images import download_images


def test_download_images() -> None:
    bearer_token: str | None = os.getenv("BEARER_TOKEN")
    client: tweepy.Client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
    result: dict[str, str] = download_images(tweet_id=1197649654785069057, api=client)
    assert result == {"url": "https://twitter.lovinator.space/static/tweets/1197649654785069057.webp"}
