def assert_status_code(response, expected=200):
    assert response.status_code == expected,  f"Expected {expected} status code, but got {response.status_code} status code"


def assert_not_empty(data):
    assert data, "Response data is empty"


def assert_required_fields(data, required_fields):
    for user in data:
        for field in required_fields:
            assert field in user, "Missing field: {field}"
