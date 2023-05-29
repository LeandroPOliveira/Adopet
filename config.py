import os

SECRET_KEY = 'botina'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + r'C:\Users\loliveira\PycharmProjects\Flask\adopet'
# '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
# SGBD= 'mysql+mysqlconnector',
# servidor = 'localhost',
# usuario = 'root',
# senha = os.environ['senha'],
# database = 'catalogo')

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'