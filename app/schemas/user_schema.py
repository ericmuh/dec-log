from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    validates_schema,
)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    profile_picture = fields.Str(allow_none=True)
    profile_picture_url = fields.Method("get_profile_picture_url", dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    def get_profile_picture_url(self, obj):
        if not getattr(obj, "profile_picture", None):
            return None
        from flask import url_for

        return url_for("static", filename=obj.profile_picture, _external=True)


class RegisterSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(
            min=8, error="Password must be at least 8 characters long."
        ),
    )

    @validates("username")
    def validate_username(self, value):
        if len(value.strip()) < 3:
            raise ValidationError("Username must be at least 3 characters long.")


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class UpdateProfileSchema(Schema):
    username = fields.Str(required=False)
    email = fields.Email(required=False)
    password = fields.Str(
        required=False,
        load_only=True,
        validate=validate.Length(
            min=8, error="Password must be at least 8 characters long."
        ),
    )

    @validates_schema
    def validate_payload(self, data, **kwargs):
        if not data:
            raise ValidationError("At least one field must be provided.")
        if "username" in data and len(data["username"].strip()) < 3:
            raise ValidationError(
                {"username": ["Username must be at least 3 characters long."]}
            )


class ProfilePictureSchema(Schema):
    profile_picture = fields.Field(required=True)
