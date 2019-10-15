# Statement for enabling the development environment


# # Define the database - we are working with
# # SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# DATABASE_CONNECT_OPTIONS = {}

# # Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED = True

# Secret key for signing cookies

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True


class DevConfig(Config):
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
