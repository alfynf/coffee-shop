from app import app
from app.controllers import order_controller
from flask import Blueprint, request

order_blueprint = Blueprint("order_routes", __name__)

@app.route("/orders", methods=["POST"])
def createOrder():
    params = request.json
    return order_controller.createOrderController(**params)

@app.route("/orders", methods=["GET"])
def viewOrder():
    return order_controller.viewOrderController()

@app.route("/orders/date", methods=["GET"])
def viewOrderByDate():
    params = request.json
    return order_controller.viewOrderByDateController(**params)

@app.route("/orders", methods=["DELETE"])
def deleteOrder():
    params = request.json
    return order_controller.deleteOrderController(**params)