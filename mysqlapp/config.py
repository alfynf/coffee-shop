import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
    
# class database():
#     # connect to mysql database
#     def __init__(self):
#         engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/coffee_shop', echo = True)
#         Session = sessionmaker(bind=engine)
#         self.session = Session()