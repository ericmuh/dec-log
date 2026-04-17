from flask import request
from flask_restful import Resource

from ..extensions import db
from ..models import Decision
from ..schemas import decision_schema, decisions_schema


class DecisionListResource(Resource):
    def get(self):
        decisions = Decision.query.order_by(Decision.created_at.desc()).all()
        return decisions_schema.dump(decisions), 200

    def post(self):
        payload = request.get_json(silent=True) or {}
        errors = decision_schema.validate(payload)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400

        decision = Decision(
            title=payload["title"],
            reason=payload["reason"],
            confidence_level=payload["confidence_level"],
            outcome=payload.get("outcome", "Pending"),
            lesson=payload.get("lesson", "Lesson not recorded yet"),
        )
        db.session.add(decision)
        db.session.commit()
        return decision_schema.dump(decision), 201


class DecisionResource(Resource):
    def get(self, decision_id):
        decision = Decision.query.get_or_404(decision_id)
        return decision_schema.dump(decision), 200

    def put(self, decision_id):
        decision = Decision.query.get_or_404(decision_id)
        payload = request.get_json(silent=True) or {}
        errors = decision_schema.validate(payload, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400

        if "title" in payload:
            decision.title = payload["title"]
        if "reason" in payload:
            decision.reason = payload["reason"]
        if "confidence_level" in payload:
            decision.confidence_level = payload["confidence_level"]
        if "outcome" in payload:
            decision.outcome = payload["outcome"]
        if "lesson" in payload:
            decision.lesson = payload["lesson"]

        db.session.commit()
        return decision_schema.dump(decision), 200

    def delete(self, decision_id):
        decision = Decision.query.get_or_404(decision_id)
        db.session.delete(decision)
        db.session.commit()
        return {"message": "Decision deleted"}, 200
