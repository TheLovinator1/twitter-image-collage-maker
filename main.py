import os
from flask import Flask, request
import requests
import tweepy
from PIL import Image, ImageOps
from dotenv import load_dotenv
app = Flask(__name__, static_folder="tweets")


def link_list(tweet):
    link_list = []
    if "media" in tweet.entities:
        for media in tweet.extended_entities["media"]:
            link = media["media_url_https"]
            link_list.append(link)

    if len(link_list) > 1:
        return link_list


def download_images(tweet_id):
    if tweet_id == 1:
        return
    tweet = api.get_status(tweet_id)

    links = link_list(tweet)
    new_image_name = f"tweets/{tweet_id}.png"

    for itr, link in enumerate(links, start=1):
        response = requests.get(link)
        with open(f"tweets/{itr}.jpg", "wb") as file:
            file.write(response.content)

        thumb = ImageOps.fit(
            Image.open(f"tweets/{itr}.jpg"), (512, 512), Image.ANTIALIAS
        )
        thumb.save(f"tweets/{itr}.png")
        os.remove(f"tweets/{itr}.jpg")

    image1 = "tweets/1.png"
    image2 = "tweets/2.png"
    image3 = "tweets/3.png"
    image4 = "tweets/4.png"

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

    elif len(links) == 3:
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

    elif len(links) == 4:
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

    return str(new_image_name)


@ app.route("/add")
def add():
    tweet_id = request.args.get('tweet_id', default=1, type=int)
    tweet = download_images(tweet_id=tweet_id)

    return {
        "url": f"{url}/{tweet}",
    }


@ app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    load_dotenv(verbose=True)

    url = os.environ["URL"]
    auth = tweepy.OAuthHandler(
        os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(
        os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)

    if not os.path.isdir(f"tweets"):
        os.mkdir(f"tweets")

    app.run(debug=True)
