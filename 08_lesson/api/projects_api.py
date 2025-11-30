import requests
from settings import BASE_URL, TOKEN

class ProjectsAPI:

    def __init__(self):
        self.base = f"https://ru.yougile.com/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer #{token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload):
        return requests.post(self.base, json=payload, headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(f"{self.base}/{project_id}", json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base}/{project_id}", headers=self.headers)