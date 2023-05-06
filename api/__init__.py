from flask import Flask
from api.routes.distance import distance_routes
from api.routes.client import client_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(distance_routes)
    app.register_blueprint(client_routes)
    return app

