from datetime import datetime

from sqlalchemy import CheckConstraint

from app.extensions import db


class Decision(db.Model):
    __tablename__ = "decisions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    confidence_level = db.Column(db.Integer, nullable=False)
    outcome = db.Column(db.Text, nullable=True)
    lesson = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    user = db.relationship("User", back_populates="decisions")

    __table_args__ = (
        CheckConstraint(
            "confidence_level >= 1 AND confidence_level <= 10",
            name="check_confidence_level_range",
        ),
    )

    def __repr__(self) -> str:
        return f"<Decision {self.title}>"
