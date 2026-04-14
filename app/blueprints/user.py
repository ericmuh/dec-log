from flask import Blueprint
from flask_restful import Api

from app.resources.user import UserProfilePictureResource, UserProfileResource


user_bp = Blueprint("user", __name__)
user_api = Api(user_bp)

user_api.add_resource(UserProfileResource, "/profile")
user_api.add_resource(UserProfilePictureResource, "/profile/picture")
