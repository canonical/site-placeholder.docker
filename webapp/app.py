from datetime import datetime

from flask import Flask, render_template

from webapp import create_app
from webapp.jenkins import Jenkins

app = create_app()


@app.route("/_status/check")
def status():
    return "OK"


@app.route("/")
def index():
    jenkins = Jenkins(app=app)

    # Get the job details
    build_url = jenkins.info["url"]
    job_status = jenkins.info["result"]
    is_building = jenkins.info["inProgress"]

    demo_name = jenkins.get_demo_name()
    start_time = jenkins.get_start_time()
    logs = jenkins.get_job_logs()

    return render_template(
        "index.html",
        build_url=build_url,
        gh_url=gh_url,
        demo_name=demo_name,
        is_building=is_building,
        job_status=job_status,
        logs=logs,
        start_time=start_time,
    )
