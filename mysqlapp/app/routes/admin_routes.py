from app import app
from app.controllers import admin_controller
from flask import Blueprint, request

admin_blueprint = Blueprint("admin_routes", __name__)

@app.route("/admins", methods=["GET"])
def showAdmin():
    return admin_controller.showAdminController()

@app.route("/admins", methods=["POST"])
def createAdmin():
    params = request.json
    return admin_controller.createAdminController(**params)

@app.route("/admins", methods=["PUT"])
def updateAdmin():
    params = request.json
    return admin_controller.updateAdminController(**params)

@app.route("/admins", methods=["DELETE"])
def deleteAdmin():
    params = request.json
    return admin_controller.deleteAdminController(**params)

@app.route("/token", methods=["GET"])
def getToken():
    params = request.json
    return admin_controller.token(**params)