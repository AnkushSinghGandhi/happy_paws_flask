from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Importing routes
from routes import register_routes
register_routes(app)

@app.route('/')
def home():
    return "Welcome to Happy Paws API!"

if __name__ == '__main__':
    app.run(debug=True)
