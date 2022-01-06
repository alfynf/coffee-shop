from mysql.connector import connect

def __init__(self):
    try:
        self.db = connect(host='localhost',
        database = 'coffee_shop',
        user = 'root',
        password = '12345678')
    except Exception as e:
        print(e)

class database:
    def __init__(self):
        pass
    def createAdmin(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            tx =   '''INSERT INTO admins ({0}) values {1};'''.format(column,values)
            cursor = self.db.cursor()
            cursor.execute(tx)
        except Exception as e:
            print(e)
    def showAdmin(self):
        pass
    def showAdminById(self):
        pass
    def updateAdmin(self):
        pass
    def deleteAdmin(self):
        pass
    def dataCommit(self):
        self.db.commit()


