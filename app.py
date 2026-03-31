from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from dotenv import load_dotenv

# internal imports

load_dotenv()
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")


# Definiing the DB ( instance of SQLAlchemy and attaching our app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# importing blueprints and registering them
from decisions import decision_app

from users import users_app

app.register_blueprint(decision_app)
app.register_blueprint(users_app)


# This creates all tables, doesn't update tables if your models change
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
