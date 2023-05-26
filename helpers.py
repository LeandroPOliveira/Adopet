import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class FormularioUsuario(FlaskForm):
    usuario = StringField('Usuario',  [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
