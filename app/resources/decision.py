from flask import request
from flask_login import current_user
from flask_restful import Resource

from app.extensions import db
from app.models.decision import Decision
from app.schemas.decision_schema import DecisionSchema, DecisionUpdateSchema
from app.utils.auth import login_required_json
from app.utils.response import api_response


decision_schema = DecisionSchema()
decisions_schema = DecisionSchema(many=True)
decision_update_schema = DecisionUpdateSchema()


class DecisionListResource(Resource):
    method_decorators = [login_required_json]

    def get(self):
        """List the authenticated user's decisions.
        ---
        tags:
          - Decisions
        responses:
          200:
            description: Decision list returned successfully
        """
        decisions = (
            Decision.query.filter_by(user_id=current_user.id)
            .order_by(Decision.created_at.desc())
            .all()
        )
        return api_response(
            True,
            "Decisions retrieved successfully",
            {"decisions": decisions_schema.dump(decisions)},
            200,
        )

    def post(self):
        """Create a new decision.
        ---
        tags:
          - Decisions
        summary: Create decision
        description: Create a decision entry for the authenticated user.
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: decision_payload
            required: true
            schema:
              type: object
              required:
                - title
                - reason
                - confidence_level
              properties:
                title:
                  type: string
                  minLength: 1
                  example: Move to a new city
                reason:
                  type: string
                  minLength: 1
                  example: Better long-term career opportunities
                confidence_level:
                  type: integer
                  minimum: 1
                  maximum: 10
                  example: 8
                outcome:
                  type: string
                  nullable: true
                  example: Pending
                lesson:
                  type: string
                  nullable: true
                  example: Validate assumptions with a mentor first
        responses:
          201:
            description: Decision created successfully
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: true
                message:
                  type: string
                  example: Decision created successfully
                data:
                  type: object
                  properties:
                    decision:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        title:
                          type: string
                          example: Move to a new city
                        reason:
                          type: string
                        confidence_level:
                          type: integer
                          example: 8
                        outcome:
                          type: string
                          nullable: true
                        lesson:
                          type: string
                          nullable: true
                        created_at:
                          type: string
                          format: date-time
                        user_id:
                          type: integer
                          example: 1
          400:
            description: Validation error
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: false
                message:
                  type: string
                  example: Validation failed
                data:
                  type: object
          401:
            description: Authentication required
        """
        payload = decision_schema.load(request.get_json(silent=True) or {})
        decision = Decision(
            title=payload["title"].strip(),
            reason=payload["reason"].strip(),
            confidence_level=payload["confidence_level"],
            outcome=payload.get("outcome"),
            lesson=payload.get("lesson"),
            user_id=current_user.id,
        )

        db.session.add(decision)
        db.session.commit()

        return api_response(
            True,
            "Decision created successfully",
            {"decision": decision_schema.dump(decision)},
            201,
        )


class DecisionDetailResource(Resource):
    method_decorators = [login_required_json]

    def get(self, decision_id: int):
        """Get a single decision owned by the authenticated user.
        ---
        tags:
          - Decisions
        responses:
          200:
            description: Decision returned successfully
        """
        decision = self._get_owned_decision(decision_id)
        if not decision:
            return api_response(False, "Decision not found", {}, 404)
        return api_response(
            True,
            "Decision retrieved successfully",
            {"decision": decision_schema.dump(decision)},
            200,
        )

    def put(self, decision_id: int):
        """Update a decision owned by the authenticated user.
        ---
        tags:
          - Decisions
        consumes:
          - application/json
        responses:
          200:
            description: Decision updated successfully
        """
        decision = self._get_owned_decision(decision_id)
        if not decision:
            return api_response(False, "Decision not found", {}, 404)

        payload = decision_update_schema.load(request.get_json(silent=True) or {})

        if "title" in payload:
            decision.title = payload["title"].strip()
        if "reason" in payload:
            decision.reason = payload["reason"].strip()
        if "confidence_level" in payload:
            decision.confidence_level = payload["confidence_level"]
        if "outcome" in payload:
            decision.outcome = payload["outcome"]
        if "lesson" in payload:
            decision.lesson = payload["lesson"]

        db.session.commit()
        return api_response(
            True,
            "Decision updated successfully",
            {"decision": decision_schema.dump(decision)},
            200,
        )

    def delete(self, decision_id: int):
        """Delete a decision owned by the authenticated user.
        ---
        tags:
          - Decisions
        responses:
          200:
            description: Decision deleted successfully
        """
        decision = self._get_owned_decision(decision_id)
        if not decision:
            return api_response(False, "Decision not found", {}, 404)

        db.session.delete(decision)
        db.session.commit()
        return api_response(True, "Decision deleted successfully", {}, 200)

    def _get_owned_decision(self, decision_id: int):
        return Decision.query.filter_by(id=decision_id, user_id=current_user.id).first()
