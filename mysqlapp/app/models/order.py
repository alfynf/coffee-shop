# from enum import unique
from mysql.connector import connect
# from app import database
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import exc, delete, update

###################################################### NON ORM
############## DECLARE MODELS
class order_database:
    # connect to mysql database
    def __init__(self):
        try:
            self.db = connect(host='localhost',
            database = 'coffee_shop',
            user = 'root',
            password = '12345678')
        except Exception as e:
            print(e)

    ########### MODEL ORDER
    # create new order
    def createOrder(self, **params):
        try:
            column = ', '.join(list(params.keys()))
            values = tuple(list(params.values()))
            tx =   '''INSERT INTO orders ({0}) values {1};'''.format(column,values)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)
    # create order detail
    def createOrderDetail(self, **params):
        try:
            column = ', '.join(list(params.keys()))
            values = tuple(list(params.values()))
            tx =   '''INSERT INTO order_beverage ({0}) values {1};'''.format(column,values)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)   
    # view all order
    def viewOrder(self):
        try:
            tx = '''SELECT * FROM orders ORDER BY order_id DESC;'''
            cursor = self.db.cursor()
            cursor.execute(tx)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    # view order by date
    def viewOrderByDate(self, **params):
        try:
            date = params["date"]
            tx = '''SELECT * FROM orders WHERE created_at = "{0}";'''.format(date)
            cursor = self.db.cursor()
            cursor.execute(tx)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    # delete order
    def deleteOrder(self, **params):
        try:
            order_id = params['order_id']
            tx = '''DELETE FROM orders WHERE order_id = {0}'''.format(order_id)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)
    # restructure param
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result
    # data commit  
    def dataCommit(self):
        self.db.commit()