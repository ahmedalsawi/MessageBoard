from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.config import Config, DevConfig


def create_app(config_class=DevConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth.views import bp as auth_bp
    from app.forum.views import bp as forum_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(forum_bp)

    return app

