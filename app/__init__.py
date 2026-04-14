import os

from dotenv import load_dotenv
from flask import Flask
from flasgger import Swagger
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.blueprints.auth import auth_bp
from app.blueprints.decision import decision_bp
from app.blueprints.user import user_bp
from app.config import DevelopmentConfig, ProductionConfig
from app.extensions import db, login_manager, migrate
from app.models import User
from app.swagger.swagger_config import swagger_config, swagger_template
from app.utils.response import api_response


load_dotenv()


def create_app(config_name: str | None = None):
    app = Flask(__name__)

    config_value = (config_name or os.getenv("FLASK_ENV", "development")).lower()
    if config_value == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    app.config.setdefault("JSON_SORT_KEYS", False)
    app.config.setdefault("MAX_CONTENT_LENGTH", 5 * 1024 * 1024)
    app.url_map.strict_slashes = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    Swagger(app, config=swagger_config, template=swagger_template)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/user")
    app.register_blueprint(decision_bp, url_prefix="/api/decisions")

    _register_error_handlers(app)
    _register_login_manager_handlers()
    _ensure_upload_directory(app)

    with app.app_context():
        from app import models  # noqa: F401

    return app


def _register_error_handlers(app: Flask) -> None:
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return api_response(False, "Validation failed", {"errors": error.messages}, 400)

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        db.session.rollback()
        return api_response(
            False, "Database integrity error", {"errors": str(error.orig)}, 400
        )

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(error):
        db.session.rollback()
        return api_response(False, "Database error", {"errors": str(error)}, 500)

    @app.errorhandler(404)
    def handle_not_found(_error):
        return api_response(False, "Resource not found", {}, 404)

    @app.errorhandler(405)
    def handle_method_not_allowed(_error):
        return api_response(False, "Method not allowed", {}, 405)

    @app.errorhandler(413)
    def handle_payload_too_large(_error):
        return api_response(False, "Uploaded file is too large", {}, 413)


def _register_login_manager_handlers() -> None:
    @login_manager.user_loader
    def load_user(user_id: str):
        return db.session.get(User, int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return api_response(False, "Authentication required", {}, 401)


def _ensure_upload_directory(app: Flask) -> None:
    upload_dir = app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_dir, exist_ok=True)
