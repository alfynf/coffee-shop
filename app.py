from models.customers import database

def createAdminController(data):
    for param in  data['params']:
        mysqldb.createAdmin


if __name__=="__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')

    createAdminController(data)

    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()