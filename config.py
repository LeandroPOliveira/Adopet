import os

SECRET_KEY = 'botina'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + r'C:\Users\leand\PycharmProjects\bikestore\Alura-Challenge\adopet'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '/home/leandro500/Alura-Challenge/adopet'  # Pythonanywhere
# SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
# SGBD= 'mysql+mysqlconnector',
# servidor = 'leandro500.mysql.pythonanywhere-services.com',
# usuario = 'leandro500',
# senha = os.environ['senha'],
# database = 'leandro500$adopet')

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ['email']
MAIL_PASSWORD = os.environ['senha']
