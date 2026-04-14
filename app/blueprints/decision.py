from flask import Blueprint
from flask_restful import Api

from app.resources.decision import DecisionDetailResource, DecisionListResource


decision_bp = Blueprint("decision", __name__)
decision_api = Api(decision_bp)

decision_api.add_resource(DecisionListResource, "/")
decision_api.add_resource(DecisionDetailResource, "/<int:decision_id>")
