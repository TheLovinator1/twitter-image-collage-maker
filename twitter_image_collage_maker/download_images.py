import os
import tempfile

import requests
from PIL import Image, ImageOps

from twitter_image_collage_maker import settings
from twitter_image_collage_maker.link_list import link_list


def download_images(tweet_id: int, api):
    """
    Downloads images from Twitter and makes them into one image with Pillow.

    tweet_id is snowflake ID for tweet.

    Returns json with url for our created image. If tweet only has one image we
    send that instead of creating our own.
    """
    images = []
    tweet = api.get_status(tweet_id, tweet_mode="extended")
    links = link_list(tweet)
    x_offset = 0

    for link in links:
        with tempfile.SpooledTemporaryFile() as tmp:
            print(f"Trying to download {link}")
            response = requests.get(link)
            tmp.write(response.content)

            # Crop to 512 by 512 pixels
            thumb = ImageOps.fit(Image.open(tmp), (512, 512), Image.ANTIALIAS)

            # Create temp file to store the cropped image
            # We remove it manually later
            with tempfile.NamedTemporaryFile(
                    suffix=".png",
                    delete=False,
            ) as filename:
                # Save the crop
                thumb.save(filename)
                print(f"Saved {filename.name} ({link})")

                # Add the path to list so we can combine them later
                images.append(str(filename.name))

    if len(links) == 1:
        print("Found 1 image, returning that instead of creating our own")
        # Get better quality image
        image_url = (
            tweet.extended_entities["media"][0]["media_url_https"]
            .replace(".png", "?format=png&name=orig")
            .replace(".jpg", "?format=jpg&name=orig")
        )

        return {"url": image_url}

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
