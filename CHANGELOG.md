# Changelog

All notable changes to twitter-image-collage-maker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Use WebP instead of PNG when saving files to minimize file size.
- Updated dependencies (1 install, 6 updates, 0 removals).
  - Updating charset-normalizer (2.0.9 -> 2.0.10)
  - Updating urllib3 (1.26.7 -> 1.26.8)
  - Updating anyio (3.4.0 -> 3.5.0)
  - Updating requests (2.26.0 -> 2.27.1)
  - Updating gitpython (3.1.24 -> 3.1.26)
  - Installing types-urllib3 (1.26.7)
  - Updating types-requests (2.26.3 -> 2.27.7)
  - Updating pillow (8.4.0 -> 9.0.0)
  - Updating uvicorn (0.16.0 -> 0.17.0)
  - Updating starlette (0.16.0 -> 0.17.1)
  - Updating fastapi (0.70.1 -> 0.71.0)
- Updated developer dependencies (0 installs, 1 update, 0 removals)
  - Updating mypy (0.930 -> 0.931)

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
