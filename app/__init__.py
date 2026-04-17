from flask import Flask

from .blueprints.decisions import decisions_bp
from .blueprints.main import main_bp
from .blueprints.users import users_bp
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///decision_log.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models  # noqa: F401

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(decisions_bp)

    return app
