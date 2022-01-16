from app.models.admin import admin_database
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

mysqldb = admin_database()

def createAdminController(**params):
    mysqldb.createAdmin(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def showAdminController():
    dbresult = mysqldb.showAdmin()
    result = []
    for items in dbresult:
        user = {
            "admin_id": items[0],
            "name": items[1],
            "username": items[2]
        }
        result.append(user)
    
    return jsonify(result)

@jwt_required()
def updateAdminController(**params):
    mysqldb.updateAdmin(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

@jwt_required()
def deleteAdminController(**params):
    mysqldb.deleteAdmin(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def token(**params):
    dbresult = mysqldb.showAdminByUsername(**params)
    if dbresult is not None:
        admin = {
            "admin_id": dbresult[0],
        }

        expires = datetime.timedelta(days=1)
        access_token = create_access_token(admin, fresh=True,expires_delta=expires)
        data = {
            "data":admin,
            "token_access":access_token,
        }
    else:
        data = {
            "message":"Email tidak terdaftar"
        }
    return jsonify(data)







