from app import app
from app.controllers import admin_controller
from flask import Blueprint, request

model_blueprint = Blueprint("routes", __name__)

@app.route("/admins", methods=["GET"])
def showAdmin():
    return admin_controller.showAdminController()