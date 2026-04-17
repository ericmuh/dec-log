from flask import Blueprint, redirect, render_template, request, url_for

from ..extensions import db
from ..models import Decision, User

decisions_bp = Blueprint("decisions", __name__, url_prefix="/decisions")


@decisions_bp.route("/")
def list_decisions():
    decisions = Decision.query.order_by(Decision.created_at.desc()).all()
    return render_template("decisions/list.html", decisions=decisions)


@decisions_bp.route("/new", methods=["GET", "POST"])
def create_decision():
    users = User.query.order_by(User.name.asc()).all()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = int(request.form.get("confidence_level") or 3)
        user_id = int(request.form.get("user_id") or 0)

        if title and reason and user_id:
            decision = Decision(
                title=title,
                reason=reason,
                confidence_level=confidence_level,
                user_id=user_id,
                outcome="Pending",
                lesson="Lesson not recorded yet",
            )
            db.session.add(decision)
            db.session.commit()
            return redirect(
                url_for("decisions.decision_detail", decision_id=decision.id)
            )

    return render_template("decisions/create.html", users=users)


@decisions_bp.route("/<int:decision_id>")
def decision_detail(decision_id):
    decision = Decision.query.get_or_404(decision_id)
    return render_template("decisions/detail.html", decision=decision)


@decisions_bp.route("/<int:decision_id>/edit", methods=["GET", "POST"])
def edit_decision(decision_id):
    decision = Decision.query.get_or_404(decision_id)
    users = User.query.order_by(User.name.asc()).all()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = request.form.get("confidence_level", "").strip()
        outcome = request.form.get("outcome", "").strip()
        lesson = request.form.get("lesson", "").strip()
        user_id = request.form.get("user_id", "").strip()

        if title:
            decision.title = title
        if reason:
            decision.reason = reason
        if confidence_level:
            decision.confidence_level = int(confidence_level)
        if outcome:
            decision.outcome = outcome
        if lesson:
            decision.lesson = lesson
        if user_id:
            decision.user_id = int(user_id)

        db.session.commit()
        return redirect(url_for("decisions.decision_detail", decision_id=decision.id))

    return render_template("decisions/edit.html", decision=decision, users=users)


@decisions_bp.route("/<int:decision_id>/delete", methods=["POST"])
def delete_decision(decision_id):
    decision = Decision.query.get_or_404(decision_id)
    db.session.delete(decision)
    db.session.commit()
    return redirect(url_for("decisions.list_decisions"))
