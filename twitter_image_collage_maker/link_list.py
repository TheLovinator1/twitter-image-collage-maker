def link_list(tweet):
    """Generate a list with all the images in the tweet."""
    links = []
    if "media" in tweet.entities:
        links.extend(
            media["media_url_https"] for media in tweet.extended_entities["media"]
        )

    return links
