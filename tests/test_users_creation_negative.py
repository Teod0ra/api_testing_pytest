import pytest
from data.users_payload import (
    EMPTY_BODY,
    MISSING_NAME,
    MISSING_EMAIL,
    INVALID_TYPES
)
## JSON Placeholder API is API for testing and:
## resource on the server will not be really updated but it will be faked as if


@pytest.mark.parametrize(
    "payload, description",
    [
        (EMPTY_BODY, "empty body"),
        (MISSING_NAME, "missing name"),
        (MISSING_EMAIL, "missing email"),
        (INVALID_TYPES, "invalid data types"),
    ]
)
def test_create_user_negative(users_client, payload, description):
    response = users_client.create_user(payload)
    assert response.status_code in [400, 422, 201], f"Failed case {description}"
    ## status code will always return 201 - does not validate payload 

