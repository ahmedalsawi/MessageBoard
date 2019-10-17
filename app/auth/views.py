from app import app

from flask import render_template, request, redirect, url_for

from .forms import LoginForm, RegisterForm


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        print(form)
        # TODO
        return redirect('/success')
    return render_template("auth/login.jinja", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        print(form)

        # TODO
        return redirect(url_for("index"))
    return render_template("auth/register.jinja", form=form)
