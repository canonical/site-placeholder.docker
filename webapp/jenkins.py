import ast
import requests


class Jenkins:
    def __init__(self, jenkins_job_url):
        self.jenkins_job_url = jenkins_job_url
        self.info = self.__get_job_info__(jenkins_job_url)

    def __get_job_info__(self, url):
        url = f"{url}api/python"
        response = requests.get(url)
        return ast.literal_eval(response.text)

    def get_job_logs(self):
        url = f"{self.jenkins_job_url}consoleText"
        response = requests.get(url)
        return ast.literal_eval(response.text)
