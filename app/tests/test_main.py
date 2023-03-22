from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_call_name_jonancy():
    name = "Jonancy"
    url = "/callname/"+name
    response = client.get(url)
    expected_result = {"hello": name}
    assert response.status_code == 200
    assert response.json() == expected_result
