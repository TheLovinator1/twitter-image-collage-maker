# twitter-image-collage-maker

`twitter-image-collage-maker` combines several images in tweets into one.
It runs a website that downloads images from a Tweet, combines them into a 2x1, 3x1 and 2x2 and returns the new combined image. This program was made for https://github.com/TheLovinator1/discord-twitter-webhooks.

## Before

<p float="left">
<img alt="Before1" src="static\img\EJ7n4pfU0AE6gUg.jpg" width="15%" height="15%">
<img alt="Before2" src="static\img\EJ7n4pfU4AARDwj.jpg" width="15%" height="15%">
<img alt="Before3" src="static\img\EJ7n4pfVUAA9kHQ.jpg" width="15%" height="15%">
<img alt="Before4" src="static\img\EJ7n4pfVUAEJskS.jpg" width="15%" height="15%">
</p>

## After

<img alt="After1" src="static\img\1197649654785069057.png" width="15%" height="15%">

---

## Public version

https://twitter.lovinator.space/

## Installation

*(click to expand the sections below for full setup instructions)*

<details>
<summary><b>Get twitter-image-collage-maker with <code>docker-compose</code></b></summary><br/><br/>

docker-compose.yml:

```yaml
version: "3"
services:
  twitter-image-collage-maker:
    image: thelovinator/twitter-image-collage-maker
    env_file:
      - .env
    container_name: twitter-image-collage-maker
    environment:
      - CONSUMER_KEY=${CONSUMER_KEY}
      - CONSUMER_SECRET=${CONSUMER_SECRET}
      - ACCESS_TOKEN=${ACCESS_TOKEN}
      - ACCESS_TOKEN_SECRET=${ACCESS_TOKEN_SECRET}
      - URL=${URL}
      - WEBHOOK_URL=${WEBHOOK_URL}
      - DISABLE_IP=${DISABLE_IP}
      - DISCORD_ID=${DISCORD_ID}
    ports:
      - "5000:5000"
    volumes:
      - tweet_images:/home/botuser/static/tweets
    restart: unless-stopped
volumes:
  tweet_images:
```

This bot on [Docker Hub](https://hub.docker.com/r/thelovinator/twitter-image-collage-maker).

## Environment variables

No space should be between the equal sign in your .env.

Right click channel you want the tweets in -> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL

* WEBHOOK\_URL=https://discordapp.com/api/webhooks/582694/a3hmHAXItB_lzSYBx0-CeVeUDqac1vT

Go to [Twitter](https://developer.twitter.com/en/portal/apps/new) and create an app. If you don't get one try to fill out as much as possible. After it is created go to Keys and tokens. CONSUMER_KEY = API key, CONSUMER_SECRET = API key secret:

* CONSUMER\_KEY=ASFkopkoasfPOFkopaf
* CONSUMER\_SECRET=ASFkopkoasfPOFkopafASFkopkoasfPOFkopafASFkopkoasfPOFkopaf
* ACCESS\_TOKEN=1294501204821094-kKPOASPKOFpkoaskfpo
* ACCESS\_TOKEN\_SECRET=ASKOpokfpkoaspofOPFPO2908iAKOPSFKPO

Domain for website. Discord needs to access this.

* URL=https://twitter.lovinator.space/

Hide IP in webhook notification

* DISABLE_IP=True

The Discord id that should be pinged when something goes wrong. It can be found by typing \\@YourUsername in Discord.

* DISCORD_ID=126462229892694018

</details>
<details>
<summary><b>Install twitter-image-collage-maker locally on your computer behind Nginx</b></summary>

These steps are work in progress. Issues and pull requests welcome. You will get the grasp of how to use it. The steps are not perfect. You can use the public version of the bot if you get stuck. Or ask be for help on Discord/Steam/GitHub.
* Install latest version of Python 3 and nginx
* Download project from GitHub and change directory into it
* Create virtual environment:
  * `python -m venv .venv`
  * Activate virtual environment:
    * `source .venv/bin/activate`
* Install requirements
  * `pip install -r requirements.txt`
* Rename .env.example to .env and fill it with things from [Twitter](https://developer.twitter.com). You also have to uncomment STATIC_LOCATION and change it to the path where you want the images to be saved. We will use /static in this example.
* Copy twitter.service and twitter.socket to /etc/systemd/system/:
  * `sudo cp twitter.service /etc/systemd/system/`

* There is a example file for nginx. Change it to your needs.
  * `sudo cp nginx.conf /etc/nginx/`
* Restart nginx:
  * `sudo systemctl enable --now nginx`
* Create directory for images:
  * `sudo mkdir /static`
* Check what user is running Nginx, Arch is using `http`. Others could be `www-data`:
  * `ps aux | grep nginx`
* Change permissions for the directory. Change lovinator to your username:
  * `sudo chown -R lovinator:http /static`
* Create log folder
  * `sudo mkdir /var/log/twitter`
* Change permissions to your user
  * `sudo chown -R lovinator:lovinator /var/log/twitter`
* Start the service:
  * `sudo systemctl enable --now twitter.service`
  * `sudo systemctl enable --now twitter.socket`
* Check if it is running:
  * `sudo systemctl status twitter.service`
* Check logs if something went wrong:
  * `cat /var/log/twitter/error.log` and `cat /var/log/twitter/access.log`
* If everything is working you should be able to see the site in your browser

## Environment variables

No space should be between the equal sign in your .env.

Right click channel you want the tweets in -> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL

* WEBHOOK\_URL=https://discordapp.com/api/webhooks/582694/a3hmHAXItB_lzSYBx0-CeVeUDqac1vT

Go to [Twitter](https://developer.twitter.com/en/portal/apps/new) and create an app. If you don't get one try to fill out as much as possible. After it is created go to Keys and tokens. CONSUMER_KEY = API key, CONSUMER_SECRET = API key secret:

* CONSUMER\_KEY=ASFkopkoasfPOFkopaf
* CONSUMER\_SECRET=ASFkopkoasfPOFkopafASFkopkoasfPOFkopafASFkopkoasfPOFkopaf
* ACCESS\_TOKEN=1294501204821094-kKPOASPKOFpkoaskfpo
* ACCESS\_TOKEN\_SECRET=ASKOpokfpkoaspofOPFPO2908iAKOPSFKPO

Domain for website. Discord needs to access this.

* URL=https://twitter.lovinator.space/

Hide IP in webhook notification

* DISABLE_IP=True

The Discord id that should be pinged when something goes wrong. It can be found by typing \\@YourUsername in Discord.

* DISCORD_ID=126462229892694018

</details>

## Need help?

* Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
* Discord: TheLovinator#9276
* Steam: [TheLovinator](https://steamcommunity.com/id/TheLovinator/)
* Send an issue: [twitter-image-collage-maker/issues](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
* GitHub Discussions: [twitter-image-collage-maker/discussions](https://github.com/TheLovinator1/twitter-image-collage-maker/discussions)