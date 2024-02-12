from datetime import datetime

from flask import Flask, render_template

from webapp import create_app
from webapp.jenkins import Jenkins

app = create_app()


@app.route("/_status")
def status():
    return "OK"


@app.route("/")
def index():
    jenkins = Jenkins(app.config["BUILD_URL"])
    start_time = datetime.fromtimestamp(jenkins.info["timestamp"] / 1000)
    build_url = jenkins.info["url"]
    job_status = jenkins.info["result"]
    is_building = jenkins.info["inProgress"]
    gh_url = jenkins.info["actions"][0]["parameters"][0]["value"]
    domain, pr_no = "https://github.com/canonical/ubuntu.com/pull/13570".split(
        "canonical/"
    )[1].split("/pull/")
    domain = domain.replace(".", "-")
    demo_name = f"{domain}-{pr_no}.demos.haus"
    logs = jenkins.get_job_logs()

    return render_template(
        "index.html",
        build_url=build_url,
        gh_url=gh_url,
        demo_name=demo_name,
        is_building=is_building,
        job_status=job_status,
        logs=logs,
        start_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
    )
