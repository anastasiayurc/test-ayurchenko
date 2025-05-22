import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"
HEADERS = {"Content-Type": "application/json"}
PET_ID = 123456

@pytest.fixture(scope="module")
def pet_payload():
    return {
        "id": PET_ID,
        "name": "Fluffy",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["http://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    }

def test_create_pet_positive(pet_payload):
    resp = requests.post(BASE_URL, json=pet_payload, headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json()["name"] == "Fluffy"