import os

SECRET_KEY = 'botina'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + r'C:\Users\loliveira\PycharmProjects\Flask\adopet'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + r'C:\Users\leand\PycharmProjects\bikestore\Alura-Challenge\adopet'
# '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
# SGBD= 'mysql+mysqlconnector',
# servidor = 'localhost',
# usuario = 'root',
# senha = os.environ['senha'],
# database = 'catalogo')

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ['email']
MAIL_PASSWORD = os.environ['senha']
