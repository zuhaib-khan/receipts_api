from api.routes import routes
from flask import Flask

app = Flask(__name__)

app.register_blueprint(routes)
