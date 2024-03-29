import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, TextAreaField


class FormularioUsuario(FlaskForm):  # validar inputs do formulario
    email = EmailField('Email', [validators.DataRequired(), validators.Length(min=1, max=50)])
    nome = StringField('Nome',  [validators.DataRequired(), validators.Length(min=1, max=40)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    conf_senha = PasswordField('Confirme sua senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
    cadastro = SubmitField('Cadastro')


class FormularioPerfil(FlaskForm):
    nome = StringField('Usuario', [validators.DataRequired(), validators.Length(min=1, max=40)])
    telefone = StringField('Telefone',  [validators.DataRequired(), validators.Length(min=1, max=20)])
    cidade = StringField('Cidade', [validators.DataRequired(), validators.Length(min=1, max=40)])
    sobre = TextAreaField('Sobre', [validators.DataRequired(), validators.Length(min=1, max=200)])
    salvar = SubmitField('Salvar')


class FormularioPet(FlaskForm):
    nome = StringField('Nome do pet', [validators.DataRequired(), validators.Length(min=1, max=50)])
    idade = StringField('Idade', [validators.DataRequired(), validators.Length(min=1, max=10)])
    porte = StringField('Porte', [validators.DataRequired(), validators.Length(min=1, max=30)])
    descricao = StringField('Descricao', [validators.DataRequired(), validators.Length(min=1, max=50)])
    localidade = StringField('Local', [validators.DataRequired(), validators.Length(min=1, max=40)])
    salvar = SubmitField('Salvar')


class FormularioContato(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=40)])
    telefone = StringField('Telefone', [validators.DataRequired(), validators.Length(min=1, max=20)])
    animal = StringField('Nome do animal', [validators.DataRequired(), validators.Length(min=1, max=50)])
    mensagem = TextAreaField('Mensagem', [validators.DataRequired(), validators.Length(min=1, max=150)])
    enviar = SubmitField('Enviar')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'user{id}' in nome_arquivo:
            return nome_arquivo

    return 'Usuário.png'