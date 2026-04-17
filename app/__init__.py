from flask import Flask, jsonify, request

from .extensions import api, db, ma, migrate


# Basic in-memory dataset for the first API examples with jsonify.
basic_decisions = [
    {
        "id": 1,
        "title": "Adopt weekly planning",
        "reason": "Improve team coordination",
        "confidence_level": 4,
    }
]


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///decision_log.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api.init_app(app)

    from . import models  # noqa: F401
    from .resources.decision import DecisionListResource, DecisionResource

    api.add_resource(DecisionListResource, "/decisions")
    api.add_resource(DecisionResource, "/decisions/<int:decision_id>")

    @app.get("/")
    def home():
        return jsonify(
            {
                "message": "Decision Log API Lesson 6",
                "sections": {
                    "basic": "/api/basic/decisions",
                    "extensions": "/api/v1/decisions",
                },
            }
        )

    @app.get("/api/basic/decisions")
    def basic_list_decisions():
        return jsonify(basic_decisions)

    @app.get("/api/basic/decisions/<int:decision_id>")
    def basic_get_decision(decision_id):
        decision = next((d for d in basic_decisions if d["id"] == decision_id), None)
        if decision is None:
            return jsonify({"message": "Decision not found"}), 404
        return jsonify(decision)

    @app.post("/api/basic/decisions")
    def basic_create_decision():
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        reason = payload.get("reason")
        confidence_level = payload.get("confidence_level", 3)

        if not title or not reason:
            return jsonify({"message": "title and reason are required"}), 400

        new_id = max((d["id"] for d in basic_decisions), default=0) + 1
        decision = {
            "id": new_id,
            "title": title,
            "reason": reason,
            "confidence_level": confidence_level,
        }
        basic_decisions.append(decision)
        return jsonify(decision), 201

    return app
