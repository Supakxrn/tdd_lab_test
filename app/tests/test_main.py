from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_call_name_jonancy():
    name = "Jonancy"
    url = "/callname/{name}"
    response = client.get(url)
    expected_result = {"hello": "Jonancy"}
    assert response.status_code == 200
    assert response.json() == expected_result

def test_post_call_name_paipibut():
    name = "Paipibut"
    url = "/callname"
    response = client.post(url)
    expected_result = {"hello": "Paipibut"}
    assert response.status_code == 200
    assert response.json() == expected_result
