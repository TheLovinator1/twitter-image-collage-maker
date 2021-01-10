import os

import requests
import tweepy
from dhooks import Webhook
from dotenv import load_dotenv
from flask import Flask, escape, render_template, request
from PIL import Image, ImageOps

app = Flask(__name__)
load_dotenv(verbose=True)

hook = Webhook(os.environ["WEBHOOK_URL"])
url = os.environ["URL"]

auth = tweepy.OAuthHandler(
    os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])

auth.set_access_token(
    os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)


def link_list(tweet):
    link_list = []
    if "media" in tweet.entities:
        for media in tweet.extended_entities["media"]:
            link = media["media_url_https"]
            link_list.append(link)

    if len(link_list) > 1:
        return link_list
    else:
        return False


def download_images(tweet_id: int):
    try:
        tweet = api.get_status(tweet_id)
    except tweepy.error.TweepError as e:
        return f"Tweepy Error: {e}."
    except Exception as e:
        return f"Error: {e}. If the error persists please contact https://github.com/TheLovinator1/twitter-image-downloader"

    links = link_list(tweet)
    if links is False:
        return "Found no images in this tweet."

    new_image_name = f"static/tweets/{tweet_id}.png"

    for itr, link in enumerate(links, start=1):
        response = requests.get(link)
        with open(f"static/tweets/{itr}.jpg", "wb") as file:
            file.write(response.content)

        thumb = ImageOps.fit(
            Image.open(f"static/tweets/{itr}.jpg"), (512, 512), Image.ANTIALIAS
        )
        thumb.save(f"static/tweets/{itr}.png")
        os.remove(f"static/tweets/{itr}.jpg")

    image1 = "static/tweets/1.png"
    image2 = "static/tweets/2.png"
    image3 = "static/tweets/3.png"
    image4 = "static/tweets/4.png"

    if len(links) == 1:
        return "There is only one images in this tweet. No need to use this api for that :)"

    if len(links) == 2:
        imgs = list(map(Image.open, (image1, image2)))
        new_im = Image.new("RGB", (1024, 512))

        x_offset = 0
        for img in imgs:
            new_im.paste(img, (x_offset, 0))
            x_offset += img.size[0]
        new_im.save(new_image_name)
        os.remove(f"{image1}")
        os.remove(f"{image2}")
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }

    if len(links) == 3:
        imgs = list(map(Image.open, (image1, image2, image3)))
        new_im = Image.new("RGB", (1536, 512))

        x_offset = 0
        for img in imgs:
            new_im.paste(img, (x_offset, 0))
            x_offset += img.size[0]

        os.remove(f"{image1}")
        os.remove(f"{image2}")
        os.remove(f"{image3}")
        new_im.save(new_image_name)
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }

    if len(links) == 4:
        imgs = list(map(Image.open, (image1, image2, image3, image4)))
        new_im = Image.new("RGB", (1024, 1024))

        new_im.paste(imgs[0], (0, 0))
        new_im.paste(imgs[1], (512, 0))
        new_im.paste(imgs[2], (0, 512))
        new_im.paste(imgs[3], (512, 512))
        new_im.save(new_image_name)
        os.remove(f"{image1}")
        os.remove(f"{image2}")
        os.remove(f"{image3}")
        os.remove(f"{image4}")
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }


@ app.route("/add")
def add():
    tweet_id = request.args.get('tweet_id', default=1, type=int)
    print(f"Add: Tweet ID: {tweet_id}")
    if tweet_id == 1:
        return "Please add correct tweet id, e.g https://twitter.lovinator.space/add?tweet_id=1197649654785069057"

    if os.path.isfile(f"static/tweets/{tweet_id}.png"):
        print(f"{tweet_id} is already converted.")
        return {
            "url": f"{url}/static/tweets/{tweet_id}.png",
        }
    else:
        hook.send(
            f"{request.remote_addr} made image for https://twitter.com/i/status/{tweet_id}")
        return download_images(tweet_id)


@ app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
