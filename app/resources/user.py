from flask import current_app, request
from flask_login import current_user
from flask_restful import Resource

from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import (
    ProfilePictureSchema,
    UpdateProfileSchema,
    UserSchema,
)
from app.utils.auth import login_required_json
from app.utils.image_helper import (
    is_allowed_image,
    remove_file_if_exists,
    save_profile_picture,
)
from app.utils.response import api_response


user_schema = UserSchema()
update_schema = UpdateProfileSchema()
profile_picture_schema = ProfilePictureSchema()


class UserProfileResource(Resource):
    method_decorators = [login_required_json]

    def get(self):
        """Get the authenticated user's profile.
        ---
        tags:
          - Users
        responses:
          200:
            description: Profile returned successfully
        """
        return api_response(
            True,
            "Profile retrieved successfully",
            {"user": user_schema.dump(current_user)},
            200,
        )

    def put(self):
        """Update the authenticated user's profile.
        ---
        tags:
          - Users
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
        responses:
          200:
            description: Profile updated successfully
        """
        payload = update_schema.load(request.get_json(silent=True) or {})

        if "username" in payload:
            existing_user = User.query.filter(
                User.username == payload["username"].strip(), User.id != current_user.id
            ).first()
            if existing_user:
                return api_response(False, "Username already exists", {}, 400)
            current_user.username = payload["username"].strip()

        if "email" in payload:
            existing_email = User.query.filter(
                User.email == payload["email"].lower(), User.id != current_user.id
            ).first()
            if existing_email:
                return api_response(False, "Email already exists", {}, 400)
            current_user.email = payload["email"].lower()

        if "password" in payload:
            current_user.set_password(payload["password"])

        db.session.commit()
        return api_response(
            True,
            "Profile updated successfully",
            {"user": user_schema.dump(current_user)},
            200,
        )


class UserProfilePictureResource(Resource):
    method_decorators = [login_required_json]

    def post(self):
        """Upload or update the authenticated user's profile picture.
        ---
        tags:
          - Users
        consumes:
          - multipart/form-data
        parameters:
          - in: formData
            name: profile_picture
            type: file
            required: true
        responses:
          200:
            description: Profile picture updated successfully
        """
        uploaded_file = request.files.get("profile_picture")

        if not uploaded_file:
            return api_response(False, "Profile picture file is required", {}, 400)

        if not is_allowed_image(uploaded_file.filename):
            return api_response(False, "Unsupported image type", {}, 400)

        old_picture = current_user.profile_picture
        relative_path = save_profile_picture(
            uploaded_file, current_app.config["UPLOAD_FOLDER"]
        )
        current_user.profile_picture = relative_path
        db.session.commit()

        remove_file_if_exists(old_picture, current_app.static_folder)

        return api_response(
            True,
            "Profile picture updated successfully",
            {"user": user_schema.dump(current_user)},
            200,
        )
