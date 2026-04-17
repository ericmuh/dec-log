from .extensions import ma
from .models import Decision


class DecisionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Decision
        ordered = True

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(required=True)
    reason = ma.auto_field(required=True)
    confidence_level = ma.auto_field(required=True)
    outcome = ma.auto_field()
    lesson = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)


decision_schema = DecisionSchema()
decisions_schema = DecisionSchema(many=True)
