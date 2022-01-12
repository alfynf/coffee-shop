# from enum import unique
from mysql.connector import connect
# from app import database
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import exc, delete, update

###################################################### NON ORM
############## DECLARE MODELS
class database:
    # connect to mysql database
    def __init__(self):
        try:
            self.db = connect(host='localhost',
            database = 'coffee_shop',
            user = 'root',
            password = '12345678')
        except Exception as e:
            print(e)
    ########### MODEL ADMIN
    # create new admin
    def createAdmin(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            tx =   '''INSERT INTO admins ({0}) values {1};'''.format(column,values)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)
    # view all admin func
    def showAdmin(self):
        try:
            tx = '''SELECT user_id, name, username FROM admins'''
            cursor = self.db.cursor()
            cursor.execute(tx)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    # update admin profile
    def updateAdmin(self, **params):
        try:
            user_id = params['user_id']
            values = self.restructureParams(**params['values'])
            tx = '''UPDATE admins SET {0} WHERE user_id = {1};'''.format(values,user_id)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)
    # delete admin
    def deleteAdmin(self, **params):
        try:
            user_id = params['user_id']
            tx = '''DELETE FROM admins WHERE user_id = {0}'''.format(user_id)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)

    ########### MODEL ORDER
    # create new order
    def createOrder(self):
        pass
    # view all order
    def viewOrder(self):
        pass
    # view order by date
    def viewOrderByDate(self):
        pass
    # delete order
    def deleteOrder(self):
        pass
# #     ########### MODEL BEVERAGES
# #     # create new beverages
# #     def createBeverage(self):
# #         pass
# #     # view all beverages
# #     def viewBeverage(self):
# #         pass
# #     # view beverage by type
# #     def viewBeverageByType(self):
# #         pass
# #     # view beverage by price
# #     def viewBeverageByPrice(self):
# #         pass
# #     # update beverage
# #     def updateBeverage(self):
# #         pass
# #     # delete beverage
# #     def deleteBeverage(self):
# #         pass
    # restructure param
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result
    # data commit  
    def dataCommit(self):
        self.db.commit()

####################################################### NON ORM

# ####################################################### ORM
# Base = declarative_base()

# db = database()

# # ############### DECLARE TABLE STRUCT

# # declare admin table struct
# class Admins(Base):
#     __tablename__ = 'admins'
#     admin_id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String,nullable=False)
#     username = Column(String,unique=True,nullable=False)
#     password = Column(String, nullable=False)

# # # declare order table struct
# # class Orders(Base):
# #     __tablename__ = 'orders'
# #     id = Column(Integer, primary_key=True, autoincrement=True)
# #     name = Column(String)
# #     username = Column(String,unique=True)
# #     password = Column(String)

# ########### MODEL ADMIN
# # create new admin
# def createAdmin(**params):
#     try: 
#         db.session.add(Admins(**params))
#         return db.session.commit()
#     except exc.IntegrityError as e:
#         db.session.rollback()
#         print("Data sudah ada dalam basis data: {}".format(e))

# #fungsi untuk mengubah isi ke dalam dict
# def row2dict(row):
#     d={}
#     for column in row.__table__.column:
#         d[column.name] = str(getattr(row, column.name))
#     return d

# # view all admin func
# def showAdmin(self):
#     result = db.session.query(Admins).all()
#     result = [row2dict(row) for row in result]
#     return result
#     # # update admin profile
#     # def updateAdmin(self, **params):
#     #     try:
#     #         user_id = params['user_id']
#     #         values = self.restructureParams(**params['values'])
#     #         tx = '''UPDATE admins SET {0} WHERE user_id = {1};'''.format(values,user_id)
#     #         cursor = self.db.cursor()
#     #         cursor.execute(tx)
#     #     except Exception as e:
#     #         print(e)
#     # # delete admin
#     # def deleteAdmin(self, **params):
#     #     try:
#     #         user_id = params['user_id']
#     #         tx = '''DELETE FROM admins WHERE user_id = {0}'''.format(user_id)
#     #         cursor = self.db.cursor()
#     #         cursor.execute(tx)
#     #     except Exception as e:
#     #         print(e)

#     # ########### MODEL ORDER
#     # # create new order
#     # def createOrder(self):
#     #     pass
#     # # view all order
#     # def viewOrder(self):
#     #     pass
#     # # view order by date
#     # def viewOrderByDate(self):
#     #     pass
#     # # delete order
#     # def deleteOrder(self):
#     #     pass

#     # ########### MODEL BEVERAGES
#     # # create new beverages
#     # def createBeverage(self):
#     #     pass
#     # # view all beverages
#     # def viewBeverage(self):
#     #     pass
#     # # view beverage by type
#     # def viewBeverageByType(self):
#     #     pass
#     # # view beverage by price
#     # def viewBeverageByPrice(self):
#     #     pass
#     # # update beverage
#     # def updateBeverage(self):
#     #     pass
#     # # delete beverage
#     # def deleteBeverage(self):
#     #     pass
#     # # restructure param
#     # def restructureParams(self, **data):
#     #     list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
#     #     result = ', '.join(list_data)
#     #     return result
#     # # data commit  
#     # def dataCommit(self):
#     #     self.db.commit()
