from app import app

from flask import render_template


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("auth/login.jinja")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("auth/register.jinja")
