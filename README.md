# twitter-image-collage-maker

`twitter-image-collage-maker` combines several images in tweets into one.
It runs a website that downloads images from a Tweet, combines them into a 2x1, 3x1 and 2x2 and returns the new combined image. This program was made for [TheLovinator1/discord-twitter-webhooks](https://github.com/TheLovinator1/discord-twitter-webhooks).

## Before

<p float="left">
<img alt="Before1" src="img\EJ7n4pfU0AE6gUg.jpg" width="15%" height="15%">
<img alt="Before2" src="img\EJ7n4pfU4AARDwj.jpg" width="15%" height="15%">
<img alt="Before3" src="img\EJ7n4pfVUAA9kHQ.jpg" width="15%" height="15%">
<img alt="Before4" src="img\EJ7n4pfVUAEJskS.jpg" width="15%" height="15%">
</p>

## After

<img alt="After1" src="img\1197649654785069057.jpg" width="15%" height="15%">

---

## Public version

[https://twitter.lovinator.space/](https://twitter.lovinator.space/)

## Config file

Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and apply for Elevated API access to get the V1 API keys. After you have applied you can go to Projects & Apps -> Create App under Standalone Apps

| Config              | Description                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| webhook_url         | Right click channel you want tweets in -> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL.                                                 |
| api_key             | Twitter API key.                                                                                                                                       |
| api_key_secret      | Twitter API Secret Key.                                                                                                                                |
| access_token        | Twitter Access Token.                                                                                                                                  |
| access_token_secret | Twitter Access Token Secret.                                                                                                                           |
| url                 | Domain for website. Discord needs to access this. Return image will look like `https://twitter.lovinator.space/static/tweets/1197649654785069057.png`. |
| discord_id          | User that should be pinged when something goes wrong.                                                                                                  |
| static_location     | Path to folder where images are stored. Defaults to C:\ProgramData\ on Windows and /usr/share on Linux.                                                |

## Need help?

- Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
- Discord: TheLovinator#9276
- Steam: [TheLovinator](https://steamcommunity.com/id/TheLovinator/)
- Send an issue: [twitter-image-collage-maker/issues](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
- GitHub Discussions: [twitter-image-collage-maker/discussions](https://github.com/TheLovinator1/twitter-image-collage-maker/discussions)
