from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///decision_log.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Flask extensions for ORM and migrations.
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    confidence_level = db.Column(db.Integer, nullable=False)
    outcome = db.Column(db.String(20), nullable=False, default="Pending")
    lesson = db.Column(db.Text, nullable=False, default="Lesson not recorded yet")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


def parse_confidence(raw_value, fallback=3):
    try:
        value = int(raw_value)
    except (TypeError, ValueError):
        return fallback

    return value if 1 <= value <= 5 else fallback


@app.route("/")
def home():
    decisions = Decision.query.order_by(Decision.created_at.desc()).all()
    return render_template("index.html", decisions=decisions)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/decisions/new", methods=["GET", "POST"])
def create_decision():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = parse_confidence(request.form.get("confidence_level"))

        if title and reason:
            decision = Decision(
                title=title,
                reason=reason,
                confidence_level=confidence_level,
                outcome="Pending",
                lesson="Lesson not recorded yet",
            )
            db.session.add(decision)
            db.session.commit()
            return redirect(url_for("decision_detail", decision_id=decision.id))

    return render_template("create_decision.html")


@app.route("/decisions/<int:decision_id>")
def decision_detail(decision_id):
    decision = Decision.query.get_or_404(decision_id)
    return render_template("decision_detail.html", decision=decision)


@app.route("/decisions/<int:decision_id>/edit", methods=["GET", "POST"])
def edit_decision(decision_id):
    decision = Decision.query.get_or_404(decision_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = request.form.get("confidence_level", "").strip()
        outcome = request.form.get("outcome", "").strip()
        lesson = request.form.get("lesson", "").strip()

        if title:
            decision.title = title
        if reason:
            decision.reason = reason
        if confidence_level:
            decision.confidence_level = parse_confidence(
                confidence_level, decision.confidence_level
            )
        if outcome:
            decision.outcome = outcome
        if lesson:
            decision.lesson = lesson

        db.session.commit()
        return redirect(url_for("decision_detail", decision_id=decision.id))

    return render_template("edit_decision.html", decision=decision)


@app.route("/decisions/<int:decision_id>/delete", methods=["POST"])
def delete_decision(decision_id):
    decision = Decision.query.get_or_404(decision_id)
    db.session.delete(decision)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
