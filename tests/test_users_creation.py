from data.users_payload import (
    VALID_USER
)
## JSON Placeholder API is API for testing and:
## resource on the server will not be really updated but it will be faked as if
## status code will always return 201 - does not validate payload

def test_create_user(users_client):
    response = users_client.create_user(VALID_USER)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == VALID_USER["name"]
    assert data["username"] == VALID_USER["username"]
    assert data["email"] == VALID_USER["email"]
    assert "id" in data
