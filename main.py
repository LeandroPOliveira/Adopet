from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_mail import Mail


app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

from views_pet import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)
