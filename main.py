import os

from app import create_app


CONFIG = os.getenv('FLASK_CONFIG', 'default')
app = create_app(CONFIG)
