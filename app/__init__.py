

from flask import Flask
from app.auth import bp as auth_bp
from app.forum import bp as forum_bp
app = Flask(__name__)


app.register_blueprint(auth_bp)
app.register_blueprint(forum_bp)


from app.auth import views
from app.forum import views
