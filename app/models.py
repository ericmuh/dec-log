from datetime import datetime

from .extensions import db


class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    confidence_level = db.Column(db.Integer, nullable=False)
    outcome = db.Column(db.String(20), nullable=False, default="Pending")
    lesson = db.Column(db.Text, nullable=False, default="Lesson not recorded yet")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
