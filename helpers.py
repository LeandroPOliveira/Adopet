import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class FormularioUsuario(FlaskForm):  # validar inputs do formulario
    nome = StringField('Usuario',  [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')


class FormularioPet(FlaskForm):
    nome = StringField('Nome do pet', [validators.DataRequired(), validators.Length(min=1, max=50)])
    idade = StringField('Idade', [validators.DataRequired(), validators.Length(min=1, max=20)])
    porte = StringField('Porte', [validators.DataRequired(), validators.Length(min=1, max=30)])
    descricao = StringField('Descricao', [validators.DataRequired(), validators.Length(min=1, max=40)])
    localidade = StringField('Local', [validators.DataRequired(), validators.Length(min=1, max=40)])
    salvar = SubmitField('Salvar')
