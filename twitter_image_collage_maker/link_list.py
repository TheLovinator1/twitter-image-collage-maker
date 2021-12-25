def link_list(tweet):
    """Generate a list with all the images in the tweet."""
    link_list = []
    if "media" in tweet.entities:
        for media in tweet.extended_entities["media"]:
            link = media["media_url_https"]
            link_list.append(link)

    return link_list
