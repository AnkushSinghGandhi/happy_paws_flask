import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///happypaws.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
