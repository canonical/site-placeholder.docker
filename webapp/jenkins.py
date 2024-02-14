import ast
import requests
from datetime import datetime


class Jenkins:

    def __init__(self, app=None):
        JENKINS_URL = app.config["JENKINS_URL"]
        self.app = app
        self.job_path = app.config["BUILD_URL"].split(".com")[1]
        self.jenkins_job_url = f"http://{JENKINS_URL}{self.job_path}"
        self.info = self.__get_job_info__()

    def __get_job_info__(self):
        url = f"{self.jenkins_job_url}api/python"
        response = requests.get(url)
        return ast.literal_eval(response.text)

    def get_job_logs(self):
        url = f"{self.jenkins_job_url}consoleText"
        response = requests.get(url)
        return response.text

    def get_demo_name(self):
        gh_url = self.info["actions"][0]["parameters"][0]["value"]
        domain, pr_no = gh_url.split("canonical/")[1].split("/pull/")
        domain = domain.replace(".", "-")
        return f"{domain}-{pr_no}.demos.haus"

    def get_pr_info(self):
        return self.info["actions"][0]["parameters"][0]["value"]

    def get_start_time(self):
        return datetime.fromtimestamp(self.info["timestamp"] / 1000).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def restart_build(self):
        JENKINS_URL = self.app.config["JENKINS_URL"]
        requests.post(
            f"http://{JENKINS_URL}/webteam/start-demo/buildWithParameters",
            data={
                "PR_URL": self.get_pr_info(),
                "token": self.app.config["JENKINS_TOKEN"],
            },
        )
        return "OK"
