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
        summary: Register account
        description: Create a new user account using a unique username and email.
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: register_payload
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
                  minLength: 3
                  example: alice
                email:
                  type: string
                  format: email
                  example: alice@example.com
                password:
                  type: string
                  minLength: 8
                  example: StrongPass123
        responses:
          201:
            description: User registered successfully
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: true
                message:
                  type: string
                  example: User registered successfully
                data:
                  type: object
                  properties:
                    user:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        username:
                          type: string
                          example: alice
                        email:
                          type: string
                          example: alice@example.com
                        profile_picture:
                          type: string
                          nullable: true
                        profile_picture_url:
                          type: string
                          nullable: true
                        created_at:
                          type: string
                          format: date-time
          400:
            description: Duplicate email/username or invalid payload
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: false
                message:
                  type: string
                  example: Username already exists
                data:
                  type: object
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
        summary: Login
        description: Authenticate with email and password. Returns a session cookie.
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: login_payload
            required: true
            schema:
              type: object
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  format: email
                  example: alice@example.com
                password:
                  type: string
                  example: StrongPass123
        responses:
          200:
            description: User logged in successfully
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: true
                message:
                  type: string
                  example: Login successful
                data:
                  type: object
                  properties:
                    user:
                      type: object
                      properties:
                        id:
                          type: integer
                        username:
                          type: string
                        email:
                          type: string
          401:
            description: Invalid credentials
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: false
                message:
                  type: string
                  example: Invalid email or password
                data:
                  type: object
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
        summary: Logout
        description: Clears the active user session.
        produces:
          - application/json
        responses:
          200:
            description: User logged out successfully
            schema:
              type: object
              properties:
                success:
                  type: boolean
                  example: true
                message:
                  type: string
                  example: Logout successful
                data:
                  type: object
        """
        logout_user()
        return api_response(True, "Logout successful", {}, 200)


def api_request_json():
    from flask import request

    return request.get_json(silent=True) or {}
