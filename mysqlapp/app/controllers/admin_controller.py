from app.models.admin import database
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

mysqlb = database()

def showAdminController():
    dbresult = mysqlb.showAdmin()
    result = []
    for items in dbresult:
        user = {
            "admin_id": items[0],
            "name": items[1],
            "username": items[2],
            "password": items[3]
        }
        result.append(user)
    
    return jsonify(result)