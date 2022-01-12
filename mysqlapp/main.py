from app import app

if __name__ == "__main__":
    app.run(debug=True)

# from config.config import database
# import models.models

# # from flask import Flask

# # mock data for create admin
# create_admin_data = {
#     "params":[
#         {
#             "values":{
#                 "admin_id": 1,
#                 "name": "ajjo",
#                 "username": "ajjo",
#                 "password": "12345678"
#             }
#         }
#     ]
# }

# # mock data for update admin
# update_admin_data = {
#     "params":[
#         {
#             "admin_id": 1,
#             "values":{
#                 "name": "daengz",
#                 "username": "daengz",
#             }
#         }
#     ]
# }

# # mock data for delete admin
# delete_admin_data = {
#     "params":[
#         {
#             "admin_id":1,
#         }
#     ]
# }

# # create new admin controller
# def createAdminController(data):
#     for param in data['params']:
#         models.models.createAdmin(**param)
#     print("data berhasil ditambahkan")

# # show all admin controller
# def showAdminController():
#     result = models.models.showAdmin()
#     for data in result:
#         # print(data)
#         print(data.user_id, data.name, data.username)
#     print("data admin berhasil ditampilkan")

# # update admin controller
# def updateAdminController(data):
#     for param in data['params']:
#         mysqldb.updateAdmin(**param)
#     mysqldb.dataCommit()
#     print("data berhasil diubah")

# # delete admin controller
# def deleteAdminController(data):
#     for param in data['params']:
#         mysqldb.deleteAdmin(**param)
#     mysqldb.dataCommit()
#     print("data berhasil dihapus")

# # # ROUTING
# # app = Flask(__name__)

# # @app.route("/")
# # def main():
# #     return "Welcome!"


# # MAIN
# if __name__=="__main__":
    
#     mysqldb = database()
#     if mysqldb:
#         print("Connection Success")
#     # if mysqldb.db.is_connected():
#     #     print('Connected to MySQL database')

#     createAdminController(create_admin_data)
#     showAdminController()
#     # updateAdminController(update_admin_data)
#     # deleteAdminController(delete_admin_data)
#     # app.run(debug=True)

#     # if mysqldb.db is not None and mysqldb.db.is_connected():
#     #     mysqldb.db.close()