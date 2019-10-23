from flask import render_template, request, redirect, url_for, Blueprint, flash

from .forms import LoginForm, RegisterForm
from app.models import User

bp = Blueprint("auth", __name__)

from app import db, bcrypt


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():

        if form.email.data == "a@gmail.com" and form.password.data == "password":
            flash(f"Logined as", "green")
            return redirect(url_for("forum.home"))
        else:
            flash(f"Login invalid", "red")
    return render_template("auth/login.jinja", title="Login", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account Created", "green")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.jinja", title="Register", form=form)
