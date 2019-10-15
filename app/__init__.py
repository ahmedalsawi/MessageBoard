

from flask import Flask
from app.auth import bp as auth_bp

app = Flask(__name__)


app.register_blueprint(auth_bp)



from app.auth import views