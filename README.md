# This project has been archived and is no longer maintained.

The Twitter API is dead now after Elon Musk bought Twitter. So this project is now broken and will not be fixed. Thanks for the fish. 🐟

## twitter-image-collage-maker

`twitter-image-collage-maker` combines several images in tweets into one.
It runs a website that downloads images from a Tweet, combines them into a 2x1, 3x1 and 2x2 and returns the new combined
image. This program was made
for [TheLovinator1/discord-twitter-webhooks](https://github.com/TheLovinator1/discord-twitter-webhooks).

## Before

<p float="left">
<img alt="Before1" src="img/EJ7n4pfU0AE6gUg.jpg" width="15%" height="15%">
<img alt="Before2" src="img/EJ7n4pfU4AARDwj.jpg" width="15%" height="15%">
<img alt="Before3" src="img/EJ7n4pfVUAA9kHQ.jpg" width="15%" height="15%">
<img alt="Before4" src="img/EJ7n4pfVUAEJskS.jpg" width="15%" height="15%">
</p>

## After

<img alt="After1" src="img/1197649654785069057.jpg" width="15%" height="15%">


## Config file

Create an app and copy your bearer token.

| Config          | Description                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WEBHOOK_URL     | Right click channel you want tweets in -> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL.                                                      |
| BEARER_TOKEN    | <https://developer.twitter.com/en/portal/> - Fill out your information and accept the developer agreement & policy, create an app and copy your bearer token. |
| URL             | Domain for website. Discord needs to access this.                                                                                                           |
| DISCORD_ID      | User that should be pinged when something goes wrong.                                                                                                       |
| STATIC_LOCATION | Path to folder where images are stored. Docker users should use `/usr/share/twitter-image-collage-maker/`                                                   |

## Need help?

- Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
- Discord: TheLovinator#9276
- Send an
  issue: [twitter-image-collage-maker/issues](https://github.com/TheLovinator1/twitter-image-collage-maker/issues)
