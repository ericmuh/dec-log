from flask import Blueprint, redirect, render_template, request, url_for

from ..extensions import db
from ..models import User

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/")
def list_users():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("users/list.html", users=users)


@users_bp.route("/new", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()

        if name and email:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("users.list_users"))

    return render_template("users/create.html")


@users_bp.route("/<int:user_id>")
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("users/detail.html", user=user)
