from flask_login import login_user, logout_user
from flask_restful import Resource

from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import LoginSchema, RegisterSchema, UserSchema
from app.utils.response import api_response


register_schema = RegisterSchema()
login_schema = LoginSchema()
user_schema = UserSchema()


class RegisterResource(Resource):
    def post(self):
        """Register a new user.
        ---
        tags:
          - Auth
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - username
                - email
                - password
              properties:
                username:
                  type: string
                email:
                  type: string
                  format: email
                password:
                  type: string
        responses:
          201:
            description: User registered successfully
        """
        payload = register_schema.load(api_request_json())

        if User.query.filter_by(username=payload["username"].strip()).first():
            return api_response(False, "Username already exists", {}, 400)

        if User.query.filter_by(email=payload["email"].lower()).first():
            return api_response(False, "Email already exists", {}, 400)

        user = User(
            username=payload["username"].strip(), email=payload["email"].lower()
        )
        user.set_password(payload["password"])

        db.session.add(user)
        db.session.commit()

        return api_response(
            True, "User registered successfully", {"user": user_schema.dump(user)}, 201
        )


class LoginResource(Resource):
    def post(self):
        """Login an existing user.
        ---
        tags:
          - Auth
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - email
                - password
        responses:
          200:
            description: User logged in successfully
        """
        payload = login_schema.load(api_request_json())
        user = User.query.filter_by(email=payload["email"].lower()).first()

        if not user or not user.check_password(payload["password"]):
            return api_response(False, "Invalid email or password", {}, 401)

        login_user(user)
        return api_response(
            True, "Login successful", {"user": user_schema.dump(user)}, 200
        )


class LogoutResource(Resource):
    def post(self):
        """Logout the current user.
        ---
        tags:
          - Auth
        responses:
          200:
            description: User logged out successfully
        """
        logout_user()
        return api_response(True, "Logout successful", {}, 200)


def api_request_json():
    from flask import request

    return request.get_json(silent=True) or {}
