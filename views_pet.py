from main import app, mail
from flask import render_template
from models import Pets, Usuarios
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from helpers import FormularioPet, FormularioContato
from flask_mail import Message


@app.route('/')
def index():
    estilo_home = 'css/index.css'
    return render_template('index.html', titulo='Adopet', estilo=estilo_home, visibility='hidden')


@app.route('/home')
def home():
    estilo_home = 'css/home.css'
    # if 'usuario_logado' not in session or session['usuario_logado'] is None:
    #     return redirect(url_for('login', proxima=url_for('home'), estilo=estilo_home, visibility='visible'))

    lista = Pets.query.order_by(Pets.id)

    form = FormularioPet()
    return render_template('home.html', titulo='Home', form=form, pets=lista)


@app.route('/mensagem')
def mensagem():
    estilo_home = 'css/home.css'
    form = FormularioContato()
    return render_template('mensagem.html', titulo='Adopet', estilo=estilo_home, visibility='visible', form=form)


@app.route('/send', methods=['POST', ])
def send():
    form = FormularioContato(request.form)

    nome = form.nome.data
    telefone = form.telefone.data
    animal = form.animal.data
    mensagem = form.mensagem.data

    msg = Message(
        subject=f'{nome} enviou uma mensagem',
        sender=app.config.get('MAIL_USERNAME'),
        recipients=['leandro_lpo2@hotmail.com', app.config.get('MAIL_USERNAME')],
        body=f'''

        {nome} com o telefone {telefone}, te enviou a seguinte mensagem:
        
        {animal}
        
        {mensagem}        
                '''
    )

    mail.send(msg)
    flash('Mensagem enviada com sucesso!', 'sucesso')

    return redirect('/home')


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
