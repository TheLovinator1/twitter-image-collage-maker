def link_list(tweet):
    """Generate a list with all the images in the tweet."""
    link_list = []
    if "media" in tweet.entities:
        link_list.extend(
            media["media_url_https"] for media in tweet.extended_entities["media"]
        )

    return link_list
