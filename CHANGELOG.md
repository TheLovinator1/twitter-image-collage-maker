# Changelog

All notable changes to twitter-image-collage-maker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2022-01-16

### Added

- Update dependencies.
- Change line-length to 119 characters.
- Move @username to beginning of error message.
- Add example and summary to documentation.
- Update license in pyproject.toml.
- Make docstrings shorter.
- If URL ends with a slash remove it so we don't get two.
- Move exception handling to main.py.
- Use /usr/share instead of /home/.
- Fix systemd service file.
- Change discord_username to discord_id to show that it needs ID instead of username.
- Move images to extras folder and update README.md.
- Use config file instead of environment variables.
- Change license to GPLv3.
- Move Python files to own folder and functions to own file.
- Move example files to extras folder.
- Use FastAPI instead of Flask.

## [0.1.0] - 2021-12-05

### Added

- Use Poetry.
- Add WIP guide in README for using twitter-image-collage-maker with Nginx.
- Add example files for systemd service and nginx config.
- Use tmpdir to store temp images.
- Send errors to Discord and ping owner.
- Add images to README.md.
- Fixed tweets that are extended.
- Get IP address of the user who uploaded the image and send to Discord.
- Check if image exists before remaking it.
