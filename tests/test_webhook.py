from twitter_image_collage_maker.webhooks import send_webhook


def test_send_webhook():
    result = send_webhook("Hello, just running Pytest :-)")
    assert result.status_code == 200
    assert result.ok
