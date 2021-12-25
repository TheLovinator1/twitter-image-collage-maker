# twitter-image-collage-maker

`twitter-image-collage-maker` combines several images in tweets into one.
It runs a website that downloads images from a Tweet, combines them into a 2x1, 3x1 and 2x2 and returns the new combined image. This program was made for [TheLovinator1/discord-twitter-webhooks](https://github.com/TheLovinator1/discord-twitter-webhooks).

## Before

<p float="left">
<img alt="Before1" src="extras\img\EJ7n4pfU0AE6gUg.jpg" width="15%" height="15%">
<img alt="Before2" src="extras\img\EJ7n4pfU4AARDwj.jpg" width="15%" height="15%">
<img alt="Before3" src="extras\img\EJ7n4pfVUAA9kHQ.jpg" width="15%" height="15%">
<img alt="Before4" src="extras\img\EJ7n4pfVUAEJskS.jpg" width="15%" height="15%">
</p>

## After

<img alt="After1" src="extras\img\1197649654785069057.jpg" width="15%" height="15%">

---

## Public version

[https://twitter.lovinator.space/](https://twitter.lovinator.space/)

## Installation

These steps are work in progress. Issues and pull requests welcome. You will get the grasp of how to use it. The steps are not perfect. You can use the public version of the bot if you get stuck. Or ask be for help on Discord/Steam/GitHub.

- Install latest version of Python 3, Poetry and Nginx
- Download project from GitHub and change directory into it
- Install requirements
  - `poetry install`
- Copy twitter.service and twitter.socket to /etc/systemd/system/
  - `sudo cp twitter.service /etc/systemd/system/`
- There is a example file for nginx. Change it to your needs.
  - `sudo cp nginx.conf /etc/nginx/`
- Restart nginx:
  - `sudo systemctl enable --now nginx`
- Check what user is running Nginx, Arch is using `http`. Others could be `www-data`:
  - `ps aux | grep nginx`
- Change permissions for the directory. Change lovinator to your username:
  - `sudo chown -R lovinator:http /static`
- Create log folder
  - `sudo mkdir /var/log/twitter`
- Change permissions to your user
  - `sudo chown -R lovinator:lovinator /var/log/twitter`
- Start the service:
  - `sudo systemctl enable --now twitter.service`
  - `sudo systemctl enable --now twitter.socket`
- Check if it is running:
  - `sudo systemctl status twitter.service`
- Check logs if something went wrong:
  - `cat /var/log/twitter/error.log` and `cat /var/log/twitter/access.log`
- If everything is working you should be able to see the site in your browser

## Config file

Right click channel you want the tweets in -> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL

- webhook_url = https://discordapp.com/api/webhooks/582694/a3hmHAXItB_lzSYBx0-CeVeUDqac1vT

Go to [Twitter](https://developer.twitter.com/en/portal/apps/new) and create an app.

- api_key = ASFkopkoasfPOFkopaf
- api_key_secret = ASFkopkoasfPOFkopafASFkopkoasfPOFkopafASFkopkoasfPOFkopaf
- access_token = 1294501204821094-kKPOASPKOFpkoaskfpo
- access_token_secret = ASKOpokfpkoaspofOPFPO2908iAKOPSFKPO

Domain for website. Discord needs to access this. Return image will look like `https://twitter.lovinator.space/static/tweets/1197649654785069057.png`

- url = https://twitter.lovinator.space/

Hide IP in webhook notification

- hidden_ip = True

The Discord id that should be pinged when something goes wrong. It can be found by typing \\@YourUsername in Discord.

- discord_id = 126462229892694018

</details>

## Need help?

- Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
- Discord: TheLovinator#9276
- Steam: [TheLovinator](https://steamcommunity.com/id/TheLovinator/)
- Send an issue: [twitter-image-collage-maker/issues](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
- GitHub Discussions: [twitter-image-collage-maker/discussions](https://github.com/TheLovinator1/twitter-image-collage-maker/discussions)
