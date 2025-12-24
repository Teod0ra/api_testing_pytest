from utils.assertions import *
import pytest


def test_get_users(users_client):
    required_fields = ["id", "name", "email"]
    response = users_client.get_users()
    assert_status_code(response)

    users = response.json()
    assert_not_empty(users)
    assert_required_fields(users, required_fields=required_fields)


@pytest.mark.parametrize("field", [
    "id", "name", "email"
])
def test_required_fields_are_not_empty(users_client, field):
    response = users_client.get_users()
    for user in response:
        assert user[field], f"{field} field is required field and should not be empty"


@pytest.mark.parametrize("field", [
    "name", "username", "email"
])
def test_str_fields(users_client, field):
    response = users_client.get_users()
    for user in response:
        assert isinstance(user[field], str), f"{field} should be String."
