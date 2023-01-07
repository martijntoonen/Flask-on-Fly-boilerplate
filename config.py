import os
from pathlib import Path

basedir = Path(__file__).parent


class Config:
    FLASK_ADMIN_SWATCH = 'cerulean'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SECRET_KEY = 'shhh_dont_say_a_word'


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ADMIN_SWATCH = 'superhero'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SECRET_KEY = os.getenv('SECRET_KEY')


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
