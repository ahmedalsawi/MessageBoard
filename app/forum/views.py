from app import app

from flask import render_template


@app.route("/", methods=["GET"])
def index():
    return render_template("home.jinja")


@app.route("/forum", methods=["GET"])
def forum():
    return render_template("home.jinja")

@app.route("/forum/:id", methods=["GET"])
def thread():
    return render_template("home.jinja")