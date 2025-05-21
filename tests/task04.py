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

def test_create_pet_negative():
    # Missing required fields
    resp = requests.post(BASE_URL, json={"id": PET_ID + 1}, headers=HEADERS)
    assert resp.status_code != 200

def test_get_pet_positive():
    resp = requests.get(f"{BASE_URL}/{PET_ID}")
    assert resp.status_code == 200
    assert resp.json()["id"] == PET_ID

def test_get_pet_negative():
    resp = requests.get(f"{BASE_URL}/99999999")
    assert resp.status_code == 404

def test_update_pet_positive(pet_payload):
    pet_payload["name"] = "FluffyUpdated"
    pet_payload["status"] = "sold"
    resp = requests.put(BASE_URL, json=pet_payload, headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json()["name"] == "FluffyUpdated"

def test_update_pet_negative():
    # Invalid data
    resp = requests.put(BASE_URL, json={"id": "not-a-number", "name": ""}, headers=HEADERS)
    assert resp.status_code != 200

def test_delete_pet_positive():
    resp = requests.delete(f"{BASE_URL}/{PET_ID}")
    assert resp.status_code == 200

def test_delete_pet_negative():
    resp = requests.delete(f"{BASE_URL}/99999999")
    assert resp.status_code == 404