import pytest
from api.projects_api import ProjectsAPI
import random
import string

def random_title():
    return "Proj-" + "".join(random.choices(string.ascii_letters, k=6))

@pytest.fixture
def api():
    return ProjectsAPI()

@pytest.fixture
def new_project(api):
    payload = {
        "title": random_title(),
        "users": {
            "user_id": "admin"
        }
    }
    response = api.create_project(payload)
    print(response.json())
    assert response.status_code == 201
    return response.json()["id"]
