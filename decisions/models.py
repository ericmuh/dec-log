from app import db
from datetime import datetime


# MODELS FOR THE DECISION
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    reason = db.Column(db.String(120))
    confidence_level = db.Column(db.Integer)
    outcome = db.Column(db.String)
    lesson = db.Column(db.Text)
    due_date = db.Column(db.String(128))
    create_at = db.Column(db.DateTime, default=datetime.now())
