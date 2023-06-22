from main import db
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.String(20), nullable=False)
    porte = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.String(40), nullable=False)
    localidade = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), primary_key=False)
    nome = db.Column(db.String(20), primary_key=False)
    senha = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(40), nullable=False)
    sobre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome
