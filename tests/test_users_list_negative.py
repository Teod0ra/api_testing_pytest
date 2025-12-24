from utils.assertions import *
import pytest


@pytest.mark.parametrize("user_id", ["abc", "!@#", -1, 0, 999999])
def test_user_invalid_ids(users_client, user_id):
    response = users_client.get_user_by_id(user_id)
    assert response.status_code in [400, 404]

