"""
Main application module for the Receipt Processor API.
This module creates the Flask application instance, registers the routes blueprint.
"""
from api.routes import routes
from flask import Flask

app = Flask(__name__)

app.register_blueprint(routes)
