from main import app
from flask import render_template
from models import Pets
from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioPet


@app.route('/')
def index():
    estilo_home = 'css/index.css'
    return render_template('index.html', titulo='Adopet', estilo=estilo_home, visibility='hidden')


@app.route('/home')
def home():
    estilo_home = 'css/home.css'
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('home'), estilo=estilo_home, visibility='visible'))

    lista = Pets.query.order_by(Pets.id)

    form = FormularioPet()
    return render_template('home.html', titulo='Home', form=form, pets=lista)


@app.route('/mensagem')
def mensagem():
    estilo_home = 'css/home.css'
    return render_template('mensagem.html', titulo='Adopet', estilo=estilo_home, visibility='visible')