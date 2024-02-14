import ast
import requests
from datetime import datetime


class Jenkins:

    def __init__(self, app=None):
        self.jenkins_url = app.config.get("JENKINS_URL") or "localhost"
        self.jenkins_token = app.config.get("JENKINS_TOKEN")
        self.job_path = app.config.get("BUILD_URL").split(".com")[1]
        self.jenkins_job_url = f"http://{self.jenkins_url}{self.job_path}"
        self.info = self.__get_job_info__()

    def __get_job_info__(self):
        url = f"{self.jenkins_job_url}api/python"
        response = requests.get(url)
        info = ast.literal_eval(response.text)
        info["gh_url"] = self.__get_pr_info__(info)
        return info

    def __get_pr_info__(self, info):
        for action in info["actions"]:
            if "parameters" in action:
                for param in action["parameters"]:
                    if "PR_URL" in param["name"]:
                        return param["value"]
        return "No PR URL found"

    def get_job_logs(self):
        url = f"{self.jenkins_job_url}consoleText"
        response = requests.get(url)
        return response.text

    def get_demo_name(self):
        domain, pr_no = self.info["gh_url"].split("canonical/")[1].split("/pull/")
        domain = domain.replace(".", "-")
        return f"{domain}-{pr_no}.demos.haus"

    def get_start_time(self):
        return datetime.fromtimestamp(self.info["timestamp"] / 1000).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def restart_build(self):
        requests.post(
            f"http://{self.jenkins_url}/webteam/start-demo/buildWithParameters",
            data={
                "PR_URL": self.info["gh_url"],
                "token": self.jenkins_token,
            },
        )
        return "OK"
