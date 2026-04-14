from marshmallow import Schema, ValidationError, fields, validate, validates_schema


class DecisionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        required=True, validate=validate.Length(min=1, error="Title is required.")
    )
    reason = fields.Str(
        required=True, validate=validate.Length(min=1, error="Reason is required.")
    )
    confidence_level = fields.Int(
        required=True,
        validate=validate.Range(
            min=1, max=10, error="Confidence level must be between 1 and 10."
        ),
    )
    outcome = fields.Str(allow_none=True)
    lesson = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)

    @validates_schema
    def validate_confidence_level(self, data, **kwargs):
        return


class DecisionUpdateSchema(Schema):
    title = fields.Str(required=False)
    reason = fields.Str(required=False)
    confidence_level = fields.Int(
        required=False,
        validate=validate.Range(
            min=1, max=10, error="Confidence level must be between 1 and 10."
        ),
    )
    outcome = fields.Str(allow_none=True)
    lesson = fields.Str(allow_none=True)

    @validates_schema
    def validate_payload(self, data, **kwargs):
        if not data:
            raise ValidationError("At least one field must be provided.")
        return
