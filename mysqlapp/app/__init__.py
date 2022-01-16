from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

from app.routes.admin_routes import *
from app.routes.order_routes import *

app.register_blueprint(admin_blueprint)
app.register_blueprint(order_blueprint)