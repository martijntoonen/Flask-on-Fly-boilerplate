from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config


admin = Admin(name='My project', template_mode='bootstrap4', url='/')
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str) -> Flask:
    """
    The flask application factory.
    Use 'flask run' to run with default configuration.
    Or use 'app.run()' somewhere else in python code.
    :param config_name: define config class in config.py. Map config_name to class in the dict.
    :return: flask application object
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import User
    admin.add_view(ModelView(User, db.session))

    return app
