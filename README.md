# twitter-image-collage-maker

`twitter-image-collage-maker` combines several images in tweets into one.
It runs a website that downloads images, combines them into a 2x1, 3x1 and 2x2 and returns the new combined image. This program was made for https://github.com/TheLovinator1/discord-twitter-webhooks.

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

</details>
<details>
<summary><b>Get twitter-image-collage-maker with <code>docker cli</code></b></summary><br/><br/>

```console
docker run -d \
  --name=twitter-image-collage-maker \
  -e WEBHOOK_URL=https://discord.com/api/webhooks/151256151521/Drw1jBO9Xyo1hAVsvaNdI1d077dOsfsafAV-nxIDvH-XJeSIeAVavasvkM0Vu \
  -e CONSUMER_KEY=akaopspokfpofasfsaf \
  -e CONSUMER_SECRET=fsa0fskaopfsoapfkofskaopfskopafskopaf \
  -e ACCESS_TOKEN=1521521515-JeASFAd0cGtASifvSSaSFmIr4kopAw8V0oyiH6jN \
  -e ACCESS_TOKEN_SECRET=VlHAS12FYqkQdASFd5XvyunwPaS12F8zPMTZ6IZASF1No \
  -e URL=https://twitter.lovinator.space/ \
  -e DISABLE_IP=True \
  --restart unless-stopped \
  thelovinator/twitter-image-collage-maker
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

</details>
<details>
<summary><b>Get twitter-image-collage-maker with <code>Python</code> with <code>pip</code></b></summary>

* Install latest version of Python 3 for your operating system
* Download project from GitHub and change directory into it
* (Optional) Create virtual environment:
  * `python -m venv .venv`
    * Activate virtual environment:
      * Windows:  `.\.venv\Scripts\activate`
      * Not windows:  `source .venv/bin/activate`
* Install requirements
  * `pip install -r requirements.txt`
* Rename .env.example to .env and fill it with things from [Twitter](https://developer.twitter.com). If you don't want to use the .env-file you can add variables to your environment.
* Start the bot (inside the activated virtual environment if you made one):
  * `python main.py`

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

</details>

## Need help?

* Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
* Discord: TheLovinator#9276
* Steam: [TheLovinator](https://steamcommunity.com/id/TheLovinator/)
* Send an issue: [twitter-image-collage-maker/issues](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
* GitHub Discussions: [twitter-image-collage-maker/discussions](https://github.com/TheLovinator1/twitter-image-collage-maker/discussions)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
