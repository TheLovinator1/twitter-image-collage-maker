import os
import tempfile

import requests
import tweepy
from PIL import Image, ImageOps

from twitter_image_collage_maker import settings


def download_images(tweet_id: int, api: tweepy.Client) -> dict:
    """
    Downloads images from Twitter and makes them into one image with Pillow.

    Args:
        tweet_id: The ID of the tweet to download images from.
        api: The Tweepy API object. This is used to download the tweet.

    Returns:
        Json with url for our created image, if tweet only has one image we send that instead of creating our own.

    """
    images = []
    links = []
    tweet = api.get_tweet(id=tweet_id, expansions=["attachments.media_keys"], media_fields=["url"])

    if tweet.includes:
        includes = tweet.includes
    if "media" in includes:
        media_list: list[dict] = [media.data for media in tweet.includes["media"]]
        for image in media_list:
            links.append(image["url"])

    x_offset = 0

    for link in links:
        with tempfile.SpooledTemporaryFile() as tmp:
            print(f"Trying to download {link}")
            response = requests.get(link)
            tmp.write(response.content)

            # Crop to 512 by 512 pixels
            thumb = ImageOps.fit(Image.open(tmp), (512, 512))

            # Create temp file to store the cropped image
            # We remove it manually later.
            with tempfile.NamedTemporaryFile(
                    suffix=".png",
                    delete=False,
            ) as filename:
                # Save the crop
                thumb.save(filename)
                print(f"Saved {filename.name} ({link})")

                # Add the path to list, so we can combine them later.
                images.append(str(filename.name))

    if len(links) == 1:
        print("Found 1 image, returning that instead of creating our own")
        return {"url": image['url']}

    if len(links) == 2:
        print("Found 2 images")
        imgs = list(map(Image.open, (images[0], images[1])))
        new_im = Image.new("RGB", (1024, 512))

        for img in imgs:
            new_im.paste(img, (x_offset, 0))
            x_offset += img.size[0]

    if len(links) == 3:
        print("Found 3 images")
        imgs = list(map(Image.open, (images[0], images[1], images[2])))
        new_im = Image.new("RGB", (1536, 512))

        for img in imgs:
            new_im.paste(img, (x_offset, 0))
            x_offset += img.size[0]

    if len(links) == 4:
        print("Found 4 images")
        imgs = list(
            map(
                Image.open,
                (
                    images[0],
                    images[1],
                    images[2],
                    images[3],
                ),
            )
        )
        new_im = Image.new("RGB", (1024, 1024))

        new_im.paste(imgs[0], (0, 0))
        new_im.paste(imgs[1], (512, 0))
        new_im.paste(imgs[2], (0, 512))
        new_im.paste(imgs[3], (512, 512))

    # Save our merged image
    new_im.save(
        f"{settings.static_location}/tweets/{tweet_id}.webp",
        format="WebP",
    )
    print(f"Saved merged image for https://twitter.com/i/status/{tweet_id}")

    # Remove the temp files
    for image in images:
        print(f"Removing {image}")
        os.remove(image)

    return {"url": f"{settings.url}/static/tweets/{tweet_id}.webp"}
