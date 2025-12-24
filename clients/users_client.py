import requests
from config.settings import BASE_URL, TIMEOUT

class UsersClient:
    def get_users(self):
        return requests.get(f"{BASE_URL}/users", timeout=TIMEOUT)

    def get_user_by_id(self, user_id):
        return requests.get(f"{BASE_URL}/users/{user_id}", timeout=TIMEOUT)