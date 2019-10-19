import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True


class DevConfig(Config):
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASE_DIR, "app.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
