from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
swagger_ext = Swagger()
api = Api()
