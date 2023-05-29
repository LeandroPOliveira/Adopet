from main import app
from flask import render_template, request, url_for, session, flash, redirect
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    estilo_login = 'css/login.css'
    return render_template('login.html', titulo='Login', estilo=estilo_login, form=form)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)  # instanciar a validação do formulario
    usuario = Usuarios.query.filter_by(nome=form.nome.data).first()  # faz a query no banco de dados
    senha = check_password_hash(usuario.senha, form.senha.data)  # checa se a senha corresponde
    proxima_pagina = request.form['proxima']
    if usuario and senha:  # se usuario e senha estiverem corretos, segue o login
        session['usuario_logado'] = usuario.nome
        flash(usuario.nome + 'logado com sucesso')
        if proxima_pagina == 'None':
            proxima_pagina = url_for('index')
        return redirect(proxima_pagina)
    else:
        flash('Usuario não encontrado')
        return redirect(url_for('login'))
