import config
import requests


class YougileProject:

    def __init__(self, url):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {config.TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        body = {
            "title": title,
        }
        resp = requests.post(f"{self.url}/api-v2/projects", json=body,
                             headers=self.headers)
        return resp

    def update_project(self, project_id, new_title, deleted=False):
        body = {
            "deleted": deleted,
            "title": new_title
        }
        resp = requests.put(f"{self.url}/api-v2/projects/{project_id}",
                            json=body, headers=self.headers)
        return resp

    def get_project_by_id(self, project_id):
        resp = requests.get(f"{self.url}/api-v2/projects/{project_id}",
                            headers=self.headers)
        return resp
