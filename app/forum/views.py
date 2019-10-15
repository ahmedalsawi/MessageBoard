from app import app

from flask import render_template


@app.route("/", methods=["GET"])
def home():
    return render_template("home.jinja")


@app.route("/threads", methods=["GET"])
def threads():
    return render_template("forum/threads.jinja")


@app.route("/threads/<string:id>", methods=["GET"])
def thread(id):
    return render_template("forum/thread.jinja")
