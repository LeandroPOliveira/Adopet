from main import db


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.String(20), nullable=False)
    porte = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.String(40), nullable=False)
    localidade = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuarios(db.Model):
    nome = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome
