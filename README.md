
# API Test Framework

This project demonstrates a simple API test framework using Python, pytest, and requests targeting the public API:

https://jsonplaceholder.typicode.com/users

The goal is to test positive and negative API requests, using parametrization.

### Tech Stack
- Python 3.10+
- pytest
- requests

# Project structure
```text
├── clients/
│   └── users_client.py        # API client
├── config/
│   └── settings.py      # Base url, configs
├── data/
│   └── users_payloads.py      # Test payloads
├── tests/
│   └── test_users_creation_negative.py     # Negative tests for POST endpoint
│   └── test_users_creation.py     # Positive tests for POST endpoint
│   └── test_users_list_negatie.py     # Negative tests for GET endpoint
│   └── test_users_list.py     # Postive testsfor GET endpoint
├── utils/
│   └── assertions.py  #Assertions helpers
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

### Test Cases –  /users

| Test ID | Test Type | Scenario | Request / Payload | Expected Result |
|---------|----------|---------|-----------------|----------------|
| TC-01   | Positive | Create user with valid payload | POST /users: name, username, email | 201 Created, user ID returned |
| TC-02   | Negative | Create user with empty body | POST /users: `{}` | 400 / 422 (validation error) |
| TC-03   | Negative | Missing required field: name | POST /users: email only | 400 / 422 |
| TC-04   | Negative | Missing required field: email | POST /users: name only | 400 / 422 |
| TC-05   | Negative | Invalid data types | POST /users: name as number, email as boolean | 400 / 422 |
| TC-06   | Positive | Get all users | GET /users | 200 OK, list of users, each has id, name, email |
| TC-07   | Positive | Get user by valid ID | GET /users/1 | 200 OK, user object has id, name, email |
| TC-08   | Negative | Get user by invalid ID | GET /users/invalid | 404 Not Found |

## How to Write Tests

This framework uses **pytest** along with **API clients** (`UsersClient`) and **helper functions** (`assertions.py`) to organize tests efficiently. Follow these guidelines:


### Folder & File Structure

- Place tests in the `tests/` folder.
- Name test files starting with `test_`, e.g., `test_users_post.py`.
- Test classes and functions should also start with `Test` and `test_`, respectively.
- Use `data/` for payloads and `config/settings.py` for base URLs and headers.

### Parametrized Tests

- Use pytest.mark.parametrize for multiple inputs in one test function:
```bash
@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),      # existing user
    (9999, 404),   # non-existent user
])
```
### Best Practices

- Name test functions descriptively, e.g., test_create_user_missing_email.

- Separate positive and negative tests.

- Keep payloads, settings, and assertions in dedicated files.

- Parametrize where possible to reduce code duplication.

- Include clear validation checks: status code, response type, required fields.

## How to Run Tests
This framework uses **pytest** for running API tests. Follow the instructions below to execute tests locally.

Make sure you have **Python 3.10+** installed. Then install required packages:

```
pip install -r requirements.txt
````

**!** It’s recommended to use a virtual environment to avoid conflicts with system packages.
#### Create virtual environment
```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
````
After activation, your terminal should show 
(venv) at the beginning of the prompt.

#### Install dependencies
````bash
pip install --upgrade pip
pip install -r ./requirements.txt
````
This will install **python, requiests** and other required packages inside the virtual environment.

#### Run all tests
````bash
pytest -v
````
**-v** stands for v**erbose** showing detailed test results.
#### Run specific tests
- Run only POST tests
````bash
pytest -k "users_creation" -v
````
- Run only GET tests
````bash
pytest -k "users_list" -v
````