from datetime import datetime

from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    decisions = db.relationship(
        "Decision", back_populates="user", cascade="all, delete-orphan"
    )


class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    confidence_level = db.Column(db.Integer, nullable=False)
    outcome = db.Column(db.String(20), nullable=False, default="Pending")
    lesson = db.Column(db.Text, nullable=False, default="Lesson not recorded yet")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="decisions")
