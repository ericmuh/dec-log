from flask import Blueprint
from flask_restful import Api

from app.resources.auth import LoginResource, LogoutResource, RegisterResource


auth_bp = Blueprint("auth", __name__)
auth_api = Api(auth_bp)

auth_api.add_resource(RegisterResource, "/register")
auth_api.add_resource(LoginResource, "/login")
auth_api.add_resource(LogoutResource, "/logout")
