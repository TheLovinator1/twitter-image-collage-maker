from fastapi.testclient import TestClient
from httpx import Response

from twitter_image_collage_maker.main import app

client: TestClient = TestClient(app)


def test_read_main() -> None:
    response: Response = client.get("/")
    assert response.status_code == 200


def test_add() -> None:
    response: Response = client.get("/add?tweet_id=1197649654785069057")
    assert response.status_code == 200
