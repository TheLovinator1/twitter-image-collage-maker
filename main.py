import os
import tempfile

import requests
import tweepy
from dhooks import Webhook
from dotenv import load_dotenv
from flask import Flask, render_template, request
from PIL import Image, ImageOps

app = Flask(__name__)
load_dotenv(verbose=True)

hook = Webhook(os.environ["WEBHOOK_URL"])
url = os.environ["URL"]

# TODO: Change this to actual boolean instead of a string that is True or False lol
hidden_ip = os.getenv("DISABLE_IP", default="True")
discord_username = os.getenv("DISCORD_ID", default="126462229892694018")

auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])

auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)


def link_list(tweet):
    """Generate a list with all the images in the tweet."""
    link_list = []
    if "media" in tweet.entities:
        for media in tweet.extended_entities["media"]:
            link = media["media_url_https"]
            link_list.append(link)

    return link_list


def notify_discord(message: str):
    if request.environ.get("HTTP_X_FORWARDED_FOR") is None:
        ip = request.environ["REMOTE_ADDR"]
    else:
        ip = request.environ["HTTP_X_FORWARDED_FOR"]

    if hidden_ip == "False":
        hook.send(f"{ip} {message}")
    else:
        hook.send(f"Someone {message}")


def download_images(tweet_id: int):
    """
    Downloads images from Twitter and makes them into one image with Pillow.

    tweet_id is snowflake ID for tweet.

    Returns json with url for our created image. If tweet only has one image we
    send that instead of creating our own.
    """
    try:
        images = []
        tweet = api.get_status(tweet_id, tweet_mode="extended")
        links = link_list(tweet)  # Generates a list with all the images in the tweet.
        x_offset = 0

        for link in links:
            with tempfile.SpooledTemporaryFile() as tmp:
                print("Trying to download " + link)
                response = requests.get(link)
                tmp.write(response.content)

                # Crop to 512 by 512 pixels
                thumb = ImageOps.fit(Image.open(tmp), (512, 512), Image.ANTIALIAS)

                # Create temp file to store the cropped image, we remove it manually later
                filename = tempfile.NamedTemporaryFile(suffix=".png", delete=False)

                # Save the crop
                thumb.save(filename)
                print(f"Saved {filename.name} ({link})")

                # Add the path to list so we can combine them later
                images.append(str(filename.name))

        if len(links) == 1:
            print("Found 1 link")
            image_url = (
                tweet.extended_entities["media"][0]["media_url_https"]
                .replace(".png", "?format=png&name=orig")
                .replace(".jpg", "?format=jpg&name=orig")
            )  # Get better quality

            return {
                "url": image_url,
            }

        if len(links) == 2:
            print("Found 2 links")
            imgs = list(map(Image.open, (images[0], images[1])))
            new_im = Image.new("RGB", (1024, 512))

            for img in imgs:
                new_im.paste(img, (x_offset, 0))
                x_offset += img.size[0]

        if len(links) == 3:
            print("Found 3 links")
            imgs = list(map(Image.open, (images[0], images[1], images[2])))
            new_im = Image.new("RGB", (1536, 512))

            for img in imgs:
                new_im.paste(img, (x_offset, 0))
                x_offset += img.size[0]

        if len(links) == 4:
            print("Found 4 links")
            imgs = list(map(Image.open, (images[0], images[1], images[2], images[3])))
            new_im = Image.new("RGB", (1024, 1024))

            new_im.paste(imgs[0], (0, 0))
            new_im.paste(imgs[1], (512, 0))
            new_im.paste(imgs[2], (0, 512))
            new_im.paste(imgs[3], (512, 512))

        # Save our merged image
        new_im.save(f"static/tweets/{tweet_id}.png")
        print(f"Saved merged image for https://twitter.com/i/status/{tweet_id}")
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }
    except Exception as e:
        print("Error: " + str(e))
        notify_discord(
            f"errored for https://twitter.com/i/status/{tweet_id}\n{e} "
            f"<@{discord_username}>"
        )
    finally:
        filename.close()
        for image in images:
            print(f"Removing {image}")
            os.remove(str(image))


@app.route("/add")
def add():
    """
    The page where we add tweets that will be downloaded.
    Example: /add?tweet_id=1197649654785069057 to download tweet with ID 1197649654785069057

    Returns string with URL to the image.
    """

    tweet_id = request.args.get("tweet_id", default=1, type=int)
    print(f"Add: Tweet ID: {tweet_id}")
    if tweet_id == 1:
        return (
            "Please add correct tweet id, e.g "
            "https://twitter.lovinator.space/add?tweet_id=1197649654785069057"
        )

    if os.path.isfile(f"static/tweets/{tweet_id}.png"):
        print(f"{tweet_id} is already converted.")
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }
    notify_discord(f"made image for https://twitter.com/i/status/{tweet_id}")
    return download_images(tweet_id)


@app.route("/")
def index():
    """Renders /templates/index.html"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
