from fastapi.testclient import TestClient

from twitter_image_collage_maker.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_add():
    response = client.get("/add?tweet_id=1197649654785069057")
    assert response.status_code == 200
