from app.models.order import order_database
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

mysqldb_order = order_database()

@jwt_required()
def createOrderController(**params):
    print("p")
    order = {
        "order_id":params["order_id"],
        "created_at":datetime.date.today(),
        "customer_name":params["customer_name"],
        "admin_id":params["admin_id"],
    }
    print(order)
    mysqldb_order.createOrder(**order)
    mysqldb_order.dataCommit()
    for beverage in params["beverage"]:
        data = {
            "order_id":order["order_id"],
            "beverage_id":beverage["beverage_id"],
            "qty":beverage["qty"],
        }
        print(data)
        mysqldb_order.createOrderDetail(**data)
        mysqldb_order.dataCommit()

    return jsonify({"message":"Success"})

@jwt_required()
def viewOrderController():
    dbresult = mysqldb_order.viewOrder()
    result = []
    for items in dbresult:
        order = {
            "order_id": items[0],
            "created_at": items[1],
            "customer_name": items[2],
            "total": items[4]
        }
        result.append(order)
    
    return jsonify(result)

@jwt_required()
def viewOrderByDateController(**params):
    dbresult = mysqldb_order.viewOrderByDate(**params)
    result = []
    for items in dbresult:
        order = {
            "order_id": items[0],
            "created_at": items[1],
            "customer_name": items[2],
            "total": items[4]
        }
        result.append(order)
    
    return jsonify(result)

@jwt_required()
def deleteOrderController(**params):
    mysqldb_order.deleteOrder(**params)
    mysqldb_order.dataCommit()
    return jsonify({"message":"Success"})