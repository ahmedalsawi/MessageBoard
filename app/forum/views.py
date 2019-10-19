from flask import render_template, Blueprint

threads = [
    {"id": 1, "user": "user1", "title": "title1"},
    {"id": 2, "user": "user2", "title": "title2"},
]

posts = [{"id": 2, "thread": 1, "user": "user1", "content": "conent1"}]

bp = Blueprint("forum", __name__)


@bp.route("/", methods=["GET"])
def home():
    return render_template("forum/home.jinja")


@bp.route("/threads", methods=["GET", "POST"])
def threads_view():
    return render_template("forum/threads.jinja", threads=threads)


@bp.route("/threads/<string:id>", methods=["GET", "POST"])
def thread_view(id):
    return render_template("forum/thread.jinja", thread=[1, 2])
